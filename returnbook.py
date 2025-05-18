# returnbook.py

from books import book_list

history = []

def return_book(code):
    if code in book_list and not book_list[code]["available"]:
        book_list[code]["available"] = True
        history.append(book_list[code]["title"])
        print(f"🔁 Buku '{book_list[code]['title']}' berhasil dikembalikan.")
    elif code in book_list:
        print("❌ Buku ini belum dipinjam.")
    else:
        print("❌ Kode buku tidak valid.")

def view_history():
    print("\n📚 Riwayat Pengembalian:")
    if not history:
        print("Belum ada buku yang dikembalikan.")
    for i, title in enumerate(history, 1):
        print(f"{i}. {title}")
