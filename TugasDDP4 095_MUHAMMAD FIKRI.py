buku = {
    "judul": "cara push imo 1menit",
    "penulis": "Jesnolimit",
    "tahun": 2020
}

def tampilkan_menu():
    print("--------------------------------")
    print("    pengelolaan data buku")
    print("------------------------------")
    print("1. daftar data buku")
    print("2. tambah buku")
    print("3. ubah data buku")
    print("4. hapus data buku")
    print("5. keluar")
    print("--------------------------------")

def tampilkan_data():
    print(" DATA BUKU ")
    if len(buku) == 0:
        print("data buku masih kosong.")
    else:
        for key, value in buku.items():
            nama = key.replace("_", " ").title()
            print(nama.ljust(15) + ": " + str(value))

while True:
    tampilkan_menu()
    pilihan = input("pilih (1-5): ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        key_baru = input("memasukkan nama data yg ingin ditambah (contoh: penerbit): ").lower()
        if key_baru == "":
            print("nama data tidak boleh kosong.")
        elif key_baru in buku:
            print(f"Data '{key_baru}' sudah ada. Gunakan menu ubah data.")
        else:
            nilai_baru = input(f"tambahkan teks untuk {key_baru}: ").strip()
            if nilai_baru == "":
                print("nilai data tidak boleh kosong.")
            else:
                buku[key_baru] = nilai_baru
                print(f"data '{key_baru}' berhasil ditambahkan. ")
                tampilkan_data()

    elif pilihan == "3":
        key_ubah = input("Masukkan nama data yang ingin diubah (contoh: penulis): ").lower()
        if key_ubah in buku:
            nilai_ubah = input(f"Masukkan teks baru untuk {key_ubah}: ")
            buku[key_ubah] = nilai_ubah
            print(f"Data '{key_ubah}' berhasil diubah.")
            tampilkan_data()
        else:
            print(f"Data '{key_ubah}' tidak ditemukan.")

    elif pilihan == "4":
        key_hapus = input("masukkan nama data yg ingin diubah (penulis): ").lower()
        if key_hapus in buku:
            del buku[key_hapus]
            print("data '{key_hapus}' berhasil dihapus.")
            tampilkan_data()
        else:
            print("data '{key_hapus}' tidak ditemukan.")

    elif pilihan == "5":
        print("terimakasih sudah menggunakan program saya.")
        break

    else:
        print("pilihan tidak valid, coba lagi angka 1 sampai 5.")