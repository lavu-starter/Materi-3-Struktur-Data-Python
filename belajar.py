# Program Daftar Umur Siswa
import json  # ✅ tambahkan ini di bagian atas

# Menyimpan data siswa dalam list of dictionary
siswa = [
    {"nama": "Andi", "umur": 16},
    {"nama": "Budi", "umur": 17},
    {"nama": "Citra", "umur": 15}
]

# Menampilkan daftar siswa
print("Daftar Umur Siswa:")
print("-------------------")
for data in siswa:
    print(f"Nama: {data['nama']}, Umur: {data['umur']}")

# Menambahkan data baru dari input pengguna
print("\nTambah Data Siswa")
nama_baru = input("Masukkan nama siswa: ")
umur_baru = int(input("Masukkan umur: "))

siswa.append({"nama": nama_baru, "umur": umur_baru})

# ✅ Simpan data ke file JSON setelah penambahan
with open("siswa.json", "w") as f:
    json.dump({"siswa": siswa}, f, indent=4)

# Menampilkan daftar siswa setelah penambahan
print("\nDaftar Umur Siswa Terbaru:")
print("---------------------------")
for data in siswa:
    print(f"Nama: {data['nama']}, Umur: {data['umur']}")
