# Function judul program
def my_function():
    print("===================================")
    print(" Program Pengecekan & Perhitungan ")
    print("===================================")

# Function cek ganjil/genap
def cek_ganjil_genap():
    while True:
        angka = input("\nMasukkan angka (ketik 'exit' untuk kembali): ")

        if angka.lower() == "exit":
            break

        if angka.lstrip("-").isdigit():
            angka = int(angka)

            if angka % 2 == 0:
                print("Ini adalah angka genap")
            else:
                print("Ini adalah angka ganjil")
        else:
            print("Input tidak valid!")

# Function luas persegi panjang
def luas_persegi_panjang():
    while True:
        panjang = input("\nMasukkan panjang (ketik 'exit' untuk kembali): ")

        if panjang.lower() == "exit":
            break

        lebar = input("Masukkan lebar: ")

        if lebar.lower() == "exit":
            break

        try:
            panjang = float(panjang)
            lebar = float(lebar)

            luas = panjang * lebar
            print("Luas persegi panjang =", luas)

        except ValueError:
            print("Input harus berupa angka!")

# Program utama
while True:
    my_function()

    print("\nMenu:")
    print("1. Cek Ganjil & Genap")
    print("2. Luas Persegi Panjang")
    print("3. Exit")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        cek_ganjil_genap()

    elif pilihan == "2":
        luas_persegi_panjang()

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")