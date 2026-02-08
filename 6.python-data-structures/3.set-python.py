# set adalah tipe data koleksi yang tidak memiliki nilai duplikat.
# secara analogi Set adalah koleksi data yang bersifat unordered (tidak berurutan) dan unindexed (tidak punya nomor indeks).
# Contoh tipe data set di Python adalah set, frozenset, dan dict.
# ==========================================================================================================

# contoh perbedaan list dan set
# Menggunakan LIST (Pakai kurung siku [ ])
tamu_list = ["Andi", "Budi", "Andi", "Citra"]
print(tamu_list)
# Hasil: ['Andi', 'Budi', 'Andi', 'Citra']
# (Andi muncul 2 kali, List menerimanya apa adanya)

print("---")

# Menggunakan SET (Pakai kurung kurawal { })
tamu_set = {"Andi", "Budi", "Andi", "Citra"}
print(tamu_set)
# Hasil: {'Citra', 'Andi', 'Budi'}
# (Perhatikan: Andi cuma sisa 1! Dan urutannya bisa jadi berantakan/acak)

# ==========================================================================================================
#Kenapa Kita Butuh Set? (Fungsinya)
#Mungkin kamu bertanya, "Kenapa saya mau pakai data yang acak dan membuang duplikat?"
#Berikut situasi di mana Set sangat berguna:
# Data: Kamu punya data 1.000 email pelanggan, tapi banyak yang dobel-dobel. Ubah saja ke Set, otomatis sisa yang unik saja.
#Cek Kehadiran Super Cepat: Set itu seperti penjaga pintu yang punya ingatan fotografis. Jika kamu tanya "Apakah 'Budi' ada di dalam?", Set bisa menjawab jauh lebih cepat daripada List, terutama jika datanya ada jutaan.

# ==========================================================================================================

#. Hal yang TIDAK BISA dilakukan Set
#Karena Set itu "Acak" (tidak punya nomor urut), kamu tidak bisa melakukan ini:
data = {"A", "B", "C"}

# INI AKAN ERROR:
print(data[0]) 
# Python akan bingung: "Yang mana data ke-0? Di sini tidak ada urutan!"
# INI AKAN ERROR (TypeError: 'set' object does not support item assignment)
# ==========================================================================================================

#contoh 1: Kasus "Membersihkan Data Ganda"
#Kita punya data yang ada duplikat, kita bisa membuang duplikat tersebut dengan cara:
# Data pendaftar yang berantakan (banyak duplikat)
pendaftar = ["Budi", "Siti", "Budi", "Joko", "Siti", "Andi", "Budi"]

print(f"Total data masuk: {len(pendaftar)} orang")
#ouput : Total data masuk: 7 orang

# --- KEAJAIBAN SET ---
# Ubah list menjadi set untuk menghapus duplikat otomatis
pendaftar_unik = set(pendaftar)

print(f"Total pendaftar asli: {len(pendaftar_unik)} orang")
print(f"Daftar nama: {pendaftar_unik}")

# Output:
# Total pendaftar asli: 4 orang
# Daftar nama: {'Joko', 'Andi', 'Budi', 'Siti'} 
# (Perhatikan: Urutan nama mungkin berubah karena set itu acak)


#Contoh 2: Kasus "Fitur Mutual Friends" (Teman yang Sama)
#Ini adalah logika yang dipakai Facebook atau Instagram. Kita punya dua orang user, dan kita ingin mencari siapa teman yang sama di antara mereka.
# Daftar teman User A dan User B
teman_andi = {"Bayu", "Citra", "Dewi", "Eko"}
teman_budi = {"Citra", "Fajar", "Dewi", "Gita"}

# 1. Mencari Mutual Friends (Irisan / Intersection)
# Simbol '&' artinya "cari yang ada di KEDUANYA"
mutual_friends = teman_andi & teman_budi

print(f"Teman Andi: {teman_andi}")
print(f"Teman Budi: {teman_budi}")
print("-" * 20)
print(f"Mutual Friends (Teman yang sama): {mutual_friends}")

# Output:
# Teman Andi: {'Citra', 'Dewi', 'Eko', 'Bayu'}
# Teman Budi: {'Dewi', 'Citra', 'Fajar', 'Gita'}
# ----------------------------------
# Mutual Friends (Teman yang sama): {'Citra', 'Dewi'}


# Contoh 3: Kasus "Gudang Barang" (Tambah & Hapus)
#Set bersifat Mutable, artinya isinya bisa diubah (ditambah atau dikurangi) selama program berjalan. Ini contoh pengelolaan stok barang sederhana.
# Stok awal di gudang
gudang = {"Laptop", "Mouse", "Keyboard"}

print(f"Gudang awal: {gudang}")
# output: Gudang awal: {'Laptop', 'Mouse', 'Keyboard'}

# 1. Barang baru masuk (Gunakan .add)
gudang.add("Monitor")
print("-> Menambah Monitor...")
# output: -> Menambah Monitor...

# 2. Barang terjual/keluar (Gunakan .remove)
gudang.remove("Mouse")
print("-> Mouse terjual...")
# output: -> Mouse terjual...

# 3. Coba tambah barang yang SUDAH ADA
gudang.add("Laptop") 
print("-> Mencoba menambah Laptop lagi...")
# output: -> Mencoba menambah Laptop lagi...
# Python tidak akan error, tapi tidak akan menambah laptop kedua.

print("-" * 20)
print(f"Stok gudang sekarang: {gudang}")

# Output final:
# Gudang awal: {'Laptop', 'Mouse', 'Keyboard'}
# -> Menambah Monitor...
# -> Mouse terjual...
# ----------------------------------
# Stok gudang sekarang: {'Laptop', 'Keyboard', 'Monitor'}


