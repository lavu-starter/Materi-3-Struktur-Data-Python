import tkinter as tk
from tkinter import messagebox
import json
import os

# --- Fungsi JSON ---
def load_data():
    if os.path.exists("siswa.json"):
        with open("siswa.json", "r") as f:
            return json.load(f)["siswa"]
    return []

def save_data():
    with open("siswa.json", "w") as f:
        json.dump({"siswa": siswa}, f, indent=4)

def tambah_data():
    nama = entry_nama.get()
    nilai = entry_nilai.get()

    if not nama or not nilai:
        messagebox.showwarning("Peringatan", "Nama dan Nilai tidak boleh kosong!")
        return
    
    try:
        nilai = int(nilai)
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    siswa.append({"nama": nama, "nilai": nilai})
    save_data()
    tampilkan_data()
    entry_nama.delete(0, tk.END)
    entry_nilai.delete(0, tk.END)

def tampilkan_data():
    listbox.delete(0, tk.END)
    for data in siswa:
        listbox.insert(tk.END, f"Nama: {data['nama']}, Nilai: {data['nilai']}")

# --- GUI ---
root = tk.Tk()
root.title("Program Daftar Nilai Siswa")
root.geometry("400x400")

# Frame input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Nilai:").grid(row=1, column=0, padx=5, pady=5)
entry_nilai = tk.Entry(frame_input)
entry_nilai.grid(row=1, column=1, padx=5, pady=5)

btn_tambah = tk.Button(frame_input, text="Tambah", command=tambah_data)
btn_tambah.grid(row=2, column=0, columnspan=2, pady=10)

# Listbox untuk menampilkan data
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Load data awal
siswa = load_data()
tampilkan_data()

root.mainloop()
