daftar_buku = [
    [1, "Sisi tergelap surga", 85000],
    [2, "The Power of When", 75000],
    [3, "Atomic Habits", 95000]
]

keranjang = []
def display_menu():
    print("==============================================")
    print("== Selamat Datang di Toko Buku Namiya ==")
    print("==============================================")
    print("Pilih aktivitas:") 
    print("1. Lihat daftar buku")
    print("2. Tambah buku ke keranjang")
    print("3. Lihat keranjang")
    print("4. Checkout")
    print("5. Cari buku")
    print("6. Keluar")

def lihat_buku():
    print("\nDAFTAR BUKU")

    for buku in daftar_buku:
        print(
            "ID :", buku[0],
            "| Judul :", buku[1],
            "| Harga : Rp", buku[2]
        )


# ================================
# CARI BUKU
# ================================
def cari_buku():

    keyword = input("\nMasukkan judul buku : ")

    ditemukan = False

    for buku in daftar_buku:

        if keyword.lower() in buku[1].lower():

            print(
                "ID :", buku[0],
                "| Judul :", buku[1],
                "| Harga : Rp", buku[2]
            )

            ditemukan = True

    if ditemukan == False:
        print("Buku tidak ditemukan")


def tambah_keranjang():

    lihat_buku()

    id_buku = int(input("\nMasukkan ID buku : "))
    jumlah = int(input("Masukkan jumlah : "))

    for buku in daftar_buku:

        if buku[0] == id_buku:

            keranjang.append([buku, jumlah])

            print("Buku berhasil ditambahkan")
            return

    print("ID buku tidak ada")



def lihat_keranjang():

    print("\nKERANJANG")

    total = 0

    if len(keranjang) == 0:
        print("Keranjang kosong")
        return

    for item in keranjang:

        buku = item[0]
        jumlah = item[1]

        subtotal = buku[2] * jumlah

        print(
            buku[1],
            "|", jumlah, "pcs",
            "| Rp", subtotal
        )

        total = total + subtotal

    print("\nTotal Belanja : Rp", total)


def checkout():

    total = 0

    for item in keranjang:

        buku = item[0]
        jumlah = item[1]

        total = total + (buku[2] * jumlah)

    print("\nTotal Bayar : Rp", total)

    uang = int(input("Masukkan uang : Rp "))

    if uang < total:
        print("Uang tidak cukup")

    else:
        kembalian = uang - total
        print("Kembalian : Rp", kembalian)
        print("Pembayaran berhasil")

        keranjang.clear()

while True:
    display_menu()

    pilih = input("Pilih menu : ")

    if pilih == "1":
        lihat_buku()
    elif pilih == "2":
        tambah_keranjang()
    elif pilih == "3":
        lihat_keranjang()
    elif pilih == "4":
        checkout()
    elif pilih == "5":
        cari_buku()
    elif pilih == "6":
        print("Program selesai")
        break
    else:
        print("Menu tidak tersedia")
