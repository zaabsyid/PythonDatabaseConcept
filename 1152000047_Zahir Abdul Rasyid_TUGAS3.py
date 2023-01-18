class Hero:
    def __init__(self, nama, diamond, bp, tiket, role):
        self.nama = nama
        self.diamond = int(diamond)
        self.bp = int(bp)
        self.tiket = int(tiket)
        self.role = role

    def get_hero_description (self):
        return self.__nama, self.__diamond, self.__bp, self.__tiket

class Magic (Hero):
    def __init__(self, nama, diamond, bp, tiket, role, magicPower):
        self.magicPower = int(magicPower)
        super().__init__(nama, diamond, bp, tiket, role)

    def get_hero_description (self):
        print("Nama hero: {} \t\nDiamond: {} \t\nBP: {} \t\nTiket: {} \t\nMagic Power: {}".format(
            self.nama,
            self.diamond,
            self.bp,
            self.tiket,
            self.magicPower
            )
        )

class Physical (Hero):
    def __init__(self, nama, diamond, bp, tiket, role, physicalPower):
        self.physicalPower = int(physicalPower)
        super().__init__(nama, diamond, bp, tiket, role)

    def get_hero_description (self):
        print("Nama hero: {} \t\nDiamond: {} \t\nBP: {} \t\nTiket: {} \t\nPhysical Power: {}".format(
            self.nama,
            self.diamond,
            self.bp,
            self.tiket,
            self.physicalPower
            )
        )

class Support (Hero):
    def __init__(self, nama, diamond, bp, tiket, role, hpHealing):
        self.hpHealing = int(hpHealing)
        super().__init__(nama, diamond, bp, tiket, role)

    def get_hero_description (self):
        print("Nama hero: {} \t\nDiamond: {} \t\nBP: {} \t\nTiket: {} \t\nHp Healing: {}".format(
            self.nama,
            self.diamond,
            self.bp,
            self.tiket,
            self.hpHealing
            )
        )

class Role:
    def __init__(self, nama):
        self.nama = nama
        self.kumpulan_hero = []

    def tambah_kumpulan_hero(self, kumpulan_hero):
        self.kumpulan_hero.append(kumpulan_hero)


class Akun:
    def __init__(self, kumpulan_role):
        self.kumpulan_role = kumpulan_role


jungler = Role("Jungler01")
offlaner = Role("Offliner01")
midlaner = Role("Midlaner01")
roamer = Role("Roamer01")

addHero = []
saveKumpulanHeroJungler = []
saveKumpulanHeroOffliner = []
saveKumpulanHeroMidlaner = []
saveKumpulanHeroRoamer = []
saveRole = []

while True:
    perintah = input(('''\n
Selamat Datang di Mobile Legends Bang Bang
Silahkan masukan perintah!
Perintah anda: '''))
    listPerintah = perintah.split(" ")

    if perintah == "LIST":
        print("Jungler01")
        for j in range(len(saveKumpulanHeroJungler)):
            print("-", saveKumpulanHeroJungler[j].nama)
            j+=1
        print("Offliner01")
        for j in range(len(saveKumpulanHeroOffliner)):
            print("-", saveKumpulanHeroOffliner[j].nama)
            j+=1
        print("Midlaner01")
        for j in range(len(saveKumpulanHeroMidlaner)):
            print("-", saveKumpulanHeroMidlaner[j].nama)
            j+=1
        print("Roamer01")
        for j in range(len(saveKumpulanHeroRoamer)):
            print("-", saveKumpulanHeroRoamer[j].nama)
            j+=1
        

    elif listPerintah[0] == "ADD":
        if listPerintah[7] == "Magic":
            addHero.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            addHero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                saveKumpulanHeroJungler.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Offliner01":
                saveKumpulanHeroOffliner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Midlaner01":
                saveKumpulanHeroMidlaner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Roamer01":
                saveKumpulanHeroRoamer.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
        elif listPerintah[7] == "Physical":
            addHero.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            saveKumpulanHeroJungler.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            addHero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                saveKumpulanHeroJungler.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Offliner01":
                saveKumpulanHeroOffliner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Midlaner01":
                saveKumpulanHeroMidlaner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Roamer01":
                saveKumpulanHeroRoamer.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
        elif listPerintah[7] == "Support":
            addHero.append(Support(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            addHero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                saveKumpulanHeroJungler.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Offliner01":
                saveKumpulanHeroOffliner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Midlaner01":
                saveKumpulanHeroMidlaner.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
            elif listPerintah[2] == "Roamer01":
                saveKumpulanHeroRoamer.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[7], listPerintah[8]))
    elif listPerintah[0] == "SEARCH":
        for j in range(len(addHero)):
            if (addHero[j].nama == listPerintah[2]):
                if (addHero[j].role == "Magic"):
                    print("Hero Ditemukan")
                    print("Hero", addHero[j].role)
                    print("Nama hero:", addHero[j].nama)
                    print("Diamond:", addHero[j].diamond)
                    print("BP:", addHero[j].bp)
                    print("Tiket:", addHero[j].tiket)
                    print("Magic Power:", addHero[j].magicPower)
                elif (addHero[j].role == "Physical"):
                    print("Hero Ditemukan")
                    print("Hero", addHero[j].role)
                    print("Nama hero:", addHero[j].nama)
                    print("Diamond:", addHero[j].diamond)
                    print("BP:", addHero[j].bp)
                    print("Tiket:", addHero[j].tiket)
                    print("Physical Power:", addHero[j].physicalPower)
                elif (addHero[j].role == "Support"):
                    print("Hero Ditemukan")
                    print("Hero", addHero[j].role)
                    print("Nama hero:", addHero[j].nama)
                    print("Diamond:", addHero[j].diamond)
                    print("BP:", addHero[j].bp)
                    print("Tiket:", addHero[j].tiket)
                    print("Hp Healing:", addHero[j].hpHealing)
            else:
                print(f"Hero dengan nama {addHero[j].nama} tidak ditemukan")

    elif listPerintah[1] == "ROLE":
        print(f"Role baru berhasil ditambahkan\t\nNama: {listPerintah[2]}\t\nJenis: {listPerintah[3]}")
    elif perintah == "EXIT":
        print("Selesai, Akun MLBB dimatikan")
        break
    else:
        print("Perintah tidak dikenali")