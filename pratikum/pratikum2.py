class ayah:
    gen = 'gledek'

    def berjalan(self):
        return "Ayah gledek"

class anak(ayah):
    pass

    def namaAnak(self):
        print("Anton", super().gen)

anak1 = anak()
anak1.namaAnak()
print(anak1.berjalan())