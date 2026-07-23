# Function judul program
def my_function():
    print("===================================")
    print(" Program Pengecekan & Perhitungan ")
    print("===================================")

# Function cek ganjil/genap
def cek_ganjil_genap():
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print("Ini adalah angka genap")
    else:
        print("Ini adalah angka ganjil")

# Function luas persegi panjang
def luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    luas = panjang * lebar
    print("Luas persegi panjang =", luas)

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

    input("\nTekan Enter untuk kembali ke menu...")
    print()