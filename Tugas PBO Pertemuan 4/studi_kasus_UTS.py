class mahasiswa:
    def __init__(self, nrp, nama, umur, jk, alamat):
        self.nrp = int(nrp)
        self.nama = nama
        self.umur = int(umur)
        self.jk = jk
        self.alamat = alamat

class dosen:
    def __init__(self, nid, nama, umur, jk, alamat):
        self.nrp = int(nid)
        self.nama = nama
        self.umur = int(umur)
        self.jk = jk
        self.alamat = alamat

class matakuliah:
    def __init__(self, idMatkul, nama_matkul, hari, jam):
        self.id_matkul = int(idMatkul)
        self.nama_matkul = nama_matkul
        self.hari = hari
        self.jam = int(jam)

while(True):
    menu = int(input('''
PROGRAM INPUT DATA
SILAHKAN PILIH :
1. INPUT MAHASISWA
2. INPUT DOSEN
3. INPUT MATAKULIAH
4. CETAK
5. EXIT
PILIH : '''))
    if menu == 1:
        jmlhMahasiswa = int(input("Masukan Jumlah Mahasiswa : "))
        saveMahasiswa = []
        i = 1
        while(i <= jmlhMahasiswa):
            print(f"<Mahasiswa {i}>")
            masukan = input("Masukan nrp/nama/umur/jk/alamat : ")
            listMasukan = masukan.split("/")
            saveMahasiswa.append(mahasiswa(listMasukan[0],listMasukan[1],listMasukan[2],listMasukan[3],listMasukan[4]))
            i += 1
        print("Berhasil terinput")

    elif menu == 2:
        jmlhDosen = int(input("Masukan Jumlah Dosen : "))
        saveDosen = []
        i = 1
        while(i <= jmlhDosen):
            print(f"<Dosen {i}>")
            masukan = input("Masukan nrp/nama/umur/jk/alamat : ")
            listMasukan = masukan.split("/")
            saveDosen.append(dosen(listMasukan[0],listMasukan[1],listMasukan[2],listMasukan[3],listMasukan[4]))
            i += 1
        print("Berhasil terinput")

    elif menu == 3:
        jmlhMatakuliah = int(input("Masukan Jumlah Matakuliah : "))
        saveMatakuliah = []
        i = 1
        while(i <= jmlhDosen):
            print(f"<Matakuliah {i}>")
            masukan = input("Masukan idMatkul/nama/hari/jam : ")
            listMasukan = masukan.split("/")
            saveMatakuliah.append(matakuliah(listMasukan[0],listMasukan[1],listMasukan[2],listMasukan[3]))
            i += 1
        print("Berhasil terinput")

    elif menu == 4:
        menuCetak = int(input('''
SILAHKAN PILIH YANG INGIN DICETAK:
1. Data Mahasiswa
2. Data Dosen
3. Data Matakuliah
PILIH : '''))
        if menuCetak == 1:
            i = 0
            j = 1
            while(True):
                if j <= jmlhMahasiswa:
                    print(f'''
NRP : {saveMahasiswa[i].nrp}
NAMA : {saveMahasiswa[i].nama}
UMUR : {saveMahasiswa[i].umur}
JK : {saveMahasiswa[i].jk}
ALAMAT : {saveMahasiswa[i].alamat}''')
                    print("="*50)
                    i += 1
                    j += 1
                else:
                    break
        
        elif menuCetak == 2:
            i = 0
            j = 1
            while(True):
                if j <= jmlhDosen:
                    print(f'''
NRP : {saveDosen[i].nid}
NAMA : {saveDosen[i].nama}
UMUR : {saveDosen[i].umur}
JK : {saveDosen[i].jk}
ALAMAT : {saveDosen[i].alamat}''')
                    print("="*50)
                    i += 1
                    j += 1
                else:
                    break

        elif menuCetak == 3:
            i = 0
            j = 1
            while(True):
                if j <= jmlhMatakuliah:
                    print(f'''
id Matakuliah : {saveMatakuliah[i].idMatakuliah}
NAMA Matakuliah : {saveMatakuliah[i].nama}
Hari : {saveMatakuliah[i].hari}
Jam : {saveMatakuliah[i].jam}''')
                    print("="*50)
                    i += 1
                    j += 1
                else:
                    break
        
    else:
        break