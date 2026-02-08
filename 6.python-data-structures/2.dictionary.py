#Dictionary adalah struktur data yang menyimpan data dalam format pasangan Key dan Value (Key: Value).
#Berbeda dengan List yang menggunakan indeks angka (0, 1, 2) untuk mengambil data, Dictionary menggunakan Key (kata kunci) yang unik.

#kegunaan utama Dictionary adalah untuk memberikan label pada data agar mudah dimengerti dan mempercepat pencarian data.
#Bayangkan kalau kamu punya buku kontak di HP. Kamu cari nomor temanmu berdasarkan Nama (Key), bukan berdasarkan "urutan ke-10 di daftar" (Index). Itulah Dictionary.

#Dictionary Digunakan di Mana Saja?
# Dalam dunia pemrograman profesional, Dictionary sangat sering ditemukan pada:
#- Pengembangan Web (API): Format data JSON yang digunakan untuk mengirim data antara Website dan Server bentuknya sangat mirip dengan Dictionary Python.
#- Database: Digunakan untuk merepresentasikan satu baris data dalam tabel (misal: data profil pengguna).
#- Konfigurasi Aplikasi: Menyimpan pengaturan aplikasi seperti nama database, password, atau tema warna.
#- Data Science: Digunakan untuk mengolah data mentah sebelum dimasukkan ke dalam tabel (seperti Pandas DataFrame).

#1. Karakteristik Utama:
#Unordered: Data tidak disimpan berdasarkan urutan (meski di Python versi terbaru urutan insert dipertahankan, secara konsep kita tidak mengaksesnya via urutan).
#Mutable: Isinya bisa diubah-ubah.
#Unique Keys: Satu kunci hanya boleh muncul sekali.

#=============================================================================================================
#=============================================================================================================
#Sintaks: Menggunakan kurung kurawal {}.
# Contoh Dictionary data mahasiswa
mahasiswa = {
    "nama": "Leo",
    "jurusan": "Informatika",
    "ipk": 3.72,
    "skills": ["Python", "PHP", "React"] # Value bisa berupa List
}

# Contoh Penggunaan Sederhana
# 1. Membuat Dictionary
mobil = {
    "merek": "Toyota",
    "model": "Corolla",
    "tahun": 2022
}

# 2. Mengambil data (Memanggil Key "merek")
print(mobil["merek"])  # Output: Toyota

# 3. Menambah data baru
mobil["warna"] = "Hitam"

# 4. Mengubah data yang sudah ada
mobil["tahun"] = 2024

print(mobil)
# Output: {'merek': 'Toyota', 'model': 'Corolla', 'tahun': 2024, 'warna': 'Hitam'}
#====================================================================================================================
#====================================================================================================================

# ==================================================================================================
#2.Fungsi-Fungsi Penting Dictionary
#A. Mengakses Data (.get)
#   Kamu bisa akses pakai kurung siku [], tapi method .get() lebih aman karena tidak akan error jika kuncinya tidak ada.
print(mahasiswa["nama"])        # Output: Leo
print(mahasiswa.get("alamat"))  # Output: None (Tidak Error)
# print(mahasiswa["alamat"])    # INI AKAN ERROR (KeyError)

#B.Menambah & Mengupdate Data
#Caranya sama persis, tinggal panggil key-nya.
mahasiswa["kampus"] = "Budi Luhur"  # Menambah data baru
mahasiswa["ipk"] = 3.80             # Mengupdate data lama
# 
#C. Mengambil Kunci atau Nilai Saja
#   (Sangat berguna saat looping.)
#.keys(): Ambil semua kuncinya.
#.values(): Ambil semua nilainya.
#.items(): Ambil keduanya (key & value).

#D. Menghapus Data (pop)
mahasiswa.pop("jurusan") # Menghapus key 'jurusan' dan valuenya
# ==================================================================================================

# ==================================================================================================
#3 fungsi dan metode bawaan yang sangat sering digunakan untuk memanipulasi Dictionary.
"a.  Mengakses Data dengan Aman (get)"
#Menggunakan get() lebih aman daripada memanggil langsung dengan [key], karena jika datanya tidak ada, program tidak akan error (crash).
#contoh
user = {"nama": "Andi", "level": "Admin"}

# Jika key ada
print(user.get("nama")) # Output: Andi

# Jika key TIDAK ada, bisa memberikan nilai default
print(user.get("email", "Email tidak ditemukan")) # Output: Email tidak ditemukan


"b.Mengambil Semua Key, Value, atau Pasangannya"
#Ini sangat berguna saat kita ingin melakukan perulangan (looping).
#contoh
user = {"nama": "Andi", "level": "Admin"}

# Mengambil semua key
print(user.keys()) # Output: dict_keys(['nama', 'level'])

# Mengambil semua value
print(user.values()) # Output: dict_values(['Andi', 'Admin'])

# Mengambil semua pasangan key-value
print(user.items()) # Output: dict_items([('nama', 'Andi'), ('level', 'Admin')])


"c. Menghapus Data"
#contoh
user = {"nama": "Andi", "level": "Admin"}

# Menghapus key "level"
user.pop("level")
print(user) # Output: {'nama': 'Andi'}

# Menghapus semua data
user.clear()
print(user) # Output: {}

"d.Menggabungkan atau Update Data (update)"

#contoh
user = {"nama": "Andi"}
user.update({"level": "Admin"})
print(user) # Output: {'nama': 'Andi', 'level': 'Admin'}

#contoh 1
data_awal = {"id": 1, "status": "Pending"}
data_baru = {"status": "Success", "waktu": "12:00"}
# Timpa data lama dengan data baru
data_awal.update(data_baru)
print(data_awal) 
# Output: {'id': 1, 'status': 'Success', 'waktu': '12:00'}

# ==================================================================================================



