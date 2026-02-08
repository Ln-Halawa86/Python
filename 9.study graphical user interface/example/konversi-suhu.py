import tkinter as tk
from tkinter import messagebox  # Import untuk menampilkan pesan error

def hitung_konversi():
    try:
        # 1. MENGAMBIL INPUT (Pengganti input() )
        # Kita ambil teks dari kotak input, lalu ubah jadi angka (float)
        suhu_f = float(entry_suhu.get())
        
        # 2. LOGIKA HITUNGAN (Sama seperti sebelumnya)
        suhu_c = (suhu_f - 32) * 5/9
        
        # 3. MENAMPILKAN OUTPUT (Pengganti print() )
        # Kita ubah teks pada label hasil. {:.2f} artinya ambil 2 angka di belakang koma.
        label_hasil.config(text=f"Hasil: {suhu_c:.2f} °C", fg="blue")
        
    except ValueError:
        # Jika user memasukkan huruf bukan angka
        messagebox.showerror("Error", "Mohon masukkan angka yang valid!")

# --- MEMBUAT JENDELA UTAMA ---
window = tk.Tk()
window.title("Konversi Suhu")
window.geometry("350x250")

# --- MEMBUAT WIDGET (KOMPONEN) ---

# 1. Label Judul
judul = tk.Label(window, text="Konversi Fahrenheit ke Celsius", font=("Arial", 12, "bold"))
judul.pack(pady=10)

# 2. Label Petunjuk
label_input = tk.Label(window, text="Masukkan Suhu (Fahrenheit):")
label_input.pack()

# 3. Kotak Input (Entry)
entry_suhu = tk.Entry(window, width=20)
entry_suhu.pack(pady=5)

# 4. Tombol (Button)
# command=hitung_konversi artinya saat diklik, jalankan fungsi di atas
tombol = tk.Button(window, text="Konversi Sekarang", command=hitung_konversi, bg="#dddddd")
tombol.pack(pady=10)

# 5. Label untuk Menampilkan Hasil
label_hasil = tk.Label(window, text="Hasil: ...", font=("Arial", 14, "bold"))
label_hasil.pack(pady=20)

# --- MENJALANKAN APLIKASI ---
window.mainloop()