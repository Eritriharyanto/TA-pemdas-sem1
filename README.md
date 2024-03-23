###pada file yang bernama teslagii.py
kode ini adalah untuk menampilkan tabel mahasiswa atau tidak yang telah diisi
kode adalah mencangkup definisi variabel, logika kondisional, logika perulangan, penggunaan fungsi, penggunaan data struktur
1.definisi variabel: Variabel-variabel seperti tabel_mahasiswa, nama, npm, fakultas, prodi, dan kota_asal
2.logika kondisional: Logika kondisional digunakan untuk menentukan apakah pengguna ingin menampilkan tabel mahasiswa atau tidak setelah tabel dibuat. Ini terjadi pada bagian if tampilkan == "ya":
3.llogika perulangan: Logika perulangan digunakan untuk menginputkan data mahasiswa sebanyak n kali menggunakan loop for i in range(n):
4.penggunaan funsi: Ada beberapa fungsi yang digunakan dalam kode ini. tambah_mahasiswa() digunakan untuk menambahkan data mahasiswa ke dalam daftar tabel_mahasiswa buat_tabel_mahasiswa() digunakan untuk mencetak tabel mahasiswa ke layar. tampilkan_tabel() digunakan untuk menampilkan tabel mahasiswa jika pengguna menginginkannya. input_data_mahasiswa() digunakan untuk menginputkan data mahasiswa dari pengguna.
5.data struktur:Data mahasiswa disimpan dalam sebuah daftar tabel_mahasiswa, di mana setiap entri adalah tupel yang berisi nama, NPM, fakultas, prodi, dan kota asal mahasiswa
dan kode ini akan menampilkan tabel mahasiswa jika memilih(ya) dan tidak menampilkan tabel jika memilih menu(tidak)

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


###pada file yang bernama kasir.py
kode ini adalah untuk menampilkan struk pembelian yang telah di pilih 
kode adalah mencangkup definisi variabel, logika kondisional, logika perulangan, penggunaan fungsi, penggunaan data struktur
Definisi Variabel: Variabel-variabel seperti pembeli, toples, kuekering, totalkuekering, totalkuebasah, kuebasah, buah, totalsemua, uang, dan kembalian didefinisikan untuk menyimpan data dan hasil perhitungan dalam program.
1.Penggunaan Logika Kondisional: Logika kondisional digunakan dalam kedua fungsi fungsikuekering() dan fungsikuebasah() untuk menentukan pilihan pengguna dan melakukan perhitungan berdasarkan pilihan tersebut.
2.Penggunaan Logika Perulangan: Meskipun tidak ada logika perulangan dalam kode utama, namun pada bagian ketika pilihan tidak valid, program memanggil kembali fungsi yang sama sampai input yang valid diberikan, seperti yang terjadi pada fungsi fungsikuebasah().
3.Penggunaan Fungsi: Ada dua fungsi yang digunakan dalam kode ini, yaitu fungsikuekering() dan fungsikuebasah(), yang digunakan untuk meminta input dari pengguna dan melakukan perhitungan berdasarkan input tersebut.
4.Penggunaan Struktur Data (Daftar/List): Meskipun tidak ada penggunaan struktur data daftar (list) secara eksplisit dalam kode ini, namun data disimpan dalam variabel-variabel yang didefinisikan sebelumnya, seperti tupel yang digunakan untuk menyimpan data mahasiswa dan data pembelian kue kering/kue basah.
5.dan kode ini akan menampilkan tabel mahasiswa jika memilih(ya) dan tidak menampilkan tabel jika memilih menu(tidak)

    print("-------------- Progam Kasir Sederhana ----------------")
    pembeli = input("Masukkan nama pembeli: ")
    print("Nama Pembeli :", pembeli)
    
    def fungsikuekering():
        global totalkuekering
        global toples
        global kuekering
        print("\n-------------- Menu Kue Kering ----------")
        print("1. Kastangel - Rp 70000")
        print("2. Nastar - Rp 80000")
        print("3. Sagu keju - Rp 60000")
        nomor = int(input("Masukkan Pilihan: "))
        toples = int(input("Berapa Toples: "))
    
        if nomor == 1:
            totalkuekering = toples * 70000
            print(toples, " toples Kastangel = Rp", totalkuekering)
            kuekering = "Kastangel"
        elif nomor == 2:
            totalkuekering = toples * 80000
            print(toples, " toples Nastar = Rp", totalkuekering)
            kuekering = "Nastar"
        elif nomor == 3:
            totalkuekering = toples * 60000
            print(toples, " toples Sagu Keju= Rp", totalkuekering)
            kuekering = "Sagu Keju"
        else:
            print("Pilihan tidak ada, Silahkan masukkan lagi!!")
    
    def fungsikuebasah():
        global totalkuebasah
        global kuebasah
        global buah
        print("\n---------- Menu Kue Basah -----------")
        print("1. Pastel - Rp 5000 ")
        print("2. Kroket - Rp 4000 ")
        print("3. Pie buah - Rp 6000 ")
        nomor = int(input("Masukkan Pilihan: "))
        buah = int(input("Berapa buah: "))
    
        if nomor == 1:
            totalkuebasah = buah * 5000 
            print(buah, " Pastel = Rp", totalkuebasah)
            kuebasah = "Pastel"
        elif nomor == 2:
            totalkuebasah = buah * 4000
            print(buah, "Kroket = Rp", totalkuebasah)
            kuebasah = "Kroket"
        elif nomor == 3:
            totalkuebasah = buah * 6000
            print(buah, " pie buah = Rp", totalkuebasah)
            kuebasah = "pie buah"
        else:
            print("pilihan tidak ada, silahkan masukan lagi!!")
            fungsikuebasah()
    
    fungsikuebasah()
    fungsikuekering()
    
    # Perbaikan perhitungan total
    totalsemua = totalkuekering + totalkuebasah
    
    print("\nTotal harus dibayar: Rp", totalsemua)
    uang = int(input("uang tunai pembeli: Rp "))
    kembalian = int(uang - totalsemua)
    print("kembalian :", kembalian)
    
    print("\n===============================")
    print("========= S T R U K  B E L I ========")
    print("=============================")
    print("nama\t\t:", pembeli)
    print("beli\t\t:", toples, kuekering, "(Rp", totalkuekering, ")")
    print("\t\t ", buah, kuebasah, "( Rp", totalkuebasah, ")")
    print("tagihan\t\t: Rp", totalsemua)
    print("dibayar\t\t: Rp", uang)
    print("kembalian\t: Rp", kembalian)
    print("====================================")
    print("====================================")
