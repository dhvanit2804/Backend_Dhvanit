import tkinter as tk
from tkinter import messagebox
from models import *
from utils import *

init_db()

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT username,password,role FROM users WHERE username=? AND password=?", (user, pwd))
    row = cur.fetchone()
    conn.close()

    if row:
        username, password, role = row
        if role == "admin":
            usr = Admin(username)
        else:
            usr = Librarian(username)

        messagebox.showinfo("Login Success", f"Welcome {username} ({role})")
        root.destroy()
        open_dashboard(usr)
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def open_dashboard(user):
    dash = tk.Tk()
    dash.title("LibraDesk Dashboard")

    tk.Label(dash, text=f"Logged in as: {user.username} ({user.role})").pack()

    tk.Button(dash, text="Add Book", command=add_book_window).pack(pady=5)
    tk.Button(dash, text="Add Member", command=add_member_window).pack(pady=5)
    tk.Button(dash, text="Borrow Book", command=borrow_window).pack(pady=5)
    tk.Button(dash, text="Return Book", command=return_window).pack(pady=5)
    tk.Button(dash, text="Search Books", command=search_window).pack(pady=5)
    tk.Button(dash, text="Reports", command=report_window).pack(pady=5)

    dash.mainloop()


# ---------------- SIMPLE FORMS ---------------- #

def add_book_window():
    win = tk.Toplevel()
    win.title("Add Book")

    tk.Label(win, text="Title").grid(row=0, column=0)
    tk.Label(win, text="Author").grid(row=1, column=0)
    tk.Label(win, text="Genre").grid(row=2, column=0)
    tk.Label(win, text="ISBN").grid(row=3, column=0)

    t = tk.Entry(win)
    a = tk.Entry(win)
    g = tk.Entry(win)
    i = tk.Entry(win)

    t.grid(row=0, column=1)
    a.grid(row=1, column=1)
    g.grid(row=2, column=1)
    i.grid(row=3, column=1)

    def save():
        book = Book(t.get(), a.get(), g.get(), i.get())
        book.save()
        messagebox.showinfo("Saved", "Book added successfully!")

    tk.Button(win, text="Save", command=save).grid(row=4, column=1)


def add_member_window():
    win = tk.Toplevel()
    win.title("Add Member")

    tk.Label(win, text="Name").grid(row=0, column=0)
    tk.Label(win, text="Email").grid(row=1, column=0)
    tk.Label(win, text="Phone").grid(row=2, column=0)

    n = tk.Entry(win)
    e = tk.Entry(win)
    p = tk.Entry(win)

    n.grid(row=0, column=1)
    e.grid(row=1, column=1)
    p.grid(row=2, column=1)

    def save():
        mem = Member(n.get(), e.get(), p.get())
        mem.save()
        messagebox.showinfo("Saved", "Member added successfully!")

    tk.Button(win, text="Save", command=save).grid(row=3, column=1)


def borrow_window():
    win = tk.Toplevel()
    win.title("Borrow Book")

    tk.Label(win, text="Member ID").grid(row=0, column=0)
    tk.Label(win, text="Book ID").grid(row=1, column=0)

    m = tk.Entry(win)
    b = tk.Entry(win)

    m.grid(row=0, column=1)
    b.grid(row=1, column=1)

    def borrow():
        member_id = int(m.get())
        book_id = int(b.get())

        borrow_date = datetime.now().strftime("%Y-%m-%d")
        due = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

        br = Borrowing(member_id, book_id, borrow_date, due)
        br.save()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Book Borrowed!")

    tk.Button(win, text="Borrow", command=borrow).grid(row=3, column=1)


def return_window():
    win = tk.Toplevel()
    win.title("Return Book")

    tk.Label(win, text="Borrowing ID").grid(row=0, column=0)
    br_id = tk.Entry(win)
    br_id.grid(row=0, column=1)

    def ret():
        bid = int(br_id.get())
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT book_id,due_date FROM borrowings WHERE id=?", (bid,))
        row = cur.fetchone()

        if not row:
            messagebox.showerror("Error", "Borrowing ID Not Found")
            return

        book_id, due_date = row
        ret_date = datetime.now().strftime("%Y-%m-%d")

        d1 = datetime.strptime(due_date, "%Y-%m-%d")
        d2 = datetime.strptime(ret_date, "%Y-%m-%d")

        late = max(0, (d2 - d1).days * 5)

        cur.execute("UPDATE borrowings SET return_date=?,fine=? WHERE id=?", (ret_date, late, bid))
        cur.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Returned", f"Book returned! Fine = ₹{late}")

    tk.Button(win, text="Return", command=ret).grid(row=2, column=1)


def search_window():
    win = tk.Toplevel()
    win.title("Search Books")

    tk.Label(win, text="Regex Pattern").grid(row=0, column=0)
    p = tk.Entry(win)
    p.grid(row=0, column=1)

    def search():
        results = search_books(p.get(), "title")
        msg = "\n".join([f"{b.id} - {b.title}" for b in results]) or "No match"
        messagebox.showinfo("Result", msg)

    tk.Button(win, text="Search", command=search).grid(row=1, column=1)


def report_window():
    win = tk.Toplevel()
    win.title("Reports")

    overdue = overdue_report()
    top_books = most_borrowed_books()

    text = "---- Overdue Books ----\n"
    for r in overdue:
        text += f"{r[0]} - {r[1]} (Due: {r[2]})\n"

    text += "\n---- Most Borrowed ----\n"
    for r in top_books:
        text += f"{r[0]} - {r[1]} times\n"

    tk.Label(win, text=text, justify="left").pack()


# ---------------- MAIN LOGIN WINDOW ---------------- #

root = tk.Tk()
root.title("LibraDesk Login")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Password").grid(row=1, column=0)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=3, column=1)

root.mainloop()