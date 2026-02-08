# pengenalan sequence di python
# Sequence adalah tipe data yang dapat menyimpan beberapa nilai dalam satu variabel.
# Contoh tipe data sequence di Python adalah list, tuple, dan string.

# ======================================================================================================
#1
#list adalah tipe data sequence yang dapat diubah (mutable) dan dapat menyimpan berbagai tipe data.
#kegunaan : Untuk data yang dinamis, sering bertambah, berkurang, atau diedit.
#list menggunakan ini ya []
my_list = [1, 2, 3, 'empat', 'lima']
print("List:", my_list)
#output: List: [1, 2, 3, 'empat', 'lima']

# contoh lain list
users = ["Andi", "Budi", "Citra"]
users[0] = "Anton"  # Bisa diubah
users.append("Dedi") # Bisa ditambah
print(users) # Output: ['Anton', 'Budi', 'Citra', 'Dedi']
# ======================================================================================================


# ======================================================================================================
#2
#tuple adalah tipe data sequence yang tidak dapat diubah (immutable) dan dapat menyimpan berbagai tipe data.
#Kegunaan: Untuk data pasti/konstan yang tidak boleh diganggu gugat agar aman dan lebih hemat memori.
#tuple menggunakan ini ya ()
my_tuple = (1, 2, 3, 'empat', 'lima')
print("Tuple:", my_tuple)
#output: Tuple: (1, 2, 3, 'empat', 'lima')

# contoh lain tuple
coordinates = (10.0, 20.0)
# koordinat[0] = 50  <-- Akan ERROR jika dijalankan!
print(coordinates)  # Output: (10.0, 20.0)

#contoh soal latihan tuple
# Buat tuple dengan nama "buah" yang berisi beberapa nama buah
buah = ("apel", "jeruk", "mangga", "pisang")
print("Tuple buah:", buah)
#output: Tuple buah: ('apel', 'jeruk', 'mangga', 'pisang')
# ======================================================================================================



# ======================================================================================================
#3
#string adalah tipe data sequence yang tidak dapat diubah Immutable (Karakter di dalamnya tidak bisa diubah satu per satu).  dan hanya menyimpan karakter
my_string = "Hello, World!"
print("String:", my_string)
# pesan[0] = 'J'  <-- ERROR! String tidak bisa diubah per huruf.
#output: String: Hello, World!
# ======================================================================================================


