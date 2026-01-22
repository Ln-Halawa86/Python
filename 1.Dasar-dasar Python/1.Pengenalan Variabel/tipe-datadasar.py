# 1. String (Bisa petik satu atau dua)
nama_depan = "John"
nama_belakang = 'Broken'

# 2. Integer (Bilangan bulat)
umur = 25
jumlah_hari = 365

# 3. Float (Desimal)
# Di JS semua angka adalah 'Number', di Python dibedakan Int dan Float
berat_badan = 65.5
pi = 3.14

# 4. Boolean (Wajib Huruf Besar Awalnya)
is_login = True
has_data = False

# 5. None (Sama dengan null di JS)
alamat = None

# 6. Multiple Assignment
# Python punya fitur keren untuk mempersingkat kode yang di JS agak panjang. Kamu bisa mengisi banyak variabel dalam satu baris.
# Mengisi nilai x, y, dan z sekaligus
x, y, z = 10, 20, 30

print(x) # Output: 10
print(y) # Output: 20

# 7.Cek Tipe Data
# di Python kamu pakai fungsi type().
x = 100
y = "Seratus"

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>

# 8. String Formatting (F-String)
nama = "Budi"
# Taruh huruf 'f' sebelum tanda kutip
print(f"Halo, {nama}")