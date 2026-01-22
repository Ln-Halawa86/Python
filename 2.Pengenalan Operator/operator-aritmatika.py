#Berikut adalah daftar lengkap 7 operator aritmatika di Python.
#1. Penjumlahan (+)
a = 10
b = 5
print(a + b)  # Output: 15

#2. Pengurangan (-)
print(a - b)  # Output: 5

#3. Perkalian (*)
print(a * b)  # Output: 50

#4. Pembagian (/)
print(a / b)  # Output: 2.0

#5. Modulus (%)
# Mengembalikan sisa pembagian, maksudnya hasil dari a % b adalah sisa dari pembagian a dengan b.
print(a % b)  # Output: 0

#6. Eksponen (**)
# Menghitung pangkat, maksudnya hasil dari a ** b adalah a dipangkatkan dengan b.
# Divariabel a adalah 10, dan b adalah 5, maka 10 dipangkatkan dengan 5 = 10x10x10x10x10 = 100000.
print(a ** b)  # Output: 100000

#7. Floor Division (//)
# Membagi dan membulatkan ke bawah ke bilangan bulat terdekat.
c = 15
d = 4
print(c // d)  # Output: 3
# Karena 15 dibagi 4 adalah 3.75, dan dibulatkan ke bawah menjadi 3.

#===================================================================
#catatan tambahan
x = 10
y = 4

# 1. Pembagian Biasa (selalu float)
hasil_bagi = x / y   
print(hasil_bagi)    # Output: 2.5 (Tipe data: float)

# 2. Floor Division (dibulatkan ke bawah)
hasil_floor = x // y 
print(hasil_floor)   # Output: 2 (Tipe data: int)

# 3. Pangkat
# Hati-hati: ^ di Python adalah XOR (bitwise), bukan pangkat.
print(2 ** 3)        # Output: 8 
print(2 ^ 3)         # Output: 1 (Karena ini operasi biner 10 XOR 11)


