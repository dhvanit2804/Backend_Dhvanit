"""
LibraDesk - Single-file implementation for the TechFix Advance App assessment.
Features:
- SQLite persistence for members, books, borrowings, invoices
- Classes (Member, Book, LibrarySystem) with inheritance and exceptions
- Tkinter GUI with role-based login (Admin / Librarian)
- Borrow / Return flow, overdue fine calculation, invoice generation (txt/csv)
- Regex-based search for title/author/genre
- File I/O for invoices
- Basic reporting: overdue list, most borrowed
"""

import sqlite3
import re
import csv
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

# -------------- Exceptions ----------------
class LibraryError(Exception):
    pass

class NotAvailableError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

# -------------- Data classes ----------------
class Member:
    def __init__(self, member_id, name, email, role='member'):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.role = role

class Book:
    def __init__(self, book_id, title, author, genre, isbn, total_qty, available_qty):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.total_qty = total_qty
        self.available_qty = available_qty

# -------------- Library System (DB + Logic) ----------------
class LibrarySystem:
    DB_FILE = "libradesk.db"
    FINE_PER_DAY = 10.0   # currency units per day overdue
    TAX_RATE = 0.05       # 5% tax for invoices

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_FILE)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()
        self._ensure_default_users()

    def _create_tables(self):
        c = self.conn.cursor()
        c.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            role TEXT
        );
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT DEFAULT 'member'
        );
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            isbn TEXT UNIQUE,
            total_qty INTEGER,
            available_qty INTEGER
        );
        CREATE TABLE IF NOT EXISTS borrowings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            due_date TEXT,
            return_date TEXT,
            fine_paid REAL DEFAULT 0,
            FOREIGN KEY(member_id) REFERENCES members(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        );
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            borrowing_id INTEGER,
            generated_on TEXT,
            fine REAL,
            tax REAL,
            total REAL,
            saved_path TEXT
        );
        CREATE TABLE IF NOT EXISTS borrow_count (
            book_id INTEGER PRIMARY KEY,
            count INTEGER DEFAULT 0,
            FOREIGN KEY(book_id) REFERENCES books(id)
        );
        """)
        self.conn.commit()

    def _ensure_default_users(self):
        # Add simple users for role-based login (in real app use secure hashing)
        c = self.conn.cursor()
        # username/password/role
        users = [
            ('admin', 'admin123', 'admin'),
            ('librarian', 'lib123', 'librarian')
        ]
        for u,p,r in users:
            c.execute("INSERT OR IGNORE INTO users(username,password,role) VALUES(?,?,?)", (u,p,r))
        self.conn.commit()

    # ---------- Member operations ----------
    def add_member(self, name, email, role='member'):
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO members(name,email,role) VALUES(?,?,?)", (name,email,role))
            self.conn.commit()
            return c.lastrowid
        except sqlite3.IntegrityError as e:
            raise LibraryError("Member with this email already exists.")

    def update_member(self, member_id, name=None, email=None, role=None):
        c = self.conn.cursor()
        row = c.execute("SELECT * FROM members WHERE id=?", (member_id,)).fetchone()
        if not row:
            raise MemberNotFoundError("Member not found.")
        vals = {"name": name or row["name"], "email": email or row["email"], "role": role or row["role"]}
        c.execute("UPDATE members SET name=?, email=?, role=? WHERE id=?", (vals["name"], vals["email"], vals["role"], member_id))
        self.conn.commit()

    def get_member(self, member_id):
        c = self.conn.cursor()
        row = c.execute("SELECT * FROM members WHERE id=?", (member_id,)).fetchone()
        if not row:
            raise MemberNotFoundError("Member not found.")
        return Member(row['id'], row['name'], row['email'], row['role'])

    def list_members(self):
        c = self.conn.cursor()
        return [dict(r) for r in c.execute("SELECT * FROM members").fetchall()]

    # ---------- Book operations ----------
    def add_book(self, title, author, genre, isbn, qty):
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO books(title,author,genre,isbn,total_qty,available_qty) VALUES(?,?,?,?,?,?)",
                      (title, author, genre, isbn, qty, qty))
            book_id = c.lastrowid
            c.execute("INSERT OR IGNORE INTO borrow_count(book_id,count) VALUES(?,?)", (book_id, 0))
            self.conn.commit()
            return book_id
        except sqlite3.IntegrityError:
            raise LibraryError("Book with this ISBN already exists.")

    def update_book(self, book_id, **kwargs):
        c = self.conn.cursor()
        row = c.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
        if not row:
            raise LibraryError("Book not found.")
        title = kwargs.get("title", row["title"])
        author = kwargs.get("author", row["author"])
        genre = kwargs.get("genre", row["genre"])
        isbn = kwargs.get("isbn", row["isbn"])
        total_qty = kwargs.get("total_qty", row["total_qty"])
        # if total_qty changed, update available_qty accordingly
        available_qty = row["available_qty"] + (total_qty - row["total_qty"])
        if available_qty < 0:
            available_qty = 0
        c.execute("UPDATE books SET title=?,author=?,genre=?,isbn=?,total_qty=?,available_qty=? WHERE id=?",
                  (title,author,genre,isbn,total_qty,available_qty,book_id))
        self.conn.commit()

    def list_books(self):
        c = self.conn.cursor()
        return [dict(r) for r in c.execute("SELECT * FROM books").fetchall()]

    def search_books(self, pattern, field='title'):
        # Use regex - pattern expected as Python regex; search case-insensitive
        if field not in ('title','author','genre'):
            raise ValueError("Field must be title, author, or genre.")
        c = self.conn.cursor()
        rows = c.execute(f"SELECT * FROM books").fetchall()
        prog = re.compile(pattern, re.IGNORECASE)
        return [dict(r) for r in rows if prog.search(r[field])]

    # ---------- Borrow / Return ----------
    def borrow_book(self, member_id, book_id, days=14):
        c = self.conn.cursor()
        # Validate member
        m = c.execute("SELECT * FROM members WHERE id=?", (member_id,)).fetchone()
        if not m:
            raise MemberNotFoundError("Member not found.")
        b = c.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
        if not b:
            raise LibraryError("Book not found.")
        if b['available_qty'] <= 0:
            raise NotAvailableError("Book is not available right now.")
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=days)
        c.execute("INSERT INTO borrowings(member_id,book_id,borrow_date,due_date) VALUES(?,?,?,?)",
                  (member_id, book_id, borrow_date.isoformat(), due_date.isoformat()))
        # Update availability
        c.execute("UPDATE books SET available_qty = available_qty - 1 WHERE id=?", (book_id,))
        # increment borrow_count
        c.execute("INSERT OR IGNORE INTO borrow_count(book_id,count) VALUES(?,0)", (book_id,))
        c.execute("UPDATE borrow_count SET count = count + 1 WHERE book_id=?", (book_id,))
        self.conn.commit()
        return c.lastrowid

    def return_book(self, borrowing_id):
        c = self.conn.cursor()
        br = c.execute("SELECT * FROM borrowings WHERE id=?", (borrowing_id,)).fetchone()
        if not br:
            raise LibraryError("Borrowing record not found.")
        if br['return_date'] is not None:
            raise LibraryError("This book has already been returned.")
        return_date = datetime.now()
        due_date = datetime.fromisoformat(br['due_date'])
        fine = 0.0
        if return_date > due_date:
            delta = (return_date.date() - due_date.date()).days
            fine = delta * self.FINE_PER_DAY
        # Update borrowing
        c.execute("UPDATE borrowings SET return_date=?, fine_paid=? WHERE id=?", (return_date.isoformat(), fine, borrowing_id))
        # Update book availability
        c.execute("UPDATE books SET available_qty = available_qty + 1 WHERE id=?", (br['book_id'],))
        self.conn.commit()
        # Create invoice if fine > 0
        invoice_path = None
        invoice_id = None
        if fine > 0:
            invoice_id, invoice_path = self.generate_invoice(borrowing_id, fine)
        return {"fine": fine, "invoice_id": invoice_id, "invoice_path": invoice_path}

    # ---------- Invoice generation ----------
    def generate_invoice(self, borrowing_id, fine):
        c = self.conn.cursor()
        borrowing = c.execute("SELECT b.*, m.name as member_name, bk.title as book_title, bk.isbn as isbn FROM borrowings b "
                              "JOIN members m ON b.member_id = m.id JOIN books bk ON b.book_id = bk.id "
                              "WHERE b.id=?", (borrowing_id,)).fetchone()
        if not borrowing:
            raise LibraryError("Borrowing not found for invoice.")
        tax = round(fine * self.TAX_RATE, 2)
        total = round(fine + tax, 2)
        generated_on = datetime.now().isoformat()
        # Save invoice to db (path empty for now)
        c.execute("INSERT INTO invoices(borrowing_id,generated_on,fine,tax,total) VALUES(?,?,?,?,?)",
                  (borrowing_id, generated_on, fine, tax, total))
        invoice_id = c.lastrowid
        # Save invoice to file (txt and csv copy)
        invoice_txt = self._format_invoice_text(invoice_id, borrowing, fine, tax, total, generated_on)
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)
        txt_path = os.path.join(folder, f"invoice_{invoice_id}.txt")
        csv_path = os.path.join(folder, f"invoice_{invoice_id}.csv")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(invoice_txt)
        # csv
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvf:
            writer = csv.writer(csvf)
            writer.writerow(["Invoice ID", "Borrowing ID", "Member", "Book", "ISBN", "Generated On", "Fine", "Tax", "Total"])
            writer.writerow([invoice_id, borrowing['id'], borrowing['member_name'], borrowing['book_title'], borrowing['isbn'], generated_on, fine, tax, total])
        # Update invoice saved_path in DB
        c.execute("UPDATE invoices SET saved_path=? WHERE id=?", (txt_path, invoice_id))
        self.conn.commit()
        return invoice_id, txt_path

    def _format_invoice_text(self, invoice_id, borrowing, fine, tax, total, generated_on):
        lines = [
            f"Invoice ID: {invoice_id}",
            f"Generated On: {generated_on}",
            "---------------------------",
            f"Member: {borrowing['member_name']}",
            f"Book: {borrowing['book_title']}",
            f"ISBN: {borrowing['isbn']}",
            f"Borrowed On: {borrowing['borrow_date']}",
            f"Due Date: {borrowing['due_date']}",
            "---------------------------",
            f"Fine: {fine:.2f}",
            f"Tax ({int(self.TAX_RATE*100)}%): {tax:.2f}",
            f"Total: {total:.2f}",
            "---------------------------",
            "Thank you for using LibraDesk!"
        ]
        return "\n".join(lines)

    # ---------- Reports ----------
    def overdue_list(self):
        c = self.conn.cursor()
        now_iso = datetime.now().isoformat()
        rows = c.execute("SELECT br.id, m.name as member_name, bk.title as book_title, br.due_date "
                         "FROM borrowings br JOIN members m ON br.member_id = m.id JOIN books bk ON br.book_id = bk.id "
                         "WHERE br.return_date IS NULL AND br.due_date < ?", (now_iso,)).fetchall()
        return [dict(r) for r in rows]

    def most_borrowed(self, top_n=10):
        c = self.conn.cursor()
        rows = c.execute("SELECT bc.book_id, bc.count, bk.title FROM borrow_count bc JOIN books bk ON bc.book_id = bk.id "
                         "ORDER BY bc.count DESC LIMIT ?", (top_n,)).fetchall()
        return [dict(r) for r in rows]

    # ---------- Auth ----------
    def authenticate(self, username, password):
        c = self.conn.cursor()
        row = c.execute("SELECT role FROM users WHERE username=? AND password=?", (username,password)).fetchone()
        if row:
            return row['role']
        return None

    # Close
    def close(self):
        self.conn.close()

# -------------- GUI ----------------
class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LibraDesk")
        self.system = LibrarySystem()
        self.current_role = None
        self.current_user = None
        self._build_login()

    def _build_login(self):
        for w in self.root.winfo_children():
            w.destroy()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text="LibraDesk - Login", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky='e')
        username = ttk.Entry(frame)
        username.grid(row=1, column=1)
        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky='e')
        password = ttk.Entry(frame, show='*')
        password.grid(row=2, column=1)

        def do_login():
            u = username.get().strip()
            p = password.get().strip()
            role = self.system.authenticate(u,p)
            if role:
                self.current_role = role
                self.current_user = u
                messagebox.showinfo("Login", f"Welcome {u} ({role})")
                self._build_main()
            else:
                messagebox.showerror("Login failed", "Invalid credentials.")

        ttk.Button(frame, text="Login", command=do_login).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Label(frame, text="Use 'admin'/'admin123' or 'librarian'/'lib123'").grid(row=4, column=0, columnspan=2)

    def _build_main(self):
        for w in self.root.winfo_children():
            w.destroy()
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # Members tab (both roles can manage members; admin has more rights)
        members_frame = ttk.Frame(notebook, padding=8)
        notebook.add(members_frame, text="Members")
        self._members_tab(members_frame)

        # Books tab
        books_frame = ttk.Frame(notebook, padding=8)
        notebook.add(books_frame, text="Books")
        self._books_tab(books_frame)

        # Borrow/Return tab (librarian + admin)
        borrow_frame = ttk.Frame(notebook, padding=8)
        notebook.add(borrow_frame, text="Borrow/Return")
        self._borrow_tab(borrow_frame)

        # Search/Reports tab
        reports_frame = ttk.Frame(notebook, padding=8)
        notebook.add(reports_frame, text="Search & Reports")
        self._reports_tab(reports_frame)

        # Logout button
        btn_frame = ttk.Frame(self.root, padding=6)
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame, text="Logout", command=self._logout).pack(side='right')

    def _logout(self):
        self.current_role = None
        self.current_user = None
        self._build_login()

    # ---------- Members tab ----------
    def _members_tab(self, frame):
        # Left: form, Right: list
        form = ttk.LabelFrame(frame, text="Add / Edit Member", padding=8)
        form.pack(side='left', fill='y', padx=6, pady=6)
        ttk.Label(form, text="Name:").grid(row=0, column=0, sticky='e')
        name_e = ttk.Entry(form, width=25)
        name_e.grid(row=0, column=1)
        ttk.Label(form, text="Email:").grid(row=1, column=0, sticky='e')
        email_e = ttk.Entry(form, width=25)
        email_e.grid(row=1, column=1)

        def add_member():
            name = name_e.get().strip()
            email = email_e.get().strip()
            if not name or not email:
                messagebox.showerror("Input error", "Name and email required.")
                return
            try:
                mid = self.system.add_member(name, email)
                messagebox.showinfo("Added", f"Member added with ID {mid}")
                refresh_list()
            except LibraryError as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(form, text="Add Member", command=add_member).grid(row=2, column=0, columnspan=2, pady=6)

        # Member list
        list_frame = ttk.LabelFrame(frame, text="Members List", padding=8)
        list_frame.pack(side='left', fill='both', expand=True, padx=6, pady=6)
        cols = ("id","name","email","role")
        tree = ttk.Treeview(list_frame, columns=cols, show='headings')
        for c in cols:
            tree.heading(c, text=c.title())
        tree.pack(fill='both', expand=True)

        def refresh_list():
            for r in tree.get_children():
                tree.delete(r)
            for m in self.system.list_members():
                tree.insert('', 'end', values=(m['id'], m['name'], m['email'], m['role']))
        refresh_list()

    # ---------- Books tab ----------
    def _books_tab(self, frame):
        form = ttk.LabelFrame(frame, text="Add / Edit Book", padding=8)
        form.pack(side='left', fill='y', padx=6, pady=6)
        labels = ["Title","Author","Genre","ISBN","Qty"]
        entries = {}
        for i,l in enumerate(labels):
            ttk.Label(form, text=l+':').grid(row=i, column=0, sticky='e')
            e = ttk.Entry(form, width=30)
            e.grid(row=i, column=1)
            entries[l.lower()] = e

        def add_book():
            try:
                title = entries['title'].get().strip()
                author = entries['author'].get().strip()
                genre = entries['genre'].get().strip()
                isbn = entries['isbn'].get().strip()
                qty = int(entries['qty'].get().strip())
                if not (title and isbn and qty>0):
                    messagebox.showerror("Input error","Title, ISBN and Qty required.")
                    return
                bid = self.system.add_book(title, author, genre, isbn, qty)
                messagebox.showinfo("Added", f"Book added id {bid}")
                refresh_books()
            except ValueError:
                messagebox.showerror("Input error","Qty must be integer.")
            except LibraryError as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(form, text="Add Book", command=add_book).grid(row=len(labels), column=0, columnspan=2, pady=6)

        # Book list
        listf = ttk.LabelFrame(frame, text="Books", padding=8)
        listf.pack(side='left', fill='both', expand=True, padx=6, pady=6)
        cols = ("id","title","author","genre","isbn","total_qty","available_qty")
        tree = ttk.Treeview(listf, columns=cols, show='headings')
        for c in cols:
            tree.heading(c, text=c.title())
        tree.pack(fill='both', expand=True)

        def refresh_books():
            for r in tree.get_children():
                tree.delete(r)
            for b in self.system.list_books():
                tree.insert('', 'end', values=(b['id'], b['title'], b['author'], b['genre'], b['isbn'], b['total_qty'], b['available_qty']))
        refresh_books()

    # ---------- Borrow / Return tab ----------
    def _borrow_tab(self, frame):
        # Borrow area
        borrow_frame = ttk.LabelFrame(frame, text="Borrow Book", padding=8)
        borrow_frame.pack(fill='x', padx=6, pady=6)
        ttk.Label(borrow_frame, text="Member ID:").grid(row=0,column=0,sticky='e')
        member_e = ttk.Entry(borrow_frame, width=10)
        member_e.grid(row=0,column=1)
        ttk.Label(borrow_frame, text="Book ID:").grid(row=0,column=2,sticky='e')
        book_e = ttk.Entry(borrow_frame, width=10)
        book_e.grid(row=0,column=3)
        ttk.Label(borrow_frame, text="Days:").grid(row=0,column=4,sticky='e')
        days_e = ttk.Entry(borrow_frame, width=5)
        days_e.insert(0,"14")
        days_e.grid(row=0,column=5)

        def do_borrow():
            try:
                mid = int(member_e.get().strip())
                bid = int(book_e.get().strip())
                days = int(days_e.get().strip())
                bor_id = self.system.borrow_book(mid, bid, days)
                messagebox.showinfo("Borrowed", f"Borrow recorded: id {bor_id}")
            except ValueError:
                messagebox.showerror("Input error","IDs and days must be integer.")
            except LibraryError as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(borrow_frame, text="Borrow", command=do_borrow).grid(row=0,column=6,padx=6)

        # Return area
        return_frame = ttk.LabelFrame(frame, text="Return Book", padding=8)
        return_frame.pack(fill='x', padx=6, pady=6)
        ttk.Label(return_frame, text="Borrowing ID:").grid(row=0,column=0,sticky='e')
        borrowid_e = ttk.Entry(return_frame, width=10)
        borrowid_e.grid(row=0,column=1)

        def do_return():
            try:
                bid = int(borrowid_e.get().strip())
                res = self.system.return_book(bid)
                if res['fine'] > 0:
                    messagebox.showinfo("Returned", f"Book returned. Fine: {res['fine']:.2f}. Invoice saved at {res['invoice_path']}")
                else:
                    messagebox.showinfo("Returned", "Book returned. No fine.")
            except ValueError:
                messagebox.showerror("Input error","Borrowing ID must be integer.")
            except LibraryError as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(return_frame, text="Return", command=do_return).grid(row=0,column=2,padx=6)

        # List open borrowings
        list_frame = ttk.LabelFrame(frame, text="Open Borrowings", padding=8)
        list_frame.pack(fill='both', expand=True, padx=6, pady=6)
        cols = ("id","member_id","member_name","book_id","book_title","borrow_date","due_date")
        tree = ttk.Treeview(list_frame, columns=cols, show='headings')
        for c in cols:
            tree.heading(c, text=c.title())
        tree.pack(fill='both', expand=True)

        def refresh_open():
            for r in tree.get_children():
                tree.delete(r)
            q = ("SELECT br.id, br.member_id, m.name as member_name, br.book_id, bk.title as book_title, br.borrow_date, br.due_date "
                 "FROM borrowings br JOIN members m ON br.member_id=m.id JOIN books bk ON br.book_id=bk.id "
                 "WHERE br.return_date IS NULL")
            rows = self.system.conn.cursor().execute(q).fetchall()
            for r in rows:
                tree.insert('', 'end', values=(r['id'], r['member_id'], r['member_name'], r['book_id'], r['book_title'], r['borrow_date'], r['due_date']))
        refresh_open()
        # add refresh button
        ttk.Button(list_frame, text="Refresh", command=refresh_open).pack(side='bottom', pady=6)

    # ---------- Reports / Search ----------
    def _reports_tab(self, frame):
        upper = ttk.LabelFrame(frame, text="Regex Search", padding=8)
        upper.pack(fill='x', padx=6, pady=6)
        ttk.Label(upper, text="Field:").grid(row=0,column=0)
        field_var = tk.StringVar(value='title')
        ttk.Combobox(upper, textvariable=field_var, values=['title','author','genre'], width=10).grid(row=0,column=1)
        pattern_e = ttk.Entry(upper, width=40)
        pattern_e.grid(row=0,column=2)
        result_frame = ttk.LabelFrame(frame, text="Search Results", padding=8)
        result_frame.pack(fill='both', expand=True, padx=6, pady=6)
        cols = ("id","title","author","genre","isbn","available")
        tree = ttk.Treeview(result_frame, columns=cols, show='headings')
        for c in cols:
            tree.heading(c, text=c.title())
        tree.pack(fill='both', expand=True)

        def do_search():
            pat = pattern_e.get().strip()
            f = field_var.get()
            if not pat:
                messagebox.showerror("Input", "Enter regex pattern.")
                return
            try:
                res = self.system.search_books(pat, f)
                for r in tree.get_children():
                    tree.delete(r)
                for b in res:
                    tree.insert('', 'end', values=(b['id'], b['title'], b['author'], b['genre'], b['isbn'], b['available_qty']))
            except re.error as e:
                messagebox.showerror("Regex error", str(e))

        ttk.Button(upper, text="Search", command=do_search).grid(row=0,column=3,padx=6)

        # Reports: overdue and most borrowed
        lower = ttk.LabelFrame(frame, text="Reports", padding=8)
        lower.pack(fill='both', expand=True, padx=6, pady=6)
        ttk.Button(lower, text="Overdue List", command=self._show_overdue).pack(side='left', padx=6)
        ttk.Button(lower, text="Most Borrowed", command=self._show_most_borrowed).pack(side='left', padx=6)
        ttk.Button(lower, text="Open Invoices Folder", command=self._open_invoices_folder).pack(side='left', padx=6)

    def _show_overdue(self):
        overdue = self.system.overdue_list()
        if not overdue:
            messagebox.showinfo("Overdue", "No overdue borrowings.")
            return
        text = "\n".join([f"BorrowID {r['id']} | Member: {r['member_name']} | Book: {r['book_title']} | Due: {r['due_date']}" for r in overdue])
        self._show_text_window("Overdue List", text)

    def _show_most_borrowed(self):
        top = self.system.most_borrowed(10)
        if not top:
            messagebox.showinfo("Most Borrowed", "No borrowings yet.")
            return
        text = "\n".join([f"{r['title']} (BookID {r['book_id']}): {r['count']} borrows" for r in top])
        self._show_text_window("Most Borrowed Books", text)

    def _open_invoices_folder(self):
        folder = os.path.abspath("invoices")
        if not os.path.isdir(folder):
            messagebox.showinfo("Invoices", "No invoices yet.")
            return
        # try to open folder in OS file explorer
        try:
            if os.name == 'nt':
                os.startfile(folder)
            elif os.name == 'posix':
                os.system(f'xdg-open "{folder}"')
            else:
                messagebox.showinfo("Invoices folder", folder)
        except Exception:
            messagebox.showinfo("Invoices folder", folder)

    def _show_text_window(self, title, text):
        win = tk.Toplevel(self.root)
        win.title(title)
        txt = tk.Text(win, wrap='word', width=80, height=25)
        txt.insert('1.0', text)
        txt.pack(fill='both', expand=True)
        ttk.Button(win, text="Close", command=win.destroy).pack(pady=6)

# -------------- Run ----------------
def main():
    root = tk.Tk()
    root.geometry("900x600")
    app = AppGUI(root)
    root.mainloop()
    app.system.close()

if __name__ == "__main__":
    main()
