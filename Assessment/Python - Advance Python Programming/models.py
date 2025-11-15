import sqlite3
from datetime import datetime, timedelta

DB_NAME = "libradesk.db"


def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Members Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        membership_date TEXT
    )
    """)

    # Books table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        genre TEXT,
        isbn TEXT UNIQUE,
        available INTEGER DEFAULT 1
    )
    """)

    # Borrowing table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS borrowings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        book_id INTEGER,
        borrow_date TEXT,
        due_date TEXT,
        return_date TEXT,
        fine REAL DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    # Seed users if empty
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO users(username,password,role) VALUES('admin','admin123','admin')")
        cur.execute("INSERT INTO users(username,password,role) VALUES('librarian','lib123','librarian')")

    conn.commit()
    conn.close()


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def can_add_books(self):
        return False
    
    def can_view_reports(self):
        return False
    
class Admin(User):
    def __init__(self, username):
        super().__init__(username, "admin")
    
    def can_add_books(self):
        return True

    def can_view_reports(self):
        return True
    
class Librarian(User):
    def __init__(self, username):
        super().__init__(username, "librarian")
    
    def can_view_reports(self):
        return True
    

class Book:
    def __init__(self, title, author, genre, isbn, available=True, _id=None):
        self.id = _id
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.available = available

    def save(self):
        conn = get_connection()
        cur = conn.cursor()

        if self.id is None:
            cur.execute("INSERT INTO books(title,author,genre,isbn,available) VALUES(?,?,?,?,?)",
                        (self.title, self.author, self.genre, self.isbn, int(self.available)))
        else:
            cur.execute("UPDATE books SET title=?,author=?,genre=?,isbn=?,available=? WHERE id=?",
                        (self.title, self.author, self.genre, self.isbn, int(self.available), self.id))

        conn.commit()
        conn.close()

class Member:
    def __init__(self, name, email, phone, membership_date=None, _id=None):
        self.id = _id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_date = membership_date or datetime.now().strftime("%Y-%m-%d")

    def save(self):
        conn = get_connection()
        cur = conn.cursor()

        if self.id is None:
            cur.execute("INSERT INTO members(name,email,phone,membership_date) VALUES(?,?,?,?)",
                        (self.name, self.email, self.phone, self.membership_date))
        else:
            cur.execute("UPDATE members SET name=?,email=?,phone=?,membership_date=? WHERE id=?",
                        (self.name, self.email, self.phone, self.membership_date, self.id))

        conn.commit()
        conn.close()

class OverdueBookError(Exception):
    pass

class Borrowing:
    FINE_PER_DAY = 5

    def __init__(self, member_id, book_id, borrow_date, due_date, return_date=None, fine=0, _id=None):
        self.id = _id
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine

    def save(self):
        conn = get_connection()
        cur = conn.cursor()

        if self.id is None:
            cur.execute("""
            INSERT INTO borrowings(member_id,book_id,borrow_date,due_date,return_date,fine)
            VALUES(?,?,?,?,?,?)
            """, (self.member_id, self.book_id, self.borrow_date, self.due_date, self.return_date, self.fine))
        else:
            cur.execute("""
            UPDATE borrowings SET member_id=?,book_id=?,borrow_date=?,due_date=?,return_date=?,fine=? WHERE id=?
            """, (self.member_id, self.book_id, self.borrow_date, self.due_date, self.return_date, self.fine, self.id))

        conn.commit()
        conn.close()

    def calculate_fine(self):
        if not self.return_date:
            return 0
        d1 = datetime.strptime(self.due_date, "%Y-%m-%d")
        d2 = datetime.strptime(self.return_date, "%Y-%m-%d")

        late_days = (d2 - d1).days
        return max(0, late_days * Borrowing.FINE_PER_DAY)