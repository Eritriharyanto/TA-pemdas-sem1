# Definisi variabel global
tabel_mahasiswa = []

# Fungsi untuk menambahkan data mahasiswa
def tambah_mahasiswa():
    nama = input("Nama: ")
    npm = input("NPM: ")
    fakultas = input("Fakultas: ")
    prodi = input("Prodi: ")
    kota_asal = input("Kota Asal: ")
    tabel_mahasiswa.append((nama, npm, fakultas, prodi, kota_asal))

# Fungsi untuk membuat tabel mahasiswa
def buat_tabel_mahasiswa():
    print("\nTabel Mahasiswa:")
    print("| No |   Nama   |    NIM    |    FAKULTAS   |     PRODI     |    KOTA ASAL    |")
    print("|----|----------|-----------|---------------|---------------|-----------------|")
    for i, data in enumerate(tabel_mahasiswa, 1):
        print(f"| {i:2} | {data[0]:<9} | {data[1]:<10} | {data[2]:<11} | {data[3]:<12} | {data[4]:<15} |")

# Logika kondisional untuk menentukan apakah tabel mahasiswa akan ditampilkan atau tidak
def tampilkan_tabel():
    tampilkan = input("Apakah Anda ingin menampilkan tabel mahasiswa? (ya/tidak): ").lower()
    if tampilkan == "ya":
        buat_tabel_mahasiswa()
    else:
        print("Terima kasih.")

# Logika perulangan untuk menambahkan data mahasiswa
def input_data_mahasiswa():
    n = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(n):
        print(f"\nMasukkan data untuk mahasiswa ke-{i + 1}:")
        tambah_mahasiswa()

# Program utama
input_data_mahasiswa()
tampilkan_tabel()
