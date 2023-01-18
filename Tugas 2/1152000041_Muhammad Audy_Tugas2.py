#Nama : Muhammad Audy
#NRP : 1152000041
#Tugas 2


import random
import os

class Hero:
    def __init__(self, n, ba, hp, skill, pasif):
        self.nama = n
        self.basicAttack = int(ba)
        self.hp = int(hp)
        self.skill = skill
        self.pasif = pasif
        self.item = []

    def tambahItem(self, item):
        self.item.append(item)

class Magical(Hero):
    def __init__(self, n, ba, hp, skill, mp, pd, pasif):
        self.magicPower = int(mp)
        self.physicalDefense = int(pd)
        super().__init__(n, ba, hp, skill, pasif)

class Physical(Hero):
    def __init__(self, n, ba, hp, skill, pa, md, pasif):
        self.physicalAttack = int(pa)
        self.magicDefense = int(md)
        super().__init__(n, ba, hp, skill, pasif)

class Item:
    def __init__(self, n, dmg):
        self.nama = n
        self.damage = int(dmg)

class Skill:
    def __init__(self, n, attck, deff):
        self.nama = n
        self.attack = int(attck)
        self.defense = int(deff)


save_item_dari_input_masukan = []

mystic_gush = Skill("Mystic Gush", 10, 80)
deadly_magic = Skill("Deadly Magic", 20, 70)
order_n_chaos = Skill("Order & Chaos", 30, 60)
violet_reqiem = Skill("Violet Reqiem", 40, 50)
zaman_force = Skill("Zaman Force", 40, 50)
vegeane_flame = Skill("Vegeane Flame", 60, 30)
feathered_air_strike = Skill("Fearhered Air Strike", 70, 20)
bast_feast = Skill("Bats Feast", 80, 10)
triple_sweep = Skill("Triple Sweep", 20, 10)
alecto = Skill("Alecto : Final Blow", 30, 15)
the_way_of_dragon = Skill("The Way of Dragon", 40, 20)
pasif = Skill("Pasif", 200, 0)

gord = Magical("Gord", 100, 800, mystic_gush, 100, 100, 0)
harley = Magical("Harley", 100, 700, deadly_magic, 200, 200, 0)
lunox = Magical("Lunox", 100, 600, order_n_chaos, 300, 300, pasif)
guinevere = Magical("Guinevere", 100, 500, violet_reqiem, 400, 400, 0)
harith = Magical("Harith", 100, 400, zaman_force, 500, 500, 0)
valir = Magical("Valir", 100, 300, vegeane_flame, 600, 600, 0)
pharsa = Magical("Pharsa", 100, 200, feathered_air_strike, 700, 700, pasif)
cecillion = Magical("Cecillion", 100, 100, bast_feast, 800, 800, 0)

list_hero_magic = [gord, harley, lunox, guinevere, harith, valir, pharsa, cecillion]

saber = Physical("Saber", 100, 400, triple_sweep, 400, 400, pasif)
benedetta = Physical("Benedetta", 100, 300, alecto, 500, 500, pasif)
chou = Physical("Chou", 100, 500, the_way_of_dragon, 40, 20, pasif)


hero_random_magic1 = (random.choice(list_hero_magic))
hero_random_magic2 = (random.choice(list_hero_magic))
hero_random_magic3 = (random.choice(list_hero_magic))

save_hero_magic_random1 = hero_random_magic1
save_hero_magic_random2 = hero_random_magic2
save_hero_magic_random3 = hero_random_magic3

while(True):
    print("selamat datang di pertempuran 3 vs 3")
    print("pilihan :")
    print("1. lihat daftar hero magic")
    print("2. lihat daftar hero pyhical")
    print("3. lihat skill hero magic")
    print("4. lihat skill hero physical")
    print("5. pilih hero & buat item")
    print("6. beli item")
    print("7. battle")
    print("8. keluar")
    print("pilih menu: ")
    pilih_menu = int(input())
    if pilih_menu == 1:
        print("#########")
        print("Daftar nama hero magic")
        print("$$$$$$$$$")
        print("gord")
        print("harley")
        print("lunox")
        print("guinevere")
        print("harith")
        print("valir")
        print("pharsa")
        print("cecillion")
        print("#########")
        os.system("pause")
    elif pilih_menu == 2:
        print("menu 2")
        print("#########")
        print("Daftar nama hero magic")
        print("$$$$$$$$$")
        print("saber")
        print("benedetta")
        print("chou")
        print("#########")
        os.system("pause")
    elif pilih_menu == 3:
        print("#########")
        print("daftar nama skill hero magic")
        print("$$$$$$$$$")
        print("gord memiliki skill ", gord.skill.nama)
        print("harley memiliki skill ", harley.skill.nama)
        print("lunox memiliki skill order n chaos", gord.skill.nama)
        print("lunox memiliki skill pasif", lunox.pasif.nama)
        print("guinevere memiliki skill violet reqiem", guinevere.skill.nama)
        print("harith memiliki skill zaman force", harith.skill.nama)
        print("valir memiliki skill fegeane flame", valir.skill.nama)
        print("pharsa memiliki skill feathered air strike", pharsa.skill.nama)
        print("pharsa memiliki skill pasif", pharsa.pasif.nama)
        print("cecilion memiliki skill bast feast", cecillion.skill.nama)
        print("#########")
        os.system("pause")
    elif pilih_menu == 4:
        print("#########")
        print("daftar nama skill hero physical")
        print("$$$$$$$$$")
        print("saber memiliki skill triple sweap", saber.skill.nama)
        print("saber memiliki skill pasif", saber.pasif.nama)
        print("benedetta memiliki skill alecto", benedetta.skill.nama)
        print("benedetta memiliki skill pasif", benedetta.pasif.nama)
        print("chou memiliki skill the way of the dragon", chou.skill.nama)
        print("chou memiliki skill pasif", chou.pasif.nama)
        print("#########")
        os.system("pause")
    elif pilih_menu == 5:
        print("3 Magic VS 3 Physical")
        print(save_hero_magic_random1.nama)
        print("vs")
        print("saber")
        print("3 Magic VS 3 Physical")
        print(save_hero_magic_random2.nama)
        print("vs")
        print("benedetta")
        print("3 Magic VS 3 Physical")
        print(save_hero_magic_random3.nama)
        print("vs")
        print("chou")
        os.system('pause')

        print("buat item dan tambahkan kepada hero")
        print("membuat beberapa objek item sampai berhenti")
        i = 1
        while True:
            print(f"Item ke- {i}")
            masukanItem = input("Masukan atribut item / berhenti : ")
            if masukanItem == "berhenti":
                break
            else:
                listMasukan = masukanItem.split("#")
                save_item_dari_input_masukan.append(Item(listMasukan[0], listMasukan[1]))
                i += 1
        os.system('pause')
    elif pilih_menu == 6:
        random_item1 = (random.choice(save_item_dari_input_masukan))
        random_item2 = (random.choice(save_item_dari_input_masukan))
        random_item3 = (random.choice(save_item_dari_input_masukan))
        random_item4 = (random.choice(save_item_dari_input_masukan))
        random_item5 = (random.choice(save_item_dari_input_masukan))
        random_item6 = (random.choice(save_item_dari_input_masukan))

        save_random_item1 = random_item1
        save_random_item2 = random_item2
        save_random_item3 = random_item3
        save_random_item4 = random_item4
        save_random_item5 = random_item5
        save_random_item6 = random_item6

        print("hero membeli item")
        print(save_hero_magic_random1.nama, "membeli item", save_random_item1.nama)
        print(save_hero_magic_random2.nama, "membeli item", save_random_item2.nama)
        print(save_hero_magic_random3.nama, "membeli item", save_random_item3.nama)
        print("saber membeli item", save_random_item4.nama)
        print("benedetta membeli item", save_random_item5.nama)
        print("chou membeli item", save_random_item6.nama)

        save_hero_magic_random1.tambahItem(save_random_item1)
        save_hero_magic_random2.tambahItem(save_random_item2)
        save_hero_magic_random3.tambahItem(save_random_item3)
        saber.tambahItem(save_random_item4)
        benedetta.tambahItem(save_random_item5)
        chou.tambahItem(save_random_item6)
        os.system('pause')
    elif pilih_menu == 7:
        total_serangan1_1 = save_hero_magic_random1.basicAttack + save_random_item1.damage
        saber.magicDefense = saber.magicDefense - total_serangan1_1
        total_serangan2_1 = saber.basicAttack + save_random_item4.damage
        save_hero_magic_random1.physicalDefense = save_hero_magic_random1.physicalDefense - total_serangan2_1

        print("Battle dimulai")
        print("#########################")
        print(save_hero_magic_random1.nama, "menyerang saber dengan basic attack + item ", save_random_item1.nama, "sebesar ", total_serangan1_1)
        print("magic defense saber menjadi ", saber.magicDefense)
        print("saber menyerang ", save_hero_magic_random1.nama, "dengan basic attack + item ", save_random_item4.nama, "sebesar ", total_serangan2_1)
        print("physical defense ", save_hero_magic_random1.nama, "menjadi ", save_hero_magic_random1.physicalDefense)

        total_serangan3_1 = save_hero_magic_random1.magicPower + save_hero_magic_random1.skill.attack
        saber.magicDefense = saber.magicDefense - total_serangan3_1
        print(save_hero_magic_random1.nama, "menyerang saber dengan magic attack + ultimate ", save_hero_magic_random1.skill.nama, "sebesar ", total_serangan3_1)
        print("magic defense saber menjadi", saber.magicDefense)

        total_serangan4_1 = saber.physicalAttack + saber.skill.attack + saber.pasif.attack
        save_hero_magic_random1.physicalDefense = save_hero_magic_random1.physicalDefense - total_serangan4_1
        print("saber menyerang ", save_hero_magic_random1.nama, "dengan physic attack + ultimate ", saber.skill.nama, "+ pasif sebesar", total_serangan4_1)
        print("physical defense ", save_hero_magic_random1.nama, "menjadi ", save_hero_magic_random1.physicalDefense)

        if save_hero_magic_random1.hp > saber.hp:
            print("############################")
            print(save_hero_magic_random1.nama, " WIN" )
            print("############################")
        else:
            print("############################")
            print("saber WIN" )
            print("############################")


        
        total_serangan1_2 = save_hero_magic_random2.basicAttack + save_random_item2.damage
        benedetta.magicDefense = benedetta.magicDefense - total_serangan1_2
        total_serangan2_2 = benedetta.basicAttack + save_random_item5.damage
        save_hero_magic_random2.physicalDefense = save_hero_magic_random2.physicalDefense - total_serangan2_2

        print("Battle dimulai")
        print("#########################")
        print(save_hero_magic_random2.nama, "menyerang benedetta dengan basic attack + item ", save_random_item2.nama, "sebesar ", total_serangan1_2)
        print("magic defense benedetta menjadi ", benedetta.magicDefense)
        print("benedetta menyerang ", save_hero_magic_random2.nama, "dengan basic attack + item ", save_random_item5.nama, "sebesar ", total_serangan2_2)
        print("physical defense ", save_hero_magic_random2.nama, "menjadi ", save_hero_magic_random2.physicalDefense)

        total_serangan3_2 = save_hero_magic_random2.magicPower + save_hero_magic_random2.skill.attack
        benedetta.magicDefense = benedetta.magicDefense - total_serangan3_2
        print(save_hero_magic_random2.nama, "menyerang benedetta dengan magic attack + ultimate ", save_hero_magic_random2.skill.nama, "sebesar ", total_serangan3_2)
        print("magic defense benedetta menjadi", benedetta.magicDefense)

        total_serangan4_2 = benedetta.physicalAttack + benedetta.skill.attack + benedetta.pasif.attack
        save_hero_magic_random2.physicalDefense = save_hero_magic_random2.physicalDefense - total_serangan4_2
        print("benedetta menyerang ", save_hero_magic_random2.nama, "dengan physic attack + ultimate ", benedetta.skill.nama, "+ pasif sebesar", total_serangan4_2)
        print("physical defense ", save_hero_magic_random2.nama, "menjadi ", save_hero_magic_random2.physicalDefense)

        if save_hero_magic_random2.hp > benedetta.hp:
            print("############################")
            print(save_hero_magic_random2.nama, " WIN" )
            print("############################")
        else:
            print("############################")
            print("benedetta WIN" )
            print("############################")



        total_serangan1_3 = save_hero_magic_random3.basicAttack + save_random_item3.damage
        chou.magicDefense = chou.magicDefense - total_serangan1_3
        total_serangan2_3 = chou.basicAttack + save_random_item6.damage
        save_hero_magic_random3.physicalDefense = save_hero_magic_random3.physicalDefense - total_serangan2_3

        print("Battle dimulai")
        print("#########################")
        print(save_hero_magic_random3.nama, "menyerang chou dengan basic attack + item ", save_random_item3.nama, "sebesar ", total_serangan1_3)
        print("magic defense chou menjadi ", chou.magicDefense)
        print("chou menyerang ", save_hero_magic_random3.nama, "dengan basic attack + item ", save_random_item6.nama, "sebesar ", total_serangan2_3)
        print("physical defense ", save_hero_magic_random3.nama, "menjadi ", save_hero_magic_random3.physicalDefense)

        total_serangan3_3 = save_hero_magic_random3.magicPower + save_hero_magic_random3.skill.attack
        chou.magicDefense = chou.magicDefense - total_serangan3_3
        print(save_hero_magic_random3.nama, "menyerang chou dengan magic attack + ultimate ", save_hero_magic_random3.skill.nama, "sebesar ", total_serangan3_3)
        print("magic defense chou menjadi", chou.magicDefense)

        total_serangan4_3 = chou.physicalAttack + chou.skill.attack + chou.pasif.attack
        save_hero_magic_random3.physicalDefense = save_hero_magic_random3.physicalDefense - total_serangan4_3
        print("chou menyerang ", save_hero_magic_random3.nama, "dengan physic attack + ultimate ", chou.skill.nama, "+ pasif sebesar", total_serangan4_3)
        print("physical defense ", save_hero_magic_random3.nama, "menjadi ", save_hero_magic_random3.physicalDefense)

        if save_hero_magic_random3.hp > chou.hp:
            print("############################")
            print(save_hero_magic_random3.nama, " WIN" )
            print("############################")
        else:
            print("############################")
            print("chou WIN" )
            print("############################")

    else:
        print("keluar")
        break