# Program Daftar Nilai Siswa
import json  # ✅ tambahkan ini di bagian atas

# Menyimpan data siswa dalam list of dictionary
siswa = [
    {"nama": "Andi", "nilai": 85},
    {"nama": "Budi", "nilai": 90},
    {"nama": "Citra", "nilai": 78}
]

# Menampilkan daftar siswa
print("Daftar Nilai Siswa:")
print("-------------------")
for data in siswa:
    print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")

# Menambahkan data baru dari input pengguna
print("\nTambah Data Siswa")
nama_baru = input("Masukkan nama siswa: ")
nilai_baru = int(input("Masukkan nilai: "))

siswa.append({"nama": nama_baru, "nilai": nilai_baru})

# ✅ Simpan data ke file JSON setelah penambahan
with open("siswa.json", "w") as f:
    json.dump({"siswa": siswa}, f, indent=4)

# Menampilkan daftar siswa setelah penambahan
print("\nDaftar Nilai Siswa Terbaru:")
print("---------------------------")
for data in siswa:
    print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")
