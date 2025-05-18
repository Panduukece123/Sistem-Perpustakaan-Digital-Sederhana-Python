# main.py

from books import display_books
from borrow import borrow_book
from returnbook import return_book, view_history

def main():
    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Lihat Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Lihat Riwayat Pengembalian")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            display_books()
        elif choice == "2":
            code = input("Masukkan kode buku: ")
            borrow_book(code)
        elif choice == "3":
            code = input("Masukkan kode buku: ")
            return_book(code)
        elif choice == "4":
            view_history()
        elif choice == "0":
            print("👋 Terima kasih telah menggunakan sistem perpustakaan!")
            break
        else:
            print("❗ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
