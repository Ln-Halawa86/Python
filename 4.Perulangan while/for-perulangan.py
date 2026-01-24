# perulangan for adalah perulangan yang digunakan untuk mengulangi blok kode tertentu
# untuk sejumlah iterasi yang telah ditentukan sebelumnya. Perulangan for sering digunakan ketika
# kita tahu berapa kali kita ingin mengulangi suatu tindakan.

# ===================================================================================================
#1. Contoh penggunaan perulangan for:
for i in range(5):  # range(5) menghasilkan angka dari 0 hingga 4
    # i adalah variabel yang akan mengambil nilai dari setiap iterasi
    # in adalah kata kunci yang digunakan untuk mengindikasikan bahwa kita akan mengiterasi
    print("Iterasi ke-", i) 
# Output:
# Iterasi ke- 0
# Iterasi ke- 1
# Iterasi ke- 2
# Iterasi ke- 3
# Iterasi ke- 4
# Penjelasan:
# Pada contoh di atas, perulangan for akan mengulangi blok kode di dalamnya sebanyak 5 kali,
# dimulai dari 0 hingga 4. Variabel i akan mengambil nilai dari setiap iterasi.

# Kita dapat menggunakan perulangan for untuk mengiterasi elemen-elemen dalam sebuah list:
buah = ["apel", "pisang", "jeruk"]
for item in buah:
    #cara baca kode program di atas adalah:
    #pyhon ambil isi dari variabel buah satu per satu, lalu masukkan ke variabel item
    # lalu jalankan blok kode di dalamnya
    # kemudian ulangi lagi sampai semua isi dari variabel buah habis diambil
    print("Buah:", item)

# Output:
# Buah: apel
# Buah: pisang
# Buah: jeruk   
# ===================================================================================================

# ===================================================================================================
#2. Looping for pada string:
kata = "Python"
for huruf in kata:
    print("Huruf:", huruf)
# Output:
# Huruf: P
# Huruf: y
# Huruf: t
# Huruf: h
# Huruf: o
# Huruf: n
# Penjelasan:
# Pada contoh di atas, perulangan for digunakan untuk mengiterasi setiap huruf dalam string "Python".
# Variabel huruf akan mengambil setiap karakter dari string tersebut satu per satu.
# ===================================================================================================

# ===================================================================================================
#3. looping for break dan continue
#a. Break digunakan untuk menghentikan perulangan sebelum selesai
for angka in range(10):
    if angka == 5:
        break  # Hentikan perulangan jika angka sama dengan 5
    print("Angka:", angka)
# Output:
# Angka: 0
# Angka: 1
# Angka: 2
# Angka: 3
# Angka: 4

#b. Continue digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya
for angka in range(10):
    if angka % 2 == 0:
        continue  # Lewati angka genap
    print("Angka ganjil:", angka)
# Output:
# Angka ganjil: 1   
# Angka ganjil: 3
# Angka ganjil: 5
# Angka ganjil: 7
# Angka ganjil: 9


#c. gabungan continue dan break
for angka in range(10):
    if angka == 7:
        break  # Hentikan perulangan jika angka sama dengan 7
    if angka % 2 == 0:
        continue  # Lewati angka genap
    print("Angka ganjil sebelum 7:", angka)
# Output:
# Angka ganjil sebelum 7: 1
# Angka ganjil sebelum 7: 3
# Angka ganjil sebelum 7: 5
# ===================================================================================================

# ===================================================================================================
#4.looping for menggunakan enumerate
# Fungsi enumerate() digunakan untuk mendapatkan indeks dan nilai dari elemen dalam sebuah iterable (seperti list atau string) secara bersamaan selama perulangan.
buah = ["apel", "pisang", "jeruk"]
for index, item in enumerate(buah):
    #baca kode di atas adalah:
    # python ambil isi dari variabel buah satu per satu, lalu masukkan ke variabel item
    # lalu ambil juga indeks dari setiap item tersebut, masukkan ke variabel index
    # lalu jalankan blok kode di dalamnya
    # kemudian ulangi lagi sampai semua isi dari variabel buah habis diambil
    print("Indeks:", index, "Buah:", item)
# Output:
# Indeks: 0 Buah: apel 
# Indeks: 1 Buah: pisang
# Indeks: 2 Buah: jeruk
# ===================================================================================================

#5.looping for dengan fungsi range() yang memiliki dua dan tiga argumen.
# Fungsi range() dapat menerima dua atau tiga argumen untuk menentukan rentang angka yang akan dihasilkan.
# a. range(start, stop): Menghasilkan angka dari start hingga stop-1
for angka in range(5, 10):  # Menghasilkan angka dari 5 hingga 9
    print("Angka:", angka)
# Output:
# Angka: 5
# Angka: 6
# Angka: 7
# Angka: 8
# Angka: 9

# b. range(start, stop, step): Menghasilkan angka dari start hingga stop-1 dengan langkah step
for angka in range(0, 20, 5):  # Menghasilkan angka dari 0 hingga 19 dengan langkah 5
    print("Angka:", angka)
# Output:
# Angka: 0
# Angka: 5
# Angka: 10
# Angka: 15
# ===================================================================================================



#soal latihan:

# 1. Buatlah program menggunakan perulangan for yang mencetak bilangan ganjil dari 1 hingga 19!
# output yang diharapkan:
# bilangan ganjil : 1 
# bilangan ganjil : 3
# bilangan ganjil : 5
# bilangan ganjil : 7
# bilangan ganjil : 9
# bilangan ganjil : 11
# bilangan ganjil : 13
# bilangan ganjil : 15
# bilangan ganjil : 17
# bilangan ganjil : 19
# Jawaban:
for angka_gajil in range(20):
    if angka_gajil % 2 == 0:
         continue
    print("bilangan ganjil",angka_gajil)

#jawaban diatas apakah benar?
# ya, jawaban di atas benar. Program tersebut menggunakan perulangan for untuk mengiterasi angka dari 0 hingga 19.
# Di dalam perulangan, ada kondisi yang memeriksa apakah angka tersebut genap (angka_gajil % 2 == 0).
# Jika angka tersebut genap, pernyataan continue akan dilewati, sehingga hanya angka ganjil yang dicetak.


#2. Buatlah program menggunakan perulangan for yang mencetak elemen dari list berikut beserta indeksnya!
# daftar_buah = ["mangga", "semangka", "nanas", "kiwi", "anggur"]
# output yang diharapkan:
# Indeks: 0 Buah: mangga
# Indeks: 1 Buah: semangka
# Indeks: 2 Buah: nanas
# Indeks: 3 Buah: kiwi
# Indeks: 4 Buah: anggur
# Jawaban:
daftar_buah = ["mangga", "semangka", "nanas", "kiwi", "anggur"]
for index, fruit in enumerate(buah):
    print(f"index : {index} buah: {fruit}")





