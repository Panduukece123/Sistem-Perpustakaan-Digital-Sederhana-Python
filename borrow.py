# borrow.py

from books import book_list

def borrow_book(code):
    if code in book_list and book_list[code]["Buku tersedia"]:
        book_list[code]["Buku tersedia"] = False
        print(f"Buku '{book_list[code]['title']}' berhasil dipinjam.")
        return book_list[code]['title']
    elif code in book_list:
        print("Buku sedang dipinjam.")
    else:
        print("Kode buku tidak ditemukan.")