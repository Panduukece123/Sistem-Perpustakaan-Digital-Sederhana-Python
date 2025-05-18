# books.py

book_list = {
    "001": {"title": "Laskar Pelangi", "Buku tersedia": True},
    "002": {"title": "Bumi Manusia", "Buku tersedia": True},
    "003": {"title": "Atomic Habits", "Buku tersedia": True}
}

def display_books():
    print("\n=== Daftar Buku ===")
    for code, info in book_list.items():
        status = "Tersedia" if info["Buku tersedia"] else "Dipinjam"
        print(f"{code} - {info['title']} ({status})")
