class Hero:
    jumlahHero = 0

    def __init__(self, n, r, h, m):
        self.nama = n
        self.role = r
        self.hp = h
        self.mana = m
        Hero.jumlahHero += 1

    #Metode class
    @classmethod
    def showJumlahHero(cls):
        print(cls.jumlahHero)

def landOfDawn():
    saveHero = []
    totalHero = int(input("Masukan jumlah hero : "))
    
    for i in range(totalHero):
        print("Hero ke-", Hero.jumlahHero + 1)
        print("Masukan atribut hero: nama;role;hp;mana")
        masukan = input()
        listMasukan = masukan.split(";")
        saveHero.append(Hero(listMasukan[0],listMasukan[1],listMasukan[2],listMasukan[3]))
    
    print(Hero.jumlahHero)
    print(saveHero[0].jumlahHero)

    Hero.showJumlahHero()
    saveHero[0].showJumlahHero()

landOfDawn()