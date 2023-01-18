class Hero:
    def __init__(self, nama, diamond, bp, tiket):
        self.nama = nama
        self.diamond = int(diamond)
        self.bp = int(bp)
        self.tiket = int(tiket)


class Magic (Hero):
    def __init__(self, nama, diamond, bp, tiket, magicPower):
        self.magicPower = int(magicPower)
        super().__init__(nama, diamond, bp, tiket)

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
    def __init__(self, nama, diamond, bp, tiket, physicalPower):
        self.physicalPower = int(physicalPower)
        super().__init__(nama, diamond, bp, tiket)

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
    def __init__(self, nama, diamond, bp, tiket, hpHealing):
        self.hpHealing = int(hpHealing)
        super().__init__(nama, diamond, bp, tiket)

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

class Akun:
    def __init__(self, kumpulan_role):
        self.kumpulan_role = kumpulan_role

jungler = Role("Jungler01")
offlaner = Role("Offliner01")
midlaner = Role("Midlaner01")
roamer = Role("Roamer01")

save_hero = []
save_hero_jungler = []
save_hero_offliner = []
save_hero_midlaner = []
save_hero_roamer = []
saveRole = []

while True:
    perintah = input("Selamat Datang di Mobile Legends Bang Bang\t\nSilahkan masukan perintah!\t\nPerintah anda:")
    listPerintah = perintah.split(" ")

    if perintah == "LIST":
        print("Jungler01")
        print("-", save_hero_jungler)
        print("Offliner01")
        print("-", save_hero_offliner)
        print("Midlaner01")
        print("-", save_hero_midlaner)
        print("Roamer01")
        print("-", save_hero_roamer)
        

    elif listPerintah[0] == "ADD":
        if listPerintah[7] == "Magic":
            save_hero.append(Magic(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            save_hero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                save_hero_jungler.append(listPerintah[3])
            elif listPerintah[2] == "Offliner01":
                save_hero_offliner.append(listPerintah[3])
            elif listPerintah[2] == "Midlaner01":
                save_hero_midlaner.append(listPerintah[3])
            elif listPerintah[2] == "Roamer01":
                save_hero_roamer.append(listPerintah[3])
        elif listPerintah[7] == "Physical":
            save_hero.append(Physical(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            save_hero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                save_hero_jungler.append(listPerintah[3])
            elif listPerintah[2] == "Offliner01":
                save_hero_offliner.append(listPerintah[3])
            elif listPerintah[2] == "Midlaner01":
                save_hero_midlaner.append(listPerintah[3])
            elif listPerintah[2] == "Roamer01":
                save_hero_roamer.append(listPerintah[3])
        elif listPerintah[7] == "Support":
            save_hero.append(Support(listPerintah[3], listPerintah[4], listPerintah[5], listPerintah[6], listPerintah[8]))
            print("Hero baru berhasil ditambahkan pada role", listPerintah[2])
            print("Hero", listPerintah[7])
            save_hero[0].get_hero_description()
            if listPerintah[2] == "Jungler01":
                save_hero_jungler.append(listPerintah[3])
            elif listPerintah[2] == "Offliner01":
                save_hero_offliner.append(listPerintah[3])
            elif listPerintah[2] == "Midlaner01":
                save_hero_midlaner.append(listPerintah[3])
            elif listPerintah[2] == "Roamer01":
                save_hero_roamer.append(listPerintah[3])
    elif listPerintah[0] == "SEARCH":
        for j in range(len(save_hero)):
            if (save_hero[j].nama == listPerintah[2]):
                print("Hero Ditemukan")
                print("Hero Magic")
                print("Nama hero:", save_hero[j].nama)
                print("Diamond:", save_hero[j].diamond)
                print("BP:", save_hero[j].bp)
                print("Tiket:", save_hero[j].tiket)
                print("Magic Power:", save_hero[j].magicPower)
            else:
                print("Hero dengan nama", save_hero[j].nama, "tidak ditemukan")

    elif listPerintah[1] == "ROLE":
        print("Role baru berhasil ditambahkan")
        print("Nama:", listPerintah[2])
        print("Jenis:", listPerintah[3])
    elif perintah == "EXIT":
        print("Selesai, Akun MLBB dimatikan")
        break
    else:
        print("Perintah tidak dikenali")