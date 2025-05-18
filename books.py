# books.py

book_list = {
    "001": {"title": "Laskar Pelangi", "available": True},
    "002": {"title": "Bumi Manusia", "available": True},
    "003": {"title": "Atomic Habits", "available": True}
}

def display_books():
    print("\n=== Daftar Buku ===")
    for code, info in book_list.items():
        status = "Tersedia" if info["available"] else "Dipinjam"
        print(f"{code} - {info['title']} ({status})")