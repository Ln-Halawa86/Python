#1. Sintaks Dasar
# Program menyapa user
nama = input("Siapa nama kamu? ")
print("Halo, " + nama + "! Senang bertemu denganmu.")

#2. "Jebakan" Tipe Data (Wajib Baca!)
# ↪ Python input() SELALU menganggap apapun yang kamu ketik sebagai STRING (Teks).
# ↪ Meskipun kamu mengetik angka 100, Python membacanya sebagai teks "100".
# Contoh:
umur = input("Berapa umur kamu? ")
# Niatnya mau menghitung umur
# INI AKAN ERROR!
# umur = 2026 - tahun_lahir
# Error: TypeError: unsupported operand type(s) for -: 'int' and 'str' (Artinya: Kamu mencoba mengurangi Angka dengan Teks. Tidak bisa!)

#3. Mengubah Tipe Data Input (casting)
# Jika kamu ingin menggunakan input sebagai angka, kamu harus mengubahnya.
# Contoh 
# Cara 1: Tampung dulu, baru ubah tipe datanya
tahun_lahir = input("Tahun berapa Kamu Lahir?")
tahun_int = int(tahun_lahir)
umur = 2026 - tahun_int
print(f"umur kamu sekarang adalah {umur} tahun.")

# Cara 2: Ubah langsung saat input
tahun_lahir = int(input("Tahun berapa Kamu Lahir?"))
umur = 2026 - tahun_lahir
print(f"umur kamu sekarang adalah {umur} tahun.")