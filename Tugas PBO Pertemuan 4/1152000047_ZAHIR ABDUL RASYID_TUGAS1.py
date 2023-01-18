class Hero:

    def __init__(self, n, ba):
        self.nama = n
        self.ba = int(ba)
        self.item = []

    def tambahItem(self, item):
        self.item.append(item)

class Item:

    def __init__(self, n, rd):
        self.nama = n
        self.rawDmg = int(rd)

class Lord:
    def __init__(self, n, hp):
        self.nama = n
        self.hp = int(hp)

while(True):
    jmlhHero = int(input("Masukan Jumlah Hero : "))
    saveHero = []
    i = 1
    if (jmlhHero > 5):
        print("Maksimal hero adalah 5")
    else:
        while(i <= jmlhHero):
            print(f"<Hero {i}>")
            masukan = input()
            listMasukan = masukan.split("%")
            saveHero.append(Hero(listMasukan[0],listMasukan[1]))
            i += 1


        jmlhItem = int(input("Masukan jumlah item : "))
        saveItem = []
        i = 1
        while(i <= jmlhItem):
            print(f"<Item {i}>")
            masukan = input()
            listMasukan = masukan.split(";")
            saveItem.append(Item(listMasukan[0],listMasukan[1]))
            i += 1
        
        saveLord = []
        print("!! Lord Respawn !!")
        print("<Lord>")
        masukan = input()
        listMasukan = masukan.split("*")
        saveLord.append(Lord(listMasukan[0],listMasukan[1]))
        print("// Five Seconds 'til the Lord reach the battlefiled, smash him. //")
        while (True):
            perintah = input()
            listPerintah = perintah.split(";")
            if listPerintah[0] == "PILIH ITEM" :
                for j in range(len(saveHero)):
                    if (saveHero[j].nama == listPerintah[1]):
                        for k in range(len(saveItem)):
                            if (saveItem[k].nama == listPerintah[2]):
                                print(f"{saveHero[j].nama} berhasil memakai {saveItem[k].nama} !")
                                saveHero[j].tambahItem(saveItem[k])

            elif listPerintah[0] == "GANTI ITEM" :
                for j in range(len(saveHero)):
                    if (saveHero[j].nama == listPerintah[1]):
                        for k in range(len(saveItem)):
                            if (saveItem[k].nama == listPerintah[2]):
                                print(saveHero[j].nama, saveItem[k].nama)

            else:
                i = 0
                while True:
                    if saveLord[0].hp != 0 :
                        saveLord[0].hp = saveLord[0].hp - saveItem[i].rawDmg
                        print(f'''
{saveHero[i].nama} menyerang {saveLord[0].nama} dengan senjata {saveItem[i].nama} 
sebesar {saveItem[i].rawDmg}, HP {saveLord[0].nama} sekarang {saveLord[0].hp}''')
                        i += 1
                    else:
                        break