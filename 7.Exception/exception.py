#Exception adalah kondisi yang muncul ketika terjadi kesalahan atau error dalam program. 
#Ketika exception terjadi, program akan menghentikan eksekusi dan menampilkan pesan kesalahan yang lebih detail

#struktur exception apa aja?
#try, except, else, finally
#try adalah blok kode yang akan dicoba untuk dijalankan. Jika terjadi kesalahan, maka blok except akan dijalankan.
#contoh :
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    #ZeroDivisionError adalah exception yang muncul ketika terjadi pembagian dengan nol

    print("Tidak dapat membagi dengan nol")
    #output : Tidak dapat membagi dengan nol

#================================================================================================================================================
#except adalah blok kode yang akan dijalankan ketika terjadi kesalahan dalam blok try.
#tipe error yang bisa ditangkap except apa aja?
#a.ZeroDivisionError yaitu menangkap kesalahan pembagian dengan nol
#b.NameError yaitu menangkap kesalahan ketika variabel tidak didefinisikan
#contoh NameError
# --- Contoh 1: Variabel Belum Didefinisikan ---
print("=== Contoh 1: Variabel Tidak Ada ===")
try:
    # Mencoba mencetak variabel 'nama_user' yang belum pernah dibuat sebelumnya
    print(nama_user) 
except NameError as e:
    print(f"Error tertangkap! Pesan sistem: {e}")
    print("Solusi: Pastikan variabel sudah dibuat sebelum dipanggil.")

print("\n" + "-"*30 + "\n")

# --- Contoh 2: Salah Ketik (Typo) ---
print("=== Contoh 2: Typo Nama Variabel ===")
try:
    harga_barang = 5000
    
    # Perhatikan: kita menulis 'harga_brang' (kurang huruf 'a')
    total = harga_brang * 2
    print(f"Total: {total}")
    
except NameError:
    print("Error tertangkap! Sepertinya ada salah ketik (typo) pada nama variabel.")

print("\nProgram selesai tanpa crash.")

#c. TypeError yaitu menangkap kesalahan ketika tipe data tidak sesuai
#contoh typeError
try:
    a = 10
    b = "20"
    c = a + b
    print(c)
except TypeError:
    print("Tipe data tidak sesuai")
    #output : Tipe data tidak sesuai


#d.IndexError yaitu menangkap kesalahan ketika indeks tidak valid
#contoh IndexError
try:
    a = [1, 2, 3]
    print(a[3])
except IndexError:
    print("Indeks tidak valid")
    #output : Indeks tidak valid

#e.KeyError yaitu menangkap kesalahan ketika key tidak ditemukan
#contoh KeyError
try:    
    a = {"nama": "Andi", "umur": 20}
    print(a["alamat"])
except KeyError:
    print("Key tidak ditemukan")
    #output : Key tidak ditemukan


#f.ValueError yaitu menangkap kesalahan ketika nilai tidak valid
#contoh ValueError
try:
    int("a")
except ValueError:
    print("Nilai tidak valid")
    #output : Nilai tidak valid


#g. OSError yaitu menangkap kesalahan operasi sistem
#contoh OSError
try:
    import os
    os.remove("file.txt")
except OSError:
    print("Gagal menghapus file")
    #output : Gagal menghapus file

#h.IOError yaitu menangkap kesalahan input/output
#contoh IOError
try:
    f = open("file.txt", "r")
    f.read()
except IOError:
    print("Gagal membaca file")
    #output : Gagal membaca file

#i.FileNotFoundError yaitu menangkap kesalahan ketika file tidak ditemukan
#contoh FileNotFoundError
try:
    f = open("file.txt", "r")
    f.read()
except FileNotFoundError:
    print("File tidak ditemukan")
    #output : File tidak ditemukan


#j.SyntaxError yaitu menangkap kesalahan sintaks
#contoh SyntaxError
try:
    exec("print('Hello World')")
except SyntaxError:
    print("Kesalahan sintaks")
    #output : Kesalahan sintaks

#================================================================================================================================================

#apa itu maksud else di exception?
#Else adalah blok kode yang akan dijalankan ketika tidak terjadi kesalahan dalam blok try.
#jika tidak ada kesalahan dalam blok try, maka blok else akan dijalankan.
#contoh :
try:
    a = 10
    b = 5
    c = a + b
    print(c)
except:
    print("Terjadi kesalahan")
else:
    print("Tidak terjadi kesalahan")
    #output : Tidak terjadi kesalahan


#apa itu finally?
#Finally adalah blok kode yang akan selalu dijalankan, baik terjadi kesalahan atau tidak.
#contoh :
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except:
    print("Terjadi kesalahan")
finally:
    print("Program selesai")
    #output : Program selesai



#apa itu raise?
#Raise adalah keyword yang digunakan untuk menimbulkan exception.
#contoh :
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except:
    print("Terjadi kesalahan")
    raise
    #output : Terjadi kesalahan

# contoh lain
def cek_umur(umur):
    if umur < 0:
        # Kita memicu error secara manual
        raise ValueError("Umur tidak boleh negatif!")
    print(f"Umur kamu {umur} tahun.")
    #cara kerja raise bagaimana?
    #jika umur < 0, maka raise akan memicu error ValueError
    #kemudian error tersebut akan ditangkap oleh except
    #setelah error di tangkap oleh except, kemudian disimpan ke variabel error_saya
    #kemudian print error_saya
try:
    cek_umur(-5)
except ValueError as error_saya:
    print(f"Validasi Gagal: {error_saya}")
    