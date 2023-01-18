from abc import ABC, abstractclassmethod

class Lukisan (ABC):

    @abstractclassmethod
    def warna(self):
        print("Sub class ini harus menggunakan fungsi warna")

class LukisanAbstrak(Lukisan):
    def warna(self):
        print("Dominasi warna lukisan adalah merah dan hijau")

lukisan = LukisanAbstrak()
lukisan.warna()