#.split() menghasilkan List, kita harus menggunakan teknik Indexing dan Slicing untuk mengambil \
# atau memotong data dari list tersebut sesuai kebutuhan.
#1. Indexing (Mengambil Satu Data)
#Di Python, urutan (index) selalu dimulai dari angka 0, bukan 1.
#- list[0]: Mengambil elemen pertama.
#- list[1]: Mengambil elemen kedua.
#- list[-1]: Mengambil elemen terakhir (sangat berguna jika panjang list tidak diketahui).

#2. Slicing (Mengambil Beberapa Data)
#Slicing digunakan untuk mengambil potongan data (sub-list). Rumus dasarnya: list[awal : akhir]
#awal: Index mulai (termasuk/ikut diambil).
#akhir: Batas index berhenti (TIDAK termasuk/tidak ikut diambil).
#Tips: Jika bagian awal dikosongkan, artinya "dari paling depan". Jika akhir dikosongkan, artinya 
# "sampai paling belakang".

#contoh kode
# Skenario: Data mentah dari input pengguna atau file CSV
raw_data = "Jakarta,Bandung,Surabaya,Yogyakarta,Semarang"

# 1. Gunakan split untuk mengubah string menjadi List
kota_list = raw_data.split(",")
print(f"List Lengkap: {kota_list}")
# Output: ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Semarang']

# --- INDEXING (Ambil satu per satu) ---
print(f"Data pertama (index 0): {kota_list[0]}")   # Jakarta
print(f"Data terakhir (index -1): {kota_list[-1]}") # Semarang

# --- SLICING (Ambil sebagian) ---

# Kasus Anda: Mengambil 3 data pertama
# Rumus: [0:3] -> Index 0, 1, dan 2 diambil. Index 3 berhenti.
tiga_pertama = kota_list[0:3]
# Cara lebih singkat (kosongkan awal): kota_list[:3]

print(f"3 Data Pertama: {tiga_pertama}")
# Output: ['Jakarta', 'Bandung', 'Surabaya']

# Contoh lain: Mengambil data dari index ke-2 sampai akhir
sisa_data = kota_list[2:]
print(f"Data index 2 ke atas: {sisa_data}")
# Output: ['Surabaya', 'Yogyakarta', 'Semarang']