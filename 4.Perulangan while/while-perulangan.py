# 1.Perulangan While
# while adalah salah satu struktur kontrol dalam pemrograman yang digunakan untuk menjalankan blok kode berulang 
# kali selama kondisi tertentu bernilai True.
# Sintaks dasar dari perulangan while adalah sebagai berikut:
# while kondisi:
#     blok kode yang akan dijalankan selama kondisi bernilai True   
# Contoh penggunaan perulangan while dalam Python:
# Inisialisasi variabel
count = 0
# Kondisi perulangan
while count < 5:
    print("Count is:", count)
    count += 1  # Increment nilai count sebesar 1 setiap iterasi   

    #kenapa memakai += 1 bukan = + 1?
    #Penjelasan:
    #   Operator += adalah operator penugasan yang digunakan untuk menambahkan nilai ke variabel
    #   dan kemudian menyimpan hasilnya kembali ke variabel tersebut. Jadi, count += 1
    #   adalah singkatan dari count = count + 1. Ini berarti bahwa nilai saat ini dari count
    #   akan ditambah dengan 1, dan hasilnya akan disimpan kembali ke variabel count.
    #   Jika kita menggunakan count = +1, itu akan mengatur nilai count menjadi positif 1 setiap kali,
    #   bukan menambahkannya. Oleh karena itu, untuk meningkatkan nilai count secara bertahap, kita menggunakan count += 1. 
    
    #cara kerjanya:
    # 1. Pertama, kondisi count < 5 dievaluasi. Jika kondisi ini True, blok kode di dalam while akan dijalankan.
    # 2. Di dalam blok kode, nilai count dicetak, dan kemudian count ditingkatkan sebesar 1 menggunakan count += 1.
    # 3. Setelah blok kode selesai dijalankan, program kembali ke langkah 1 untuk mengevaluasi kondisi lagi.
    # 4. Proses ini berlanjut hingga kondisi count < 5 menjadi False (yaitu ketika count mencapai 5).
    # gambaranya seperti ini:
    # Iterasi 1: count = count + 1 -> count = 0 + 1 -> count = 1
    # Iterasi 2: count = count + 1 -> count = 1 + 1 -> count = 2
    # Iterasi 3: count = count + 1 -> count = 2 + 1 -> count = 3
    # Iterasi 4: count = count + 1 -> count = 3 + 1 -> count = 4
    # Iterasi 5: count = count + 1 -> count = 4 + 1 -> count = 5 (kondisi menjadi False, perulangan berhenti)


# Output:
# Count is: 0
# Count is: 1   
# Count is: 2
# Count is: 3
# Count is: 4
# Penjelasan:
# Pada contoh di atas, perulangan while akan terus berjalan selama nilai variabel count kurang dari 5.
# Setiap kali perulangan dijalankan, nilai count akan dicetak dan kemudian ditingkatkan sebesar 1.
# Ketika nilai count mencapai 5, kondisi count < 5 menjadi False, sehingga perulangan berhenti.
# Perulangan while sangat berguna ketika jumlah iterasi tidak diketahui sebelumnya dan bergantung pada kondisi tertentu.

# apa itu iterasi?
# Iterasi adalah proses pengulangan suatu blok kode atau pernyataan dalam pemrograman.
# Setiap kali blok kode tersebut dijalankan, itu disebut satu iterasi.
# Iterasi biasanya digunakan dalam struktur kontrol seperti perulangan (looping) untuk mengeksekusi kode berulang kali
# sampai kondisi tertentu terpenuhi.
# Contoh sederhana iterasi adalah dalam perulangan while di atas, di mana setiap kali blok kode di dalam while dijalankan,
# itu dihitung sebagai satu iterasi.

# Apa itu kondisi?
# Kondisi adalah ekspresi logika yang dievaluasi sebagai True (benar) atau False (salah).
# Kondisi digunakan dalam struktur kontrol seperti perulangan (looping) dan percabangan (if-else)
# untuk menentukan alur eksekusi program.
# Dalam konteks perulangan while, kondisi menentukan apakah blok kode di dalam perulangan akan dijalankan atau tidak.
# Jika kondisi bernilai True, blok kode akan dieksekusi; jika False, perulangan akan berhenti.

#2. Contoh lain penggunaan perulangan while:
# Inisialisasi variabel
number = 1
# Kondisi perulangan
while number <= 10:
    print("Number is:", number)
    number += 2  # Increment nilai number sebesar 2 setiap iterasi
# Output:
# Number is: 1, 3, 5, 7, 9


# Soal latihan:
# Buatlah program menggunakan perulangan while yang mencetak bilangan genap dari 2 hingga 20!
angka = 2
while angka <= 20:
    print("bilangan genap :", angka)
    angka += 2 
# Output:
# bilangan genap : 2
# bilangan genap : 4
# bilangan genap : 6
# bilangan genap : 8
# bilangan genap : 10
# bilangan genap : 12
# bilangan genap : 14
# bilangan genap : 16
# bilangan genap : 18
# bilangan genap : 20


#========================================================================
#========================================================================
#========================================================================
# 3. Kontrol Eksekusi (break dan continue)
# break dan continue adalah dua pernyataan kontrol eksekusi yang digunakan dalam perulangan (looping) untuk mengubah alur eksekusi perulangan tersebut.
# Pernyataan break digunakan untuk menghentikan perulangan secara keseluruhan, sedangkan pernyataan continue 
# digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.
# Contoh penggunaan break dalam perulangan while:
count = 0
while count < 10:
    if count == 5:
        break  # Menghentikan perulangan ketika count mencapai 5
    print("Count is:", count)
    count += 1  
# Output:
# Count is: 0
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4


# Contoh penggunaan continue dalam perulangan while:
count = 0
while count < 10:
    count += 1  
    if count % 2 == 0:
        continue  # Melewati iterasi saat count adalah bilangan genap
    print("Count is:", count)

    # kenapa pakai % 2 == 0?
    # Penjelasan:
    # Operator % adalah operator modulus yang digunakan untuk mendapatkan sisa pembagian antara dua angka.
    # Dalam konteks count % 2 == 0, ini berarti kita memeriksa apakah count adalah bilangan genap.
    # Jika count dibagi 2 menghasilkan sisa 0, maka count adalah bilangan genap.
    # Jika kondisi ini terpenuhi (count adalah bilangan genap), pernyataan continue akan dieksekusi,
    # yang menyebabkan program melewati sisa kode dalam loop untuk iterasi saat ini dan melanjutkan ke iterasi berikutnya.     

# Output:
# Count is: 1   
# Count is: 3
# Count is: 5
# Count is: 7
# Count is: 9

# contoh gabungan break dan continue:
count = 0
while count < 10:
    count += 1  
    if count == 7:
        break  # Menghentikan perulangan ketika count mencapai 7
    if count % 2 == 0:
        continue  # Melewati iterasi saat count adalah bilangan genap
    print("Count is:", count)
# Output:
# Count is: 1
# Count is: 3
# Count is: 5

# latihan soal kontrol eksekusi:
# Buatlah program menggunakan perulangan while yang mencetak bilangan ganjil dari 1 hingga 15,
# tetapi hentikan perulangan jika bilangan ganjil mencapai 11!
angka_ganjil = 0
while angka_ganjil < 15:
    angka_ganjil += 1
    if angka_ganjil == 11:
        break
    if angka_ganjil % 2 == 0:
        continue
    print("bilangan ganjil :", angka_ganjil)
# Output:
# bilangan ganjil : 1
# bilangan ganjil : 3
# bilangan ganjil : 5
# bilangan ganjil : 7
# bilangan ganjil : 9

#=======================================================================
#=======================================================================
#=======================================================================
# 4. Perulangan Tak Terbatas (Infinite Loop)
# Perulangan tak terbatas (infinite loop) adalah perulangan yang terus berjalan tanpa henti karena kondisi perulangan selalu bernilai True.
# Contoh perulangan tak terbatas menggunakan while:
# while True:
#     print("This is an infinite loop!")
# Output:
# This is an infinite loop!
# Penjelasan:
# Pada contoh di atas, kondisi while selalu True, sehingga blok kode di dalam perulangan akan terus dijalankan tanpa henti.
# Perulangan tak terbatas dapat berguna dalam beberapa situasi, seperti menunggu input dari pengguna atau menjalankan server yang harus selalu aktif.
# Namun, perulangan tak terbatas juga dapat menyebabkan program menjadi tidak responsif atau macet jika tidak diatur dengan benar.
# Untuk menghentikan perulangan tak terbatas, biasanya digunakan pernyataan break di dalam blok kode perulangan berdasarkan kondisi tertentu atau intervensi dari pengguna (misalnya, menekan Ctrl+C di terminal).
# Penting untuk selalu memastikan bahwa perulangan tak terbatas memiliki mekanisme untuk keluar dari perulangan agar tidak menyebabkan masalah pada program. 
#=======================================================================


#=======================================================================
#=======================================================================
#=======================================================================
# 5. while Loop dengan else (Fitur Unik Python)
# Dalam Python, perulangan while dapat memiliki blok else yang akan dieksekusi ketika kondisi perulangan menjadi False.
# Contoh penggunaan while dengan else:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Perulangan selesai!")
# Output:
# Count is: 0
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Perulangan selesai!

#contoh lain:
number = 1
while number <= 3:
    print("Number is:", number)
    number += 1
else:
    print("Semua bilangan telah dicetak.")
# Output:
# Number is: 1
# Number is: 2
# Number is: 3
# Semua bilangan telah dicetak.


#contoh pengunaan else dan while untuk mencari bilangan prima
num = 10
i = 2
while i <= num // 2:
    if num % i == 0:
        print(num, "bukan bilangan prima")
        break
    i += 1
else:
    print(num, "adalah bilangan prima")
# Output:
# 10 bukan bilangan prima
