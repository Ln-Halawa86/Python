#Studi Kasus 1: Membersihkan Data Log Server
#kenario: Anda bekerja sebagai backend developer. 
#Server memberikan satu baris data log yang berantakan dalam bentuk String. 
#Tugas Anda adalah mengekstrak Tanggal dan Pesan Error-nya saja.

# Data Input:
#log_server = "[ERROR]--2024-01-20--Connection_Refused--IP:192.168.1.1"

#Tugas:
# - Gunakan .split() untuk memecahkan string tersebut.
# - Ambil tanggal (2024-01-20) dan pesan error (Connection_Refused) menggunakan Indexing.
# - Tampilkan output yang bersih.
# - Target Output: Tanggal: 2024-01-20 | Error: Connection_Refused
# Jawab :
log_server = "[ERROR]--2024-01-20--Connection_Refused--IP:192.168.1.1"
log_list = log_server.split("--")
#ouput : ['[ERROR]', '2024-01-20', 'Connection_Refused', 'IP:192.168.1.1']

date = log_list[1]
error = log_list[2]

print(f"error : {error} | tanggal : {date}" )
#hasil : error : Connection_Refused | tanggal : 2024-01-20


#Studi Kasus 2: Analisa Data Penjualan (Nested List)
#Skenario: Anda memiliki data penjualan harian dari 3 cabang toko yang tersimpan dalam list bersarang (Nested List). Urutan data per 
#cabang: [Nama Cabang, [Omzet Pagi, Omzet Siang, Omzet Malam]].

#Data Input
#data_toko = [
#    ["Cabang A", [100, 200, 150]],
#    ["Cabang B", [50, 80, 70]],
#    ["Cabang C", [300, 400, 350]]
#]

# Tugas:
#1. Ambil Omzet Siang dari Cabang B (Nilai 80).
#2. Ambil semua data omzet (list angka) dari Cabang C (Nilai [300, 400, 350]).
#3. (Tantangan) Hitung total omzet Cabang A dengan menjumlahkan elemen dalam sub-listnya secara 
#manual (akses indeks 0 + indeks 1 + indeks 2).
# jawab :


#Studi Kasus 3: Dekripsi Pesan Rahasia (Advanced Slicing)
#Skenario: Seorang mata-mata mengirimkan pesan terenkripsi. 
# Pesan aslinya disembunyikan di dalam string sampah. Kuncinya adalah: Mulai dari huruf ke-2 (index 1), 
# ambil setiap huruf ke-4.
# Data Input:
# pesan_acak = "xPyltuhfozn !bseiBs a"

#Tugas:
#Gunakan teknik Slicing dengan Step ([start:stop:step]) untuk memecahkan kode tersebut.

#Jawab






