#Operator Penugasan (Assignment)
#Operator penugasan digunakan untuk memberikan nilai kepada variabel.
#Operator penugasan yang paling umum adalah tanda sama dengan (=).

x = 10  # Variabel x diberi nilai 10

#1. Penugasan Sederhana (=)
print(x)  # Output: 10
#kenapa bisa seperti itu?
#Karena tanda sama dengan (=) di Python digunakan untuk menetapkan nilai ke variabel.

#2. Penugasan dengan Penambahan (+=)
x += 5  # Sama dengan x = x + 5
print(x)  # Output: 15
#kenapa bisa seperti itu?
#Karena operator += menambahkan nilai di sebelah kanan ke variabel di sebelah kiri dan menyimpan 
#hasilnya kembali ke variabel tersebut.
#pejelasan kenapa outputnya 15 adalah karena awalnya x bernilai 10,
#lalu ditambahkan 5 (10 + 5), sehingga hasil akhirnya adalah 15

#3. Penugasan dengan Pengurangan (-=)
x -= 3  # Sama dengan x = x - 3
print(x)  # Output: 12

#4. Penugasan dengan Perkalian (*=)
x *= 2  # Sama dengan x = x * 2
print(x)  # Output: 24

#5. Penugasan dengan Pembagian (/=)
x /= 4  # Sama dengan x = x / 4
print(x)  # Output: 6.0

#6. Penugasan dengan Modulus (%=)
x %= 4  # Sama dengan x = x % 4
print(x)  # Output: 2.0
#ini karena 6.0 dibagi 4 sisanya adalah 2.0