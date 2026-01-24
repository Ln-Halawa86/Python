#if pada python

# ==========================================================================================================
#konsep dasar IF pada python
#1.if digunakan untuk pengkondisian dalam program
a = 10
b = 5   
if a > b:
    print("a lebih besar dari b")  #jika a lebih besar dari b, maka akan mencetak kalimat ini
if b > a:
    print("b lebih besar dari a")  #jika b lebih besar dari a, maka akan mencetak kalimat ini   
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun

#contoh lain
nilai = 75
if nilai >= 60:
    print("Selamat, Anda lulus!")  #jika nilai lebih besar atau sama dengan 60, maka akan mencetak kalimat ini
if nilai < 60:
    print("Maaf, Anda tidak lulus.")  #jika nilai kurang dari 60, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun

#contoh lain
umur = 20
if umur >= 18:
    print("Anda sudah dewasa.")  #jika umur lebih besar atau sama dengan 18, maka akan mencetak kalimat ini 
if umur < 18:
    print("Anda masih anak-anak.")  #jika umur kurang dari 18, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun 

# Struktur Dasar (If, Elif, Else)
# if adalah pernyataan kondisi
# elif adalah singkatan dari "else if", digunakan untuk menambahkan kondisi tambahan setelah if 
# else digunakan untuk menangani kondisi ketika semua kondisi if dan elif tidak terpenuhi
# ==========================================================================================================

# ==========================================================================================================
#2.contoh penggunaan if, elif, dan else
nilai_ujian = 85
if nilai_ujian >= 90:
    print("Nilai Anda A")  #jika nilai ujian lebih besar atau sama dengan 90, maka akan mencetak kalimat ini
elif nilai_ujian >= 80:
    print("Nilai Anda B")  #jika nilai ujian lebih besar atau sama dengan 80, maka akan mencetak kalimat ini
elif nilai_ujian >= 70:
    print("Nilai Anda C")  #jika nilai ujian lebih besar atau sama dengan 70, maka akan mencetak kalimat ini
elif nilai_ujian >= 60:
    print("Nilai Anda D")  #jika nilai ujian lebih besar atau sama dengan 60, maka akan mencetak kalimat ini
else:
    print("Nilai Anda E")  #jika semua kondisi di atas tidak terpenuhi, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka akan mencetak kalimat pada else
# ==========================================================================================================


# ==========================================================================================================
#3.menggunakan operator logika dengan if
#operator logika yang umum digunakan adalah and, or, dan not
#contoh penggunaan operator logika dengan if
usia = 25
pendapatan = 5000
if usia >= 18 and pendapatan >= 3000:
    print("Anda memenuhi syarat untuk mengajukan pinjaman.")  #jika usia lebih besar atau sama dengan 18 dan pendapatan lebih besar atau sama dengan 3000, maka akan mencetak kalimat ini
if usia < 18 or pendapatan < 3000:
    print("Anda tidak memenuhi syarat untuk mengajukan pinjaman.")  #jika usia kurang dari 18 atau pendapatan kurang dari 3000, maka akan mencetak kalimat ini
if not (usia < 18):
    print("Anda sudah dewasa.")  #jika usia tidak kurang dari 18, maka akan mencetak kalimat ini    
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun

#contoh lain penggunaan operator logika dengan if
nilai_tes = 75
kehadiran = 80
if nilai_tes >= 70 and kehadiran >= 75:
    print("Anda lulus mata kuliah ini.")  #jika nilai tes lebih besar atau sama dengan 70 dan kehadiran lebih besar atau sama dengan 75, maka akan mencetak kalimat ini
if nilai_tes < 70 or kehadiran < 75:
    print("Anda tidak lulus mata kuliah ini.")  #jika nilai tes kurang dari 70 atau kehadiran kurang dari 75, maka akan mencetak kalimat ini
if not (kehadiran < 75):
    print("Kehadiran Anda memadai.")  #jika kehadiran tidak kurang dari 75, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun
# ==========================================================================================================


# ==========================================================================================================
#4.Nested If (If Bersarang)
#Nested If adalah if di dalam if
#contoh penggunaan Nested If
nilai = 85
if nilai >= 60:
    print("Selamat, Anda lulus!")  #jika nilai lebih besar atau sama dengan 60, maka akan mencetak kalimat ini
    if nilai >= 85:
        print("Anda mendapatkan predikat sangat baik.")  #jika nilai lebih besar atau sama dengan 85, maka akan mencetak kalimat ini
    else:
        print("Anda mendapatkan predikat baik.")  #jika nilai kurang dari 85, maka akan mencetak kalimat ini
else:
    print("Maaf, Anda tidak lulus.")  #jika nilai kurang dari 60, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun

#contoh lain penggunaan Nested If
usia = 20
if usia >= 18:
    print("Anda sudah dewasa.")  #jika usia lebih besar atau sama dengan 18, maka akan mencetak kalimat ini
    if usia >= 21:
        print("Anda sudah boleh mengonsumsi alkohol.")  #jika usia lebih besar atau sama dengan 21, maka akan mencetak kalimat ini
    else:
        print("Anda belum boleh mengonsumsi alkohol.")  #jika usia kurang dari 21, maka akan mencetak kalimat ini
else:
    print("Anda masih anak-anak.")  #jika usia kurang dari 18, maka akan mencetak kalimat ini
# ==========================================================================================================


# ==========================================================================================================
#5. Shorthand IF (Ternary Operator)
#Shorthand IF adalah cara singkat untuk menulis if-else dalam satu baris
#contoh penggunaan Shorthand IF
usia = 20
status = "Dewasa" if usia >= 18 else "Anak-anak"
print(status)  #jika usia lebih besar atau sama dengan 18, maka akan mencetak "Dewasa", jika tidak maka akan mencetak "Anak-anak"   

#contoh lain penggunaan Shorthand IF
nilai = 75
grade = "Lulus" if nilai >= 70 else "Tidak Lulus"
print(grade)  #jika nilai lebih besar atau sama dengan 70, maka akan mencetak "Lulus", jika tidak maka akan mencetak "Tidak Lulus"
# ==========================================================================================================




# ==========================================================================================================
#6. if dengan inputan user
#contoh penggunaan if dengan inputan user
umur = int(input("Masukkan umur Anda: "))
if umur >= 18:
    print("Anda sudah dewasa.")  #jika umur lebih besar atau sama dengan 18, maka akan mencetak kalimat ini
else:
    print("Anda masih anak-anak.")  #jika umur kurang dari 18, maka akan mencetak kalimat ini
#contoh lain penggunaan if dengan inputan user
nilai = int(input("Masukkan nilai ujian Anda: "))
if nilai >= 60:
    print("Selamat, Anda lulus!")  #jika nilai lebih besar atau sama dengan 60, maka akan mencetak kalimat ini
else:
    print("Maaf, Anda tidak lulus.")  #jika nilai kurang dari 60, maka akan mencetak kalimat ini
#jika tidak ada kondisi yang terpenuhi, maka tidak akan mencetak apapun
# ==========================================================================================================




# ==========================================================================================================
#7.Cek Kekosongan (Implicit Boolean)
#Dalam Python, beberapa nilai dianggap False secara implisit, seperti None, False, 0, "", [], {}, dan set()
#contoh penggunaan cek kekosongan dengan if
data = ""
if data:
    print("Data tidak kosong.")
else:
    print("Data kosong.")  #jika data kosong, maka akan mencetak kalimat ini

#contoh lain penggunaan cek kekosongan dengan if
data = [1, 2, 3]
if data:
    print("Data tidak kosong.")  #jika data tidak kosong, maka akan mencetak kalimat ini
    # ==========================================================================================================
