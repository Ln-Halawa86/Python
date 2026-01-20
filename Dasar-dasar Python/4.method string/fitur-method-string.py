#1. Mengubah Huruf (Kapitalisasi)
#.upper(): Mengubah semua menjadi huruf besar.
#.lower(): Mengubah semua menjadi huruf kecil.
#.capitalize(): Huruf pertama saja yang besar.
#.title(): Huruf besar di setiap awal kata.
#contoh :
teks = "belajar python iTU meNyenaNgkan"

print(teks.upper())      # "BELAJAR PYTHON ITU MENYENANGKAN"
print(teks.lower())      # "belajar python itu menyenangkan"
print(teks.capitalize()) # "Belajar python itu menyenangkan"
print(teks.title())      # "Belajar Python Itu Menyenangkan"

#2.Membersihkan Spasi (strip)
#Method ini wajib dipakai saat memproses input pengguna untuk menghapus spasi kosong yang tidak sengaja terketik di awal atau akhir kalimat.
#.strip(): Hapus spasi di kiri DAN kanan.
#.lstrip(): Hapus spasi kiri (Left) saja.
#.rstrip(): Hapus spasi kanan (Right) saja.
username = "  admin_budi  "
print(f"'{username.strip()}'")  # Output: 'admin_budi'


#3. Memecah dan Menggabungkan (split & join)
#Ini adalah teknik dasar untuk pengolahan data teks (seperti memisahkan kalimat menjadi kata-kata).
#.split(): Memotong string berdasarkan pemisah tertentu dan mengubahnya menjadi List. (Default pemisahnya adalah spasi).
#.join(): Kebalikannya, menggabungkan List menjadi satu string utuh.
kalimat = "Saya sedang belajar Python"

# Memecah string menjadi list
kata_kata = kalimat.split()
print(kata_kata) 
# Output: ['Saya', 'sedang', 'belajar', 'Python']

# Menggabungkan kembali dengan tanda hubung
gabung = "-".join(kata_kata)
print(gabung)
# Output: Saya-sedang-belajar-Python

#4. Mencari dan Mengganti (find & replace)
#.replace(lama, baru): Mengganti teks tertentu dengan teks lain.
#.find(teks): Mencari posisi indeks pertama ditemukannya teks. Jika tidak ada, hasilnya -1.
#.count(teks): Menghitung berapa kali sebuah kata muncul.
pesan = "Halo Bro, apa kabar Bro?"

# Mengganti kata
pesan_baru = pesan.replace("Bro", "Budi")
print(pesan_baru)  # Output: Halo Budi, apa kabar Budi?

# Mencari posisi kata
print("index ke-",pesan.find("apa"))  # Output: 10 (indeks ke-10)

# Menghitung jumlah kata
print("jumlah kata bro :", pesan.count("Bro")) # Output: 2


#5.Pengecekan Isi (Boolean)
#Method ini mengembalikan True atau False. Sering dipakai untuk validasi.
#.isdigit(): Apakah isinya angka semua?
#.isalpha(): Apakah isinya huruf semua?
#.startswith("..."): Apakah diawali kata tertentu?
#.endswith("..."): Apakah diakhiri kata tertentu?
#contoh :
kode = "12345"
file = "laporan.pdf"

print(kode.isdigit())      # True
print(file.endswith("pdf")) # True

#6. Split Default (Tanpa Parameter)
#Jika kurung dibiarkan kosong (), Python akan memotong teks berdasarkan Whitespace (spasi, tab, atau enter).
#Kehebatan mode default ini adalah ia mengabaikan spasi berlebih. Jika ada 5 spasi di antara kata, itu tetap dianggap satu pemisah.
# Contoh: Kalimat dengan spasi yang berantakan
teks = "Belajar    Python   itu   seru"

hasil = teks.split()

print(hasil)
# Output bersih: ['Belajar', 'Python', 'itu', 'seru']


#7 Split dengan Karakter Tertentu (Delimiter)
#Anda bisa menentukan karakter apa yang dijadikan "gunting" untuk memotong string. Ini sering dipakai saat mengolah data CSV atau log.
#Perhatian: Berbeda dengan default, mode ini tidak mengabaikan pemisah kosong.
#contoh :
# Data CSV (Comma Separated Values)
data_user = "Budi,24,Jakarta,Programmer"

# Potong berdasarkan koma
profil = data_user.split(",")

print(profil)
# Output: ['Budi', '24', 'Jakarta', 'Programmer']

#8 Membatasi Jumlah Potongan (maxsplit)
#Terkadang kita hanya ingin memisahkan kata pertama saja, dan membiarkan sisanya utuh. Kita bisa menambahkan angka parameter kedua.
# Rumusnya: .split(pemisah, maxsplit)
# contoh
email = "admin@google.com"

# Kita ingin memisahkan username dan domain saja
# 1 berarti: Lakukan pemotongan sebanyak 1 kali saja
user_data = email.split("@", 1)

print(user_data)
# Output: ['admin', 'google.com']

# 9. Studi Kasus Mini: Persiapan Data NLP (Pre-processing)
# Karena Anda tertarik pada Sentiment Analysis, berikut contoh sederhana bagaimana .split() digunakan untuk membersihkan data kasar sebelum masuk ke algoritma.
#contoh :
tweet = "  Promo hari ini SANGAT murah!!! #diskon  "

# Langkah 1: Kecilkan huruf (Lowercase)
bersih = tweet.lower()

# Langkah 2: Hapus simbol (replace sederhana)
bersih = bersih.replace("!", "").replace("#", "")

# Langkah 3: Tokenisasi (Split)
token = bersih.split()

print("======================================================")
print("Studi Kasus Mini: Persiapan Data NLP (Pre-processing)")
print(token)
# Output: ['promo', 'hari', 'ini', 'sangat', 'murah', 'diskon']
# (Sekarang data ini siap dihitung frekuensi katanya / TF-IDF)

#10. Kebalikannya: .rsplit()
#Sama persis dengan split, tapi memotong dari kanan. Ini sangat berguna untuk mengambil ekstensi file.

file = "laporan.keuangan.final.pdf"

# Potong dari kanan, 1 kali saja, berdasarkan titik
data = file.rsplit(".", 1)

print(data)
# Output: ['laporan.keuangan.final', 'pdf']
# (Kita berhasil memisahkan nama file dan ekstensinya)


#Langkah Selanjutnya yang Bisa Saya Lakukan: Hasil dari .split() selalu berupa List. Agar bisa mengolah data hasil split tersebut dengan lancar, apakah Anda ingin mempelajari cara List Indexing & Slicing (mengambil data urutan tertentu, misal: mengambil 3 data pertama saja)?

study = "Langkah Selanjutnya yang Bisa Saya Lakukan: Hasil dari .split() selalu berupa List. Agar bisa mengolah data hasil split tersebut dengan lancar, apakah Anda ingin mempelajari cara List Indexing & Slicing (mengambil data urutan tertentu, misal: mengambil 3 data pertama saja)?"

print (study.lower())
