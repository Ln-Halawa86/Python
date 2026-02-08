#soal
#Diberikan sebuah variabel tabungan dengan nilai 1000000. Buatlah kode Python untuk:
#1.Menambahkan uang sebesar 500000 ke dalam tabungan
#2.Mengurangi uang sebesar 250000 dari tabungan
#3.Menampilkan jumlah uang yang tersisa di tabungan
#jawaban:
tabungan = 1000000
tabungan += 500000
tabungan -= 250000
print("Jumlah uang yang tersisa di tabungan:", tabungan)
#output: Jumlah uang yang tersisa di tabungan: 500000

#soal 2. menghitung tabungan menggunakan input
#Seseorang menabung di bank dengan jumlah tabungan awal tertentu. Bank memberikan bunga per tahun dalam bentuk persentase. Tabungan tersebut disimpan selama beberapa bulan.
#Buatlah program untuk menghitung jumlah tabungan akhir setelah disimpan dalam jangka waktu tertentu, dengan ketentuan:

# - Pengguna memasukkan jumlah tabungan awal.
# - Pengguna memasukkan bunga per tahun (dalam persen).
# - Pengguna memasukkan lama menabung dalam bulan.
# - Program menghitung total tabungan akhir menggunakan rumus bunga sederhana:
# - Jumlah tabungan akhir = tabungan awal + (bunga × tabungan awal × lama menabung) / 1200
# - Tampilkan hasil jumlah tabungan setelah disimpan selama beberapa bulan.
# Contoh kasus:
# * Tabungan awal: 1.000.000
# * Bunga per tahun: 6%
# *Lama menabung: 12 bulan
# *Hitung berapa total tabungan setelah 12 bulan.

#jawaban
tabungan_awal = int(input("Masukkan jumlah tabungan awal: "))
bunga_per_tahun = float(input("Masukkan bunga per tahun (dalam persen): "))
lama_menabung = int(input("Masukkan lama menabung dalam bulan: "))
total_tabungan = tabungan_awal + (bunga_per_tahun * tabungan_awal * lama_menabung) / 1200

print(f"Total tabungan setelah {lama_menabung} bulan adalah: {total_tabungan}")

