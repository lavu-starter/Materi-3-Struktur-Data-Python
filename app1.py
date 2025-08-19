# Program Daftar Nilai Siswa
import json
import os

# Cek apakah file siswa.json sudah ada
if os.path.exists("siswa.json"):
    with open("siswa.json", "r") as f:
        data = json.load(f)
        siswa = data["siswa"]
else:
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

# Input berulang (bisa sampai 50 data atau lebih)
while True:
    print("\nTambah Data Siswa")
    nama_baru = input("Masukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
    if nama_baru.lower() == "selesai":
        break
    nilai_baru = int(input("Masukkan nilai: "))

    siswa.append({"nama": nama_baru, "nilai": nilai_baru})

    # Simpan setiap kali ada penambahan
    with open("siswa.json", "w") as f:
        json.dump({"siswa": siswa}, f, indent=4)

# Menampilkan daftar siswa setelah penambahan
print("\nDaftar Nilai Siswa Terbaru:")
print("---------------------------")
for data in siswa:
    print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")
