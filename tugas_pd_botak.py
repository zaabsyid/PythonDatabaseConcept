
dataMahasiswa = []


def grade(nilaiTotal):
  if nilaiTotal >= 80 :
    print("Grade : A")
  elif nilaiTotal >= 70 <= 79 :
    print("Grade : B")
  elif nilaiTotal >= 60 <= 69 :
    print("Grade : C")
  elif nilaiTotal >= 50 <= 59 :
    print("Grade : D")
  else :
    print("Grade : E")


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
                addMahasiswa = input("Masukkan nama : ")
                addMataKuliah = input("Masukkan nama matakuliah :")
                dataMahasiswa.append([addMahasiswa, addMataKuliah])
                print("Berhasil menambahkan data")
            elif menu == 2:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j])
                    j+=1
            elif menu == 3:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIUBAH : "))
                menu3 = int(input("1. Update Mahasiswa \n2. Update Matakuliah\nPILIH MENU : "))
                if menu3 == 1:
                    namaBaru = input("MASUKKAN NAMA BARU : ")
                    dataMahasiswa[indeks-1][0] = namaBaru
                elif menu3 == 2:
                    namaMatkulBaru = input("MASUKKAN NAMA MATKUL BARU : ")
                    dataMahasiswa[indeks-1][1] = namaMatkulBaru
                print("Berhasil mengubah data")
            elif menu == 4:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIHAPUS : "))
                del(dataMahasiswa[indeks-1])
                print("Berhasil menghapus data")
            elif menu == 5:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DITAMBAH NILAI MATAKULIAHNYA : "))
                nilaiKehadiran = input("Masukan nilai kehadiran : ")
                nilaiPratikum = input("Masukan nilai pratikum : ")
                nilaiTugas = input("Masukan nilai tugas : ")
                nilaiUTS = input("Masukan nilai uts : ")
                nilaiUAS = input("Masukan nilai uas : ")
                nilaiTotal = int((float(nilaiKehadiran) * 0.2) + (float(nilaiPratikum) * 0.1) 
                + (float(nilaiTugas) * 0.2) + (float(nilaiUTS) * 0.25) + (float(nilaiUAS) * 0.25))
                print("Nilai Total : ", (nilaiTotal))
                grade(nilaiTotal)
                dataMahasiswa[indeks-1].append(nilaiTotal)
            elif menu == 6:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j][0])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DILIHAT NILAINYA : "))
                print(dataMahasiswa[indeks-1][2])
            elif menu == 7:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j][0])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIUBAH NILAINYA : "))
                nilaiBaru = int(input("Masukkan nilai baru : "))
                dataMahasiswa[indeks-1][2] = nilaiBaru
                print("Berhasil mengubah nilai")
            elif menu == 8:
                print("DAFTAR MAHASISWA")
                for j in range(len(dataMahasiswa)):
                    print(f"{j+1}.", dataMahasiswa[j][0])
                    j+=1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIHAPUS NILAINYA : "))
                del(dataMahasiswa[indeks-1][2])
                print("Berhasil menghapus nilai")
            else :
                break
    elif username == "keluar" :
      print("Stop Program")
      break
    else :
        print("Username atau Password Salah")