# 1. Menampilkan Banyak Data Sekaligus
# Dengan print(), kita bisa menampilkan banyak data sekaligus dengan memisahkannya menggunakan koma.
# Contoh:
nama = "Andi"
umur = 20
# Python otomatis mengubah angka menjadi teks dan memberi spasi
print("Nama:", nama, "| Umur:", umur)
# Output: Nama: Andi | Umur: 20

#2. Mengatur Pemisah
# Secara default, koma memberikan jarak satu spasi. Anda bisa mengubahnya menggunakan parameter sep (separator).
# contoh 
# Menggunakan pemisah strip (-)
print("0812", "3456", "7890", sep="-")
# Output: 0812-3456-7890

# Menggunakan pemisah baris baru (\n)
print("Baris 1", "Baris 2", "Baris 3", sep="\n")
# Output:
# Baris 1
# Baris 2
# Baris 3

#3. Mengatur Akhiran Baris (end)
# Secara normal, setelah melakukan print(), Python akan pindah ke baris baru (Enter). Anda bisa mencegah ini dengan parameter end.
# Tanpa pindah baris, diganti dengan spasi
print("Loading", end="...")
print("Selesai")
# Output: Loading...Selesai (dalam satu baris)

#4.Format String (f-string)
# ini adalah cara paling modern dan disukai programmer Python saat ini. Anda bisa menyisipkan variabel langsung ke dalam teks dengan menambahkan huruf f di depan tanda kutip.
barang = "Laptop"
harga = 5000000

# Cara lama (ribet dengan tanda +)
print("Harga " + barang + " adalah Rp " + str(harga))

# Cara f-string (lebih bersih)
print(f"Harga {barang} adalah Rp {harga}")

#5 Karakter Escape (Khusus)
#print() juga bisa membaca karakter khusus yang diawali dengan backslash (\).
# - \n: Membuat baris baru (Enter).
# - \t: Membuat jarak Tab.
# \' atau \": Menampilkan tanda kutip di dalam teks.
# contoh
print("Daftar Belanja:\n\t1. Susu\n\t2. Roti")
# Output:
# Daftar Belanja:
# 	1. Susu
# 	2. Roti

#6.Raw string
# fungsinya turn of "Escape Character"
# contoh
# String Biasa
# \n akan dianggap sebagai "Enter" (baris baru)
print("Halo\nDunia")
# Output:
# Halo
# Dunia

# Raw String
# \n akan dicetak sebagai tulisan "\n"
print(r"Halo\nDunia")
# Output: Halo\nDunia

