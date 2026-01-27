#soal1
#Diberikan sebuah list Python bernama data yang berisi elemen berikut:
#["A", "B", "C", "D", "E"]
#Buatlah kode Python untuk:
#1.Mengambil elemen dari indeks 1 sampai sebelum indeks 4
#2.Mengambil elemen terakhir dari list tersebut
#jawaban:
data = ["A", "B", "C", "D", "E"]
#1
subset = data[1:4]
print("Elemen dari indeks 1 sampai sebelum indeks 4:", subset)
#output: Elemen dari indeks 1 sampai sebelum indeks 4: ['B', 'C', 'D']
#2
last_element = data[-1]
print("Elemen terakhir dari list tersebut:", last_element)
#output: Elemen terakhir dari list tersebut: E


#soal 2
#Diberikan sebuah list Python bernama angka yang berisi bilangan bulat:
#[10, 20, 30, 40, 50]
#Buatlah program Python dengan cara Pythonic (list comprehension) untuk:
#Menghasilkan list baru yang berisi kuadrat dari setiap elemen pada list angka
#Menampilkan hasilnya ke layar
#jawaban:
angka = [10, 20, 30, 40, 50]
# Menggunakan list comprehension untuk menghasilkan list baru dengan kuadrat setiap elemen
kuadrat_angka = [x**2 for x in angka]
# Menampilkan hasilnya ke layar
print("Kuadrat dari setiap elemen pada list angka:", kuadrat_angka)
#output: Kuadrat dari setiap elemen pada list angka: [100, 400, 900, 1600, 2500]

#soal 3
#Diberikan data transaksi harian dalam bentuk list of tuples, di mana setiap tuple berisi:
# -Kode produk
# -Nama produk
# -Harga produk
#Data transaksi tersebut memiliki beberapa ketidakteraturan pada penulisan nama produk, seperti spasi berlebih 
# dan perbedaan huruf besar–kecil.

#Buatlah program Python untuk:

#1.Menyimpan data transaksi harian menggunakan tuple di dalam sebuah list
#2.Melakukan unpacking tuple untuk setiap item transaksi
#3.Membersihkan nama produk dengan cara:
#4.Menghapus spasi berlebih di awal atau akhir teks
#5.Mengubah penulisan nama produk menjadi Title Case
#6Menyimpan hasil data yang sudah dibersihkan ke dalam list baru
#7Menampilkan data produk yang telah dibersihkan dengan format:
#Kode Produk: <kode_produk>, Nama Produk: <nama_produk>, Harga: <harga_produk>
#jawaban:
#1
transaksi_harian = [
    ("P001", "  laptop asus  ", 7500000),
    ("P002", "smartphone samsung", 5000000),
    ("P003", "  HEADPHONE JBL ", 1500000),
    ("P004", "tablet apple ", 6000000),
]
#2 dan 3
data_bersih = []
for item in transaksi_harian:
    kode_produk, nama_produk, harga_produk = item
    #4 dan 5
    nama_produk_bersih = nama_produk.strip().title()
    #6
    data_bersih.append((kode_produk, nama_produk_bersih, harga_produk)) 
#7
for produk in data_bersih:
    kode_produk, nama_produk, harga_produk = produk
    print(f"Kode Produk: {kode_produk}, Nama Produk: {nama_produk}, Harga: {harga_produk}") 
#output:
#Kode Produk: P001, Nama Produk: Laptop Asus, Harga: 7500000
#Kode Produk: P002, Nama Produk: Smartphone Samsung, Harga: 5000000
#Kode Produk: P003, Nama Produk: Headphone Jbl, Harga: 1500000
#Kode Produk: P004, Nama Produk: Tablet Apple, Harga: 6000000   
