#Operator Perbandingan (Comparison)
#Operator perbandingan digunakan untuk membandingkan dua nilai.
#Hasil dari operasi ini adalah nilai boolean: True atau False.

a = 10
b = 5

#1. Sama dengan (==)
print(a == b)  # Output: False, karena 10 tidak sama dengan 5

#2. Tidak sama dengan (!=)
print(a != b)  # Output: True, karena 10 tidak sama dengan 5

#3. Lebih besar dari (>)
print(a > b)   # Output: True, karena 10 lebih besar dari 5

#4. Lebih kecil dari (<)
print(a < b)   # Output: False, karena 10 tidak lebih kecil dari 5

#5. Lebih besar dari atau sama dengan (>=)
print(a >= b)  # Output: True, karena 10 lebih besar dari 5

#6. Lebih kecil dari atau sama dengan (<=)
print(a <= b)  # Output: False, karena 10 tidak lebih kecil dari 5
#===================================================================
#catatan tambahan
x = 7
y = 3
# Contoh penggunaan operator perbandingan dalam kondisi
if x > y:
    print(f"{x} lebih besar dari {y}")  # Output: 7 lebih besar dari 3
else:
    print(f"{x} tidak lebih besar dari {y}")    # Output: 7 lebih besar dari 3

# Menggunakan operator perbandingan dalam ekspresi
hasil = (x + 2) <= (y * 3)
print(hasil)  # Output: True, karena 9 <= 9

# Menggabungkan beberapa operator perbandingan
a = 15
b = 10
c = 5

print(a > b and b > c)  # Output: True, karena 15 > 10 dan 10 > 5
print(a < b or b > c)   # Output: True, karena 10 > 5    
