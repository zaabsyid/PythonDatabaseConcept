
dataMahasiswa = []
dataMataKuliah = []




print('''Program Python Konsep Database
SILAHKAN LOGIN TERLEBIH DAHULU''')
while(True):
    username = input("NAMA : ")
    password = input("PASSWORD : ")

    if username == "admin" and password == "admin":
        print("Berhasil Login")
        while(True):
            menu = int(input('''
SILAHKAN PILIH :
1. Create / Tambah data Mahasiswa dan Mata kuliah (C)
2. Read / Lihat data Mahasiswa dan Mata kuliah (R)
3. Update / Rename data Mahasiswa dan Mata kuliah (U)
4. Delete / Hapus data Mahasiswa dan Mata kuliah (D)
5. Tambah komponen Penilaian pada mata Kuliah
6. Lihat Nilai Mahasiswa
7. Update Nilai Mahasiswa
8. Delete Nilai Mahasiswa
9. Keluar
PILIH MENU : '''))
            if menu == 1:
                print("Menu 1")
                menu1 = int(input("1. Tambah Mahasiswa \n2. Tambah Matakuliah\nPILIH MENU : "))
                if menu1 == 1:
                    addMahasiswa = input("Tambah mahasiswa\nMasukkan nama : ")
                    dataMahasiswa.append(addMahasiswa)
                elif menu1 == 2:
                    addMataKuliah = input("Tambah matakuliah\nMasukkan nama matakuliah :")
                    dataMataKuliah.append(addMataKuliah)
                print("Berhasil menambahkan data")
            elif menu == 2:
                print("Menu 2")
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print("-", dataMahasiswa[j])
                    j+=1
                print("\n\nDAFTAR MATAKULIAH")
                for k in range(len(dataMataKuliah)):
                    print("-", dataMataKuliah[k])
                    k+=1
            elif menu == 3:
                print("Menu 3")
                menu3 = int(input("1. Update Mahasiswa \n2. Update Matakuliah\nPILIH MENU : "))
                if menu3 == 1:
                    print(dataMahasiswa)
                    indeks = int(input("PILIH INDEKS MAHASISWA YANG INGIN DIUBAH NAMANYA : "))
                    namaBaru = input("MASUKKAN NAMA BARU : ")
                    dataMahasiswa[indeks] = namaBaru
                elif menu3 == 2:
                    print(dataMataKuliah)
                    indeks = int(input("PILIH INDEKS MATKUL YANG INGIN DIUBAH NAMANYA : "))
                    namaMatkulBaru = input("MASUKKAN NAMA MATKUL BARU : ")
                    dataMataKuliah[indeks] = namaMatkulBaru
                print("Berhasil mengubah data")
            elif menu == 4:
                print("Menu 4")
                menu4 = int(input("1. Hapus Mahasiswa \n2. Hapus Matakuliah\nPILIH MENU : "))
                if menu4 == 1:
                    print(dataMahasiswa)
                    indeks = int(input("PILIH INDEKS MAHASISWA YANG INGIN DIHAPUS : "))
                    del(dataMahasiswa[indeks])
                elif menu4 == 2:
                    print(dataMataKuliah)
                    indeks = int(input("PILIH INDEKS MATAKULIAH YANG INGIN DIHAPUS : "))
                    del(dataMataKuliah[indeks])
                print("Berhasil menghapus data")
            elif menu == 5:
                print("Menu 5")
            elif menu == 6:
                print("Menu 6")
            elif menu == 7:
                print("Menu 7")
            elif menu == 8:
                print("Menu 8")
            else :
                print("Stop Program")
                break
    else :
        print("Username atau Password Salah")