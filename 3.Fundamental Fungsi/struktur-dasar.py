#Struktur Dasar Fungsi pada Python
#Fungsi adalah blok kode yang dirancang untuk melakukan tugas tertentu.
#Fungsi memungkinkan kita untuk mengelompokkan kode yang dapat digunakan kembali.

#Cara mendefinisikan fungsi di Python adalah dengan menggunakan kata kunci def diikuti dengan nama fungsi dan tanda kurung ().
#Jika fungsi menerima parameter, kita dapat menuliskannya di dalam tanda kurung tersebut.

#1.Contoh sederhana mendefinisikan dan memanggil fungsi tanpa parameter
def sapa():
    print("Halo, selamat datang di dunia Python!")
#Memanggil fungsi sapa
sapa()  # Output: Halo, selamat datang di dunia Python!

#2. Contoh mendefinisikan fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang di dunia Python!")
#Memanggil fungsi sapa_nama dengan argumen
sapa_nama("Andi")  # Output: Halo, Andi! Selamat datang di dunia Python!

#3. Contoh mendefinisikan fungsi dengan parameter dan mengembalikan nilai
def tambah(a, b):
    return a + b
#return digunakan untuk mengembalikan hasil dari fungsi ke pemanggilnya.
#kenapa harus dikembalikan?
#Karena dengan mengembalikan nilai, kita dapat menyimpan hasil fungsi ke dalam variabel atau menggunakannya dalam operasi lain.

#Memanggil fungsi tambah dan menyimpan hasilnya
hasil = tambah(10, 5)
print(hasil)  # Output: 15

#4. Contoh mendefinisikan fungsi dengan nilai default untuk parameter
def sapa_bahasa(nama, bahasa="Indonesia"):
    if bahasa == "Indonesia":
        print(f"Halo, {nama}! Selamat datang di dunia Python!")
    elif bahasa == "Inggris":
        print(f"Hello, {nama}! Welcome to the world of Python!")
    else:
        print(f"Halo, {nama}! Selamat datang di dunia Python!")
#Memanggil fungsi sapa_bahasa dengan dan tanpa argumen bahasa
sapa_bahasa("Budi")  # Output: Halo, Budi! Selamat datang di dunia Python!
sapa_bahasa("Alice", "Inggris")  # Output: Hello, Alice! Welcome to the world of Python!

#5. Contoh mendefinisikan fungsi dengan jumlah parameter yang tidak tetap
def cetak_buah(*buah):
    for item in buah:
        print(item)
#Memanggil fungsi cetak_buah dengan berbagai jumlah argumen
cetak_buah("Apel", "Pisang", "Mangga")
# Output:
# Apel  
# Pisang
# Mangga

#Itulah struktur dasar fungsi pada Python beserta beberapa contoh penggunaannya.
#Dengan memahami cara mendefinisikan dan menggunakan fungsi, kita dapat menulis kode yang lebih terstruktur dan mudah dipelihara.
#Fungsi juga membantu dalam menghindari pengulangan kode dan meningkatkan keterbacaan program.


#6.Berikut adalah contoh fungsi yang memanggil fungsi lain di dalamnya:
def hitung_luas_persegi(sisi):
    return sisi * sisi
def tampilkan_luas_persegi(sisi):
    luas = hitung_luas_persegi(sisi)
    print(f"Luas persegi dengan sisi {sisi} adalah {luas}")
#Memanggil fungsi tampilkan_luas_persegi
tampilkan_luas_persegi(4)  # Output: Luas persegi dengan sisi 4 adalah 16

