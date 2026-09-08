Batas_Nilai = (65, 100)
Nilai_Masuk = []
Lulus = []
Remedial = []

print("Sistem Pengelompokan Nilai Ujian Mahasiswa Prodi Sistem Informasi")
print("Ketik 'Selesai' untuk mengakhiri input nilai mahasiswa")
print("Ketik 'Hapus' untuk menghapus nilai mahasiswa yang Salah diinputkan")

while True:
    print("Jumlah Nilai Ujian Mahasiswa Saat Ini: ", len(Nilai_Masuk))
    Nilai = input("Masukkan Nilai Ujian Mahasiswa: ")
    if Nilai.lower() == "selesai":
        if len(Nilai_Masuk) < 5: 
            print("Jumlah nilai Ujian yang dimasukkan kurang dari 5, (baru", len(Nilai_Masuk), "), Tolong Masukan Nilai Ujian Kembali")
        elif len(Lulus) == 0:
            print("Tidak ada mahasiswa yang lulus, Tolong Masukan Nilai Ujian Kembali")
        elif len(Remedial) == 0:
            print("Tidak ada mahasiswa yang harus remedial, Tolong Masukan Nilai Ujian Kembali")
        else:
            print("Input Nilai Ujian Mahasiswa Selesai")
            break
        continue


    if Nilai.lower () == "hapus":
        if len (Nilai_Masuk) == 0:
            print("Tidak ada nilai yang dapat dihapus")
            continue

        print("Data Nilai Saat Ini:  ", Nilai_Masuk)
        Nilai_Hapus = input("Masukkan Nilai Ujian Mahasiswa yang ingin dihapus: ")

        if Nilai_Hapus in Nilai_Masuk:
            Nilai_Masuk.remove(Nilai_Hapus)
            if Nilai_Hapus in Lulus:
                Lulus.remove(Nilai_Hapus)
            elif Nilai_Hapus in Remedial:
                Remedial.remove(Nilai_Hapus)
                print("Nilai", Nilai_Hapus, "telah dihapus dari daftar.")
            else:
                print("Nilai", Nilai_Hapus, "tidak ditemukan dalam daftar.")
            continue

    Angka_Nilai = int(Nilai)
    Nilai_Masuk.append(Nilai)
    if  Angka_Nilai >= Batas_Nilai[0]:
        Lulus.append(Nilai)
        print("Nilai", Nilai, "telah dimasukkan ke dalam daftar Lulus.")
    else:
        Remedial.append(Nilai)
        print("Nilai", Nilai, "telah dimasukkan ke dalam daftar Remedial.")

print("Hasil AKhir Pengelompokan Nilai Ujian Mahasiswa Prodi Sistem Informasi")
print("Jumlah Nilai Ujian Mahasiswa yang dimasukkan: ", len(Nilai_Masuk))
print("Jumlah Mahasiswa yang Lulus: ", len(Lulus))
print("Jumlah Mahasiswa yang Harus Remedial: ", len(Remedial))