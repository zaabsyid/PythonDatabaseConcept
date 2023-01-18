#Konsep enkapsulasi
class uang:
    def __init__(self,nominal):
        self.__nominal = nominal #private variable

    def setNominal(self, nominalBaru): #setter
        self.__nominal = nominalBaru

    def _belanja(self,totalBelanja):
        print("Terima kasih. Sisa uang anda adalah: ")
        print(self._nominal - totalBelanja)

    def getNominal(self): #nominal
        return self.__nominal

class koin(uang):
    def __init__(self, bahan):
        self.bahan = bahan

    def beli(self, totalBeli) :
        print("Terima kasih. Sisa uang anda adalah : ")
        print(self._nominal - totalBeli)

#uang1 = uang(10000)
#uang1._belanja(5000)
#koin1 = koin("logam")
#koin1._nominal = 1000
#koin1.beli(500)

uang1 = uang(1000)
print(uang1.getNominal())

uang1.__nominal = 5000
print(uang1.getNominal())

uang1.setNominal(5000)
print(uang1.getNominal())