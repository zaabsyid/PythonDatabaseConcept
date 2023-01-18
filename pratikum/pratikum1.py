class orang :
    

    #constructor
    def __init__(self, nama, jk):
        self.nama = nama
        self.jk = jk
    
    def berjalan(self):
        print(self.nama, "Sedang berjalan")

orang1 = orang("Budi", "L")
orang2 = orang("Putri", "P")
orang1.berjalan()
orang2.berjalan()

#print(orang1.nama)

#orang1.berjalan()