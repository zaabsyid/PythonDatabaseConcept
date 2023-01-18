class Penjual:
    def __init__(self, nama, umur, jk, alamat):
        self.nama = nama
        self.umur = int(umur)
        self.jk = jk
        self.alamat = alamat

class Pembeli:
    def __init__(self, nama, umur, jk, alamat):
        self.nama = nama
        self.umur = int(umur)
        self.jk = jk
        self.alamat = alamat
        self. barang = []
    
    def tambahBarangYGDibeli(self, barang):
        self.barang.append(barang)

class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = int(stok)

class Keranjang (Pembeli):
    def __init__(self, nama, umur, jk, alamat, isi_keranjang):
        self.isi_keranjang = isi_keranjang
        super().__init__(nama, umur, jk, alamat)

pakKomar = Penjual("Pak Qomar", 35, "L", "Muncul")
savePembeli = []
saveBarang = []


while(True):
    menu = int(input('''
PROGRAM JUAL BELI DI TOKO PAK QOMAR
SILAHKAN PILIH :
1. INPUT BARANG
2. INPUT DATA PEMBELI
3. MASUKAN BARANG KE KERANJANG
4. CETAK BARANG YANG DIJUAL
5. CETAK BARANG DI KERANJANG
6. CETAK DAFTAR PEMBELI
7. EXIT
PILIH : '''))

    if menu == 1 :
        print("Silahkan input barang : ")
        barang = input("Masukan nama barang/harga/stok : ")
        listBarang = barang.split("/")
        saveBarang.append(Barang(listBarang[0],listBarang[1],listBarang[2]))
    elif menu == 2 :
        print("Silahkan input data pembeli : ")
        pembeli = input("Masukan nama/umur/jk/alamat : ")
        listPembeli = pembeli.split("/")
        savePembeli.append(Pembeli(listPembeli[0],listPembeli[1],listPembeli[2],listPembeli[3]))
        print("Barang berhasil di input")
    elif menu == 3 :
        print("Masukan nama pembeli/nama barang yang ingin dibeli : ")
        perintah = input()
        listPerintah = perintah.split("/")
        for j in range(len(savePembeli)):
            if (savePembeli[j].nama == listPerintah[1]):
                for k in range(len(saveBarang)):
                    if (saveBarang[k].nama == listPerintah[2]):
                        print(f"{saveBarang[j].nama} menambahkan {saveBarang[k].nama} ke keranjang!")
                        saveBarang[j].tambahItem(saveBarang[k])
    elif menu == 4 :
        print("Barang barang yang berada di gudang")
        for j in range(len(saveBarang)):
            print("-", saveBarang[j].nama)
            j+=1
    elif menu == 5 :
        print("Barang barang yang berada di keranjang")
        for j in range(len(saveBarang)):
            print("-", saveBarang[j].nama)
            j+=1
    elif menu == 6 :
        print("DAFTAR PEMBELI")
        for j in range(len(savePembeli)):
            print("-", savePembeli[j].nama)
            j+=1
    elif menu == 7 :
        print("EXIT")
        break
    else:
        print("Masukan perintah dengan benar")