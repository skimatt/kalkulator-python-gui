import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menangani tombol yang ditekan
def tekan_tombol(teks):
    if teks == "=":
        try:
            hasil = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, hasil)
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    elif teks == "C":
        entry.delete(0, tk.END)
    elif teks == "√":
        try:
            nilai = float(entry.get())
            if nilai < 0:
                messagebox.showerror("Error", "Akar kuadrat dari bilangan negatif tidak diizinkan!")
            else:
                hasil = math.sqrt(nilai)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(hasil))
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    elif teks == "^":
        entry.insert(tk.END, "**")
    elif teks == "sin":
        try:
            nilai = float(entry.get())
            hasil = math.sin(math.radians(nilai))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    elif teks == "cos":
        try:
            nilai = float(entry.get())
            hasil = math.cos(math.radians(nilai))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    elif teks == "tan":
        try:
            nilai = float(entry.get())
            hasil = math.tan(math.radians(nilai))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    elif teks == "log":
        try:
            nilai = float(entry.get())
            if nilai <= 0:
                messagebox.showerror("Error", "Logaritma hanya untuk bilangan positif!")
            else:
                hasil = math.log10(nilai)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(hasil))
        except Exception as e:
            messagebox.showerror("Error", "Input tidak valid!")
    else:
        entry.insert(tk.END, teks)

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Rahmat")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Membuat input field
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame untuk tombol
tombol_frame = tk.Frame(root, bg="#f0f0f0")
tombol_frame.pack()

# Daftar tombol
tombol = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '√', '^', 'sin',
    'cos', 'tan', 'log'
]

# Menambahkan tombol ke grid
baris = 1
kolom = 0
for teks in tombol:
    tombol_aksi = tk.Button(tombol_frame, text=teks, font=("Arial", 15), width=5, height=2,
                            command=lambda teks=teks: tekan_tombol(teks), bg="#e0e0e0", fg="black")
    tombol_aksi.grid(row=baris, column=kolom, padx=5, pady=5)
    kolom += 1
    if kolom > 3:
        kolom = 0
        baris += 1

# Menjalankan aplikasi
root.mainloop()