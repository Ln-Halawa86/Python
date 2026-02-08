#Tkinter adalah pilihan terbaik untuk memulai karena ia adalah pustaka bawaan Python (standar). Jadi, Anda tidak perlu menginstal apa pun lagi.

#Konsep Dasar Tkinter: "Kanvas dan Stiker"
#Bayangkan membuat aplikasi GUI itu seperti membuat kolase di papan tulis:
#Root (Jendela Utama): Ini adalah papan tulis atau bingkai utamanya.
#Widget: Ini adalah "stiker" atau komponen yang Anda tempelkan di papan (Tombol, Label Teks, Kotak Input).
#Geometry Manager: Ini adalah aturan cara menempelkannya (apakah ditumpuk ke bawah, dijajar ke samping, atau disusun kotak-kotak).
#Mainloop: Ini adalah "nyawa" aplikasi yang membuatnya tetap menyala menunggu klik dari pengguna.
import tkinter as tk  # 1. Import modul

# 2. Membuat Jendela Utama (Root)
window = tk.Tk()
window.title("Aplikasi Pertamaku") # Judul di atas window
window.geometry("300x200") # Ukuran window (lebar x tinggi)

# 3. Membuat Widget (Label)
label_sapaan = tk.Label(window, text="Halo, saya belajar Tkinter!", font=("Arial", 14))

# 4. Menampilkan Widget ke Layar
label_sapaan.pack()  # .pack() artinya "tempelkan saja di tengah/atas"

# 5. Menjalankan Aplikasi
window.mainloop()