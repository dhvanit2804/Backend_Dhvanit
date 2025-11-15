import re
import csv
from datetime import datetime
from models import Book, get_connection


# ------------------ REGEX SEARCH ------------------ #

def search_books(pattern, field="title"):
    regex = re.compile(pattern, re.IGNORECASE)
    books = Book.get_all() if hasattr(Book, "get_all") else []

    results = []
    for b in books:
        value = getattr(b, field)
        if regex.search(value):
            results.append(b)
    return results


def generate_invoice(member_name, book_title, fine):
    filename = f"invoice_{member_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("---- LibraDesk Invoice ----\n")
        f.write(f"Member: {member_name}\n")
        f.write(f"Book: {book_title}\n")
        f.write(f"Fine: {fine}\n")

    return filename

def overdue_report():
    conn = get_connection()
    cur = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cur.execute("""
    SELECT m.name, b.title, br.due_date
    FROM borrowings br
    JOIN members m ON br.member_id=m.id
    JOIN books b ON br.book_id=b.id
    WHERE return_date IS NULL AND due_date < ?
    """, (today,))

    rows = cur.fetchall()
    conn.close()
    return rows

def most_borrowed_books():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT b.title, COUNT(*) as times
    FROM borrowings br
    JOIN books b ON br.book_id=b.id
    GROUP BY br.book_id
    ORDER BY times DESC
    LIMIT 5
    """)

    rows = cur.fetchall()
    conn.close()
    return rows