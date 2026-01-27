#Dictionary adalah struktur data yang menyimpan data dalam format pasangan Key dan Value (Key: Value).
#Berbeda dengan List yang menggunakan indeks angka (0, 1, 2) untuk mengambil data, Dictionary menggunakan Key (kata kunci) yang unik.

#kegunaan utama Dictionary adalah untuk memberikan label pada data agar mudah dimengerti dan mempercepat pencarian data.
#Bayangkan kalau kamu punya buku kontak di HP. Kamu cari nomor temanmu berdasarkan Nama (Key), bukan berdasarkan "urutan ke-10 di daftar" (Index). Itulah Dictionary.

#1. Karakteristik Utama:
#Unordered: Data tidak disimpan berdasarkan urutan (meski di Python versi terbaru urutan insert dipertahankan, secara konsep kita tidak mengaksesnya via urutan).
#Mutable: Isinya bisa diubah-ubah.
#Unique Keys: Satu kunci hanya boleh muncul sekali.

#Sintaks: Menggunakan kurung kurawal {}.
# Contoh Dictionary data mahasiswa
mahasiswa = {
    "nama": "Leo",
    "jurusan": "Informatika",
    "ipk": 3.72,
    "skills": ["Python", "PHP", "React"] # Value bisa berupa List
}


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


#C. Mengambil Kunci atau Nilai Saja
#   (Sangat berguna saat looping.)
#.keys(): Ambil semua kuncinya.
#.values(): Ambil semua nilainya.
#.items(): Ambil keduanya (key & value).

#D. Menghapus Data (pop)
mahasiswa.pop("jurusan") # Menghapus key 'jurusan' dan valuenya

