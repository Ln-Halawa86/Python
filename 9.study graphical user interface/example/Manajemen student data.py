#make aplication simple manajemen student data (Crud Simple)

import tkinter as tk
from tkinter import ttk  # Import widget tema modern (Treeview ada di sini)
from tkinter import messagebox

class AplikasiSiswa(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # 1. Konfigurasi Jendela Utama
        self.title("Aplikasi Data Siswa")
        self.geometry("600x400")
        
        # --- FRAME 1: FORM INPUT (Bagian Atas) ---
        self.frame_input = tk.Frame(self, padx=10, pady=10)
        self.frame_input.pack(fill="x") # Isi lebar layar
        
        # Label & Entry untuk Nama
        tk.Label(self.frame_input, text="Nama Siswa:").grid(row=0, column=0, sticky="w")
        self.entry_nama = tk.Entry(self.frame_input, width=30)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)
        
        # Label & Entry untuk Jurusan
        tk.Label(self.frame_input, text="Jurusan:").grid(row=1, column=0, sticky="w")
        self.entry_jurusan = tk.Entry(self.frame_input, width=30)
        self.entry_jurusan.grid(row=1, column=1, padx=5, pady=5)
        
        # Tombol Tambah
        tk.Button(self.frame_input, text="Simpan Data", command=self.tambah_data, bg="#4CAF50", fg="white").grid(row=2, column=1, sticky="e", pady=5)

        # --- FRAME 2: TABEL DATA (Bagian Bawah) ---
        self.frame_tabel = tk.Frame(self, padx=10, pady=10)
        self.frame_tabel.pack(fill="both", expand=True)
        
        # Membuat Treeview (Tabel)
        # columns=("1", "2") artinya kita punya 2 kolom data selain kolom utama
        self.tabel = ttk.Treeview(self.frame_tabel, columns=("nama", "jurusan"), show="headings")
        
        # Mengatur Header Tabel
        self.tabel.heading("nama", text="Nama Lengkap")
        self.tabel.heading("jurusan", text="Jurusan")
        
        # Mengatur Lebar Kolom
        self.tabel.column("nama", width=250)
        self.tabel.column("jurusan", width=200)
        
        self.tabel.pack(fill="both", expand=True)
        
        # Tombol Hapus (Di bawah tabel)
        tk.Button(self.frame_tabel, text="Hapus Data Terpilih", command=self.hapus_data, bg="#f44336", fg="white").pack(pady=10)

    # --- LOGIKA PROGRAM ---
    
    def tambah_data(self):
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        
        if nama == "" or jurusan == "":
            messagebox.showwarning("Peringatan", "Data tidak boleh kosong!")
            return
            
        # Masukkan data ke tabel
        self.tabel.insert("", "end", values=(nama, jurusan))
        
        # Kosongkan input setelah simpan
        self.entry_nama.delete(0, "end")
        self.entry_jurusan.delete(0, "end")
        
    def hapus_data(self):
        # Ambil item yang sedang dipilih (disorot biru)
        item_terpilih = self.tabel.selection()
        
        if not item_terpilih:
            messagebox.showinfo("Info", "Pilih data yang ingin dihapus dulu.")
            return
            
        # Hapus item tersebut
        for item in item_terpilih:
            self.tabel.delete(item)

# Menjalankan Aplikasi
if __name__ == "__main__":
    app = AplikasiSiswa()
    app.mainloop()