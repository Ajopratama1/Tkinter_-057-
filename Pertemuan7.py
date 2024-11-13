import tkinter as tk

def hasil_prediksi():
    label_hasil.config(text="Prodi yang diprediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("300x400")
root.configure(bg="orange")

tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14)).pack(pady=10)

entries = []
for i in range(10):
    tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:").pack(anchor="w", padx=10)
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)
    entries.append(entry)

tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi).pack(pady=20)

label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()

#PENJELASAN
#Fungsi hasil_prediksi:

#Fungsi ini akan dipanggil ketika tombol "Hasil Prediksi" ditekan. Fungsi ini menampilkan teks "Teknologi Informasi" pada label hasil.
#Komponen GUI:
#Label judul: Menampilkan teks judul di bagian atas.
#10 Input nilai: Menggunakan Entry untuk memasukkan nilai mata pelajaran.
#Tombol Prediksi: Menggunakan Button yang ketika ditekan akan memanggil fungsi hasil_prediksi.
##Label hasil: Menampilkan hasil prediksi.
#Tata Letak:
#Menggunakan metode pack() dan grid() untuk menyusun komponen agar lebih rapi.
