import tkinter as tk
import sqlite3

def hasil_prediksi():
    nama = nama_entry.get()
    nilai_biologi = float(biologi_entry.get())
    nilai_fisika = float(fisika_entry.get())
    nilai_inggris = float(inggris_entry.get())

    # Menentukan prodi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # Menampilkan hasil prediksi
    prodi_label.config(text=f"Prodi Pilihan: {prediksi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()

    # Mengecek apakah tabel sudah ada, jika belum maka membuatnya
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')

    # Memasukkan data ke tabel
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                      VALUES (?, ?, ?, ?, ?)''', (nama, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))

    # Commit dan menutup koneksi
    conn.commit()
    conn.close()

# Membuat instance Tkinter
app = tk.Tk()
app.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat input untuk nama siswa
tk.Label(app, text="Nama Siswa").grid(row=0, column=0, pady=5)
nama_entry = tk.Entry(app)
nama_entry.grid(row=0, column=1, pady=5)

# Membuat input untuk nilai biologi
tk.Label(app, text="Nilai Biologi").grid(row=1, column=0, pady=5)
biologi_entry = tk.Entry(app)
biologi_entry.grid(row=1, column=1, pady=5)

# Membuat input untuk nilai fisika
tk.Label(app, text="Nilai Fisika").grid(row=2, column=0, pady=5)
fisika_entry = tk.Entry(app)
fisika_entry.grid(row=2, column=1, pady=5)

# Membuat input untuk nilai inggris
tk.Label(app, text="Nilai Bahasa Inggris").grid(row=3, column=0, pady=5)
inggris_entry = tk.Entry(app)
inggris_entry.grid(row=3, column=1, pady=5)

# Menambahkan 10 mata kuliah lagi
mata_kuliah_labels = ["Nilai Matematika", "Nilai Kimia", "Nilai Bahasa Indonesia", "Nilai Komputer",
                       "Nilai Ekonomi", "Nilai Geografi", "Nilai Sosiologi", "Nilai Seni", "Nilai Pendidikan Jasmani", "Nilai Sejarah"]

nilai_entries = []
for i, label in enumerate(mata_kuliah_labels):
    tk.Label(app, text=label).grid(row=i+4, column=0, pady=5)
    entry = tk.Entry(app)
    entry.grid(row=i+4, column=1, pady=5)
    nilai_entries.append(entry)

# Membuat button Hasil Prediksi
button_prediksi = tk.Button(app, text="Submit Nilai", command=hasil_prediksi)
button_prediksi.grid(row=15, column=0, columnspan=2, pady=10)

# Membuat label luaran hasil prediksi
prodi_label = tk.Label(app, text="Prodi Pilihan: -", font=("Helvetica", 12))
prodi_label.grid(row=16, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
app.mainloop()
