from abc import ABC, abstractclassmethod


class ATM(ABC):

    @abstractclassmethod
    def cekSaldo(self):
        pass
    
    @abstractclassmethod
    def tambahSaldo(self):
        pass

    @abstractclassmethod
    def tarikSaldo(self):
        pass

class nasabah(ATM):
    def __init__(self):
        self.saldo = 10000

    def cekSaldo(self):
        print("Saldo anda adalah : ", self.saldo)
    
    def tambahSaldo(self):
        tambah_saldo = int(input("Masukan nominal yang ingin ditambahkan : "))
        self.saldo = self.saldo + tambah_saldo
        print("Saldo anda : ", self.saldo)

    def tarikSaldo(self):
        tarik_saldo = int(input("Masukan nominal yang ingin ditarik : "))
        self.saldo = self.saldo - tarik_saldo
        print("Saldo anda : ", self.saldo)

while True:
    menu = int(input('''
Selamat Datang di Program ATM
Silahkan pilih menu
1. Cek Saldo
2. Tambah Saldo
3. Tarik Saldo
4. Exit
Pilih : '''))
    nasabah1 = nasabah()
    if menu == 1:
        print("Cek Saldo")
        nasabah1.cekSaldo()
    elif menu == 2:
        print("Tambah Saldo")
        nasabah1.tambahSaldo()
    elif menu == 3:
        print("Tarik Saldo")
        nasabah1.tarikSaldo()
    elif menu == 4:
        print("Exit")
        break
    else:
        print("Masukan angka sesuai yang ada di menu")