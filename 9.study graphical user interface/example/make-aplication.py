#make aplication Interface(Tombol & input)

import tkinter as tk

def tekan_tombol():
    # Mengambil teks dari kotak input
    nama = kotak_nama.get()
    # Mengubah tulisan pada label hasil
    label_hasil.config(text=f"Halo, {nama}! Semangat belajarnya.")

# --- Setup Jendela ---
window = tk.Tk()
window.title("Sapaan Digital")
window.geometry("400x250")

# --- Widget 1: Label Judul ---
judul = tk.Label(window, text="Siapa nama Anda?", font=("Arial", 12))
judul.pack(pady=10) # pady=10 artinya kasih jarak vertikal 10px

# --- Widget 2: Kotak Input (Entry) ---
kotak_nama = tk.Entry(window, width=30)
kotak_nama.pack(pady=5)

# --- Widget 3: Tombol (Button) ---
# command=tekan_tombol artinya: kalau diklik, jalankan fungsi 'tekan_tombol'
tombol = tk.Button(window, text="Sapa Saya!", command=tekan_tombol)
tombol.pack(pady=10)

# --- Widget 4: Label untuk Hasil ---
label_hasil = tk.Label(window, text="...", fg="blue", font=("Arial", 10, "bold"))
label_hasil.pack(pady=10)

# --- Jalankan ---
window.mainloop()