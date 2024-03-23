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