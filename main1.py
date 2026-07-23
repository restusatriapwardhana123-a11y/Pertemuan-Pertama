# ===========================================
# Program: Sistem Parkir Otomatis
# Konsep: Class, Object, Attribute, Method
# ===========================================

import datetime

class Kendaraan:
    def __init__(self, plat, jenis):
        self.plat = plat
        self.jenis = jenis
        self.waktu_masuk = datetime.datetime.now()
        self.waktu_keluar = None

    def keluar(self):
        self.waktu_keluar = datetime.datetime.now()

    def hitung_biaya(self):
        if self.waktu_keluar is None:
            print(f"Kendaraan {self.plat} belum keluar parkir.")
            return
        durasi = (self.waktu_keluar - self.waktu_masuk).seconds // 3600 + 1
        if self.jenis.lower() == "mobil":
            tarif = 5000
        else:
            tarif = 3000
        total = durasi * tarif
        print(f"Plat: {self.plat} | Jenis: {self.jenis} | Durasi: {durasi} jam | Biaya: Rp{total}")


# Membuat object kendaraan
kendaraan1 = Kendaraan("B 1234 XYZ", "Mobil")
kendaraan2 = Kendaraan("D 4567 ABC", "Motor")

print("=== Daftar Kendaraan Masuk Parkir ===")
print(f"{kendaraan1.plat} ({kendaraan1.jenis})")
print(f"{kendaraan2.plat} ({kendaraan2.jenis})")

# Simulasi kendaraan keluar
print("\n=== Kendaraan Keluar Parkir ===")
kendaraan1.keluar()
kendaraan1.hitung_biaya()

kendaraan2.keluar()
kendaraan2.hitung_biaya()