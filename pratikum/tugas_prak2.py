class singa:
    gen = "maung"

    def mengaung(self):
        print("singa mengaung")

class kucing(singa):
    def berjalan(self):
        return "Kucing Berjalan"

    def rawr(self):
        print(super().gen)

kucing1 = kucing()
print(kucing1.berjalan())
kucing1.rawr()
kucing1.mengaung()