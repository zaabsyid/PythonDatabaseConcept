class kalkulator:


    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        print("Hasil tambah : ", self.angka1 + self.angka2)

    def kurang(self):
        print("Hasil kurang : ", self.angka1 - self.angka2)

    def bagi(self):
        print("Hasil bagi : ", self.angka1 / self.angka2)

    def kali(self):
        print("Hasil kali : ", self.angka1 * self.angka2)


angka1 = int(input("Angka 1 : "))
angka2 = int(input("Angka 2 : "))

kal = kalkulator(angka1, angka2)
kal.tambah()
kal.bagi()
kal.kali()
kal.kurang()