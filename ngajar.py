import sys
# class Akun:
#     def __init__(self, username, password):
#         self.id = username
#         self.password = password
        
#     def __str__(self):
#         return f'User("{self.id}", "{self.password}")'
        
# class Admin(Akun):
#     def __init__(self, username, password):
#         super().__init__(username, password)
    
#     username = "Admin"
#     password = "Admin"
        
class Mahasiswa:
    def __init__(self, nama, matkul, nilai) -> None:
        self.nama = nama
        self.matkul = matkul
        self.nilai = nilai
    
    def __str__(self):
        return f'User("{self.nama}", "{self.matkul}", "{self.nilai}")'
        


mahasiswa_set = ()
mahasiswa_list = []
mahasiswa_tuple = tuple() #Imutable
mahasiswa_dictionary = {"mahasiswa" : [], "matkul" : [], "nilai" : []}

# idpass = []



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



def main():
    print('''Program Python Konsep Database
SILAHKAN LOGIN TERLEBIH DAHULU''')
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
        nomor = 0
        if menu == 1:
                addMahasiswa = input("Masukkan nama : ")
                addMataKuliah = input("Masukkan nama matakuliah :")
                mahasiswa_list.append(Mahasiswa(addMahasiswa, addMataKuliah, 0))
                mahasiswa_dictionary ["mahasiswa"].append(addMahasiswa)
                mahasiswa_dictionary ["matkul"].append(addMataKuliah)
                mahasiswa_dictionary ["nilai"].append(0)
                print("Berhasil menambahkan data")
                print(mahasiswa_list[0])
        elif menu == 2:
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor + 1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                for i in mahasiswa_set:
                    print(nomor + 1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                for i in mahasiswa_tuple:
                    print(nomor + 1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                print(mahasiswa_dictionary)
                
        elif menu == 3:
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("MASUKAN NOMOR MAHASISWA YANG INGIN DIUBAH : "))
                menu3 = int(input("1. Update Mahasiswa \n2. Update Matakuliah\nPILIH MENU : "))
                if menu3 == 1:
                    namaBaru = input("MASUKKAN NAMA BARU : ")
                    mahasiswa_list[indeks-1].nama = namaBaru
                elif menu3 == 2:
                    namaMatkulBaru = input("MASUKKAN NAMA MATKUL BARU : ")
                    mahasiswa_list[indeks-1].matkul = namaMatkulBaru
                print("Berhasil mengubah data")
        elif menu == 4:
                print("Menu 4")
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("MASUKAN NOMOR MAHASISWA YANG INGIN DIHAPUS : "))
                del(mahasiswa_list[indeks-1])
                print("Berhasil menghapus data")
        elif menu == 5:
                print("Menu 5")
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("MASUKAN NOMOR MAHASISWA YANG INGIN DITAMBAH NILAI MATAKULIAHNYA : "))
                nilaiKehadiran = input("Masukan nilai kehadiran : ")
                nilaiPratikum = input("Masukan nilai pratikum : ")
                nilaiTugas = input("Masukan nilai tugas : ")
                nilaiUTS = input("Masukan nilai uts : ")
                nilaiUAS = input("Masukan nilai uas : ")
                nilaiTotal = int((float(nilaiKehadiran) * 0.2) + (float(nilaiPratikum) * 0.1) 
                + (float(nilaiTugas) * 0.2) + (float(nilaiUTS) * 0.25) + (float(nilaiUAS) * 0.25))
                print("Nilai Total : ", (nilaiTotal))
                grade(nilaiTotal)
                mahasiswa_list[indeks-1].nilai = nilaiTotal
        elif menu == 6:
                print("Menu 6")
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DILIHAT NILAINYA : "))
                print(mahasiswa_list[indeks-1].nilai)
        elif menu == 7:
                print("Menu 7")
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIUBAH NILAINYA : "))
                nilaiBaru = int(input("Masukkan nilai baru : "))
                mahasiswa_list[indeks-1] = nilaiBaru
                print("Berhasil mengubah nilai")
        elif menu == 8:
                print("Menu 8")
                print("DAFTAR MAHASISWA")
                for i in mahasiswa_list:
                    print(nomor+1, "Nama Mahasiswa :",i.nama, "| Nama Matakuliah :",i.matkul)
                    nomor += 1
                indeks = int(input("PILIH MAHASISWA YANG INGIN DIHAPUS NILAINYA : "))
                mahasiswa_list[indeks-1].nilai = 0
                print("Berhasil menghapus nilai")
        elif menu == 9:
            break
            
while (True):
        menuu = int(input('''1. login\n2. keluar\nMasukan nomor perintah : '''))
        if menuu == 1:    
            print("Masukan username dan password")
            username = input("NAMA : ")
            password = input("PASSWORD : ")
            if username == "admin" and password == "admin":
                print("Berhasil Login")
                print("Selamat Datang", username)
                main()
            else:
                print("Id atau Password Kamu Salah")
        elif menuu == 2:
            break

        
    # if menu == 2:
    #     print("Masukan username dan password")
    #     regusername = input("NAMA : ")
    #     regpassword = input("PASSWORD : ")
    #     idpass.append(Akun(regusername, regpassword))
    
    # if menu == 3:
    #     for i in idpass:
    #         print(i.id)
    


    
    
    



        
       
    