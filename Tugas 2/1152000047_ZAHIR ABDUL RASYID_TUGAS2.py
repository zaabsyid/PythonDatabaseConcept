import random
import os

class Hero:
    def __init__(self, nama, basicAttack, hp, skill, pasif):
        self.nama = nama
        self.basicAttack = int(basicAttack)
        self.hp = int(hp)
        self.skill = skill
        self.pasif = pasif
        self.item = []

    def tambahItem(self, item):
        self.item.append(item)

class Magical(Hero):
    def __init__(self, nama, basicAttack, hp, skill, magicPower, physicalDef, pasif):
        self.magicPower = int(magicPower)
        self.physicalDef = int(physicalDef)
        super().__init__(nama, basicAttack, hp, skill, pasif)

class Physical(Hero):
    def __init__(self, nama, basicAttack, hp, skill, physicalAttack, magicDefense, pasif):
        self.physicalAttack = int(physicalAttack)
        self.magicDefense = int(magicDefense)
        super().__init__(nama, basicAttack, hp, skill, pasif)

class Item:
    def __init__(self, nama, damage):
        self.nama = nama
        self.damage = int(damage)

class Skill:
    def __init__(self, nama, attack, defense):
        self.nama = nama
        self.attack = int(attack)
        self.defense = int(defense)

mysticGush = Skill("Mystic Gush", 10, 80)
deadlyMagic = Skill("Deadly Magic", 20, 70)
orderNchaos = Skill("Order & Chaos", 30, 60)
violetReqiem = Skill("Violet Reqiem", 40, 50)
zamanForce = Skill("Zaman Force", 40, 50)
vegeaneFlame = Skill("Vegeane Flame", 60, 30)
featheredAirStrike = Skill("Fearhered Air Strike", 70, 20)
bastFeast = Skill("Bats Feast", 80, 10)
tripleSweep = Skill("Triple Sweep", 20, 10)
alecto = Skill("Alecto : Final Blow", 30, 15)
theWayofDragon = Skill("The Way of Dragon", 40, 20)
pasif = Skill("Pasif", 200, 0)


gord = Magical("Gord", 100, 800, mysticGush, 100, 100, 0)
harley = Magical("Harley", 100, 700, deadlyMagic, 200, 200, 0)
lunox = Magical("Lunox", 100, 600, orderNchaos, 300, 300, pasif)
guinevere = Magical("Guinevere", 100, 500, violetReqiem, 400, 400, 0)
harith = Magical("Harith", 100, 400, zamanForce, 500, 500, 0)
valir = Magical("Valir", 100, 300, vegeaneFlame, 600, 600, 0)
pharsa = Magical("Pharsa", 100, 200, featheredAirStrike, 700, 700, pasif)
cecillion = Magical("Cecillion", 100, 100, bastFeast, 800, 800, 0)

saveHeroMagic = [gord, harley, lunox, guinevere, harith, valir, pharsa, cecillion]

saber = Physical("Saber", 100, 400, tripleSweep, 400, 400, pasif)
benedetta = Physical("Benedetta", 100, 300, alecto, 500, 500, pasif)
chou = Physical("Chou", 100, 500, theWayofDragon, 40, 20, pasif)

heroRandomMagic1 = (random.choice(saveHeroMagic))
heroRandomMagic2 = (random.choice(saveHeroMagic))
heroRandomMagic3 = (random.choice(saveHeroMagic))

saveNamaHeroMagic1 = heroRandomMagic1.nama
saveNamaHeroMagic2 = heroRandomMagic2.nama
saveNamaHeroMagic3 = heroRandomMagic3.nama

saveheroMagicRandom1 = heroRandomMagic1
saveheroMagicRandom2 = heroRandomMagic2
saveheroMagicRandom3 = heroRandomMagic3

saveItem = []


def menu1():
    print(f'''
#########
Daftar nama hero magic
$$$$$$$$$
{gord.nama}
{harley.nama}
{lunox.nama}
{guinevere.nama}
{harith.nama}
{valir.nama}
{pharsa.nama}
{cecillion.nama}
#########
''')
    os.system('pause')

def menu2():
    print(f'''
#########
Daftar nama hero physical
$$$$$$$$$
{saber.nama}
{benedetta.nama}
{chou.nama}
#########
''')
    os.system('pause')

def menu3():
    print(f'''
#########
Daftar nama skill hero magic
$$$$$$$$$
{gord.nama} memiliki skill {gord.skill.nama}
{harley.nama} memiliki skill {harley.skill.nama}
{lunox.nama} memiliki skill {lunox.skill.nama}
{lunox.nama} memiliki skill {pasif.nama}
{guinevere.nama} memiliki skill {guinevere.skill.nama}
{harith.nama} memiliki skill {harith.skill.nama}
{valir.nama} memiliki skill {valir.skill.nama}
{pharsa.nama} memiliki skill {pharsa.skill.nama}
{pharsa.nama} memiliki skill {pasif.nama}
{cecillion.nama} memiliki skill {cecillion.skill.nama}
#########
''')
    os.system('pause')

def menu4():
    print(f'''
#########
Daftar nama skill hero physical
$$$$$$$$$
{saber.nama} memiliki skill {saber.skill.nama}
{saber.nama} memiliki skill {pasif.nama}
{benedetta.nama} memiliki skill {benedetta.skill.nama}
{saber.nama} memiliki skill {pasif.nama}
{chou.nama} memiliki skill {chou.skill.nama}
{saber.nama} memiliki skill {pasif.nama}
#########
''')
    os.system('pause')

def menu5():
    print(f'''
3 Magic VS 3 Physical
{saveNamaHeroMagic1}
VS
{saber.nama}
3 Magic VS 3 Physical
{saveNamaHeroMagic2}
VS
{benedetta.nama}
3 Magic VS 3 Physical
{saveNamaHeroMagic3}
VS
{chou.nama}''')
    os.system('pause')
    print('''
Buat item dan tambahkan kepada hero
Membuat beberapa objek item sampai berhenti''')
    i = 1
    while True:
        print(f"Item ke- {i}")
        masukanItem = input("Masukan atribut item / berhenti : ")
        if masukanItem == "berhenti":
            break
        else:
            listMasukan = masukanItem.split("#")
            saveItem.append(Item(listMasukan[0], listMasukan[1]))
            i += 1

    global randomItem1
    global randomItem2
    global randomItem3
    global randomItem4
    global randomItem5
    global randomItem6
    randomItem1 = (random.choice(saveItem))
    randomItem2 = (random.choice(saveItem))
    randomItem3 = (random.choice(saveItem))
    randomItem4 = (random.choice(saveItem))
    randomItem5 = (random.choice(saveItem))
    randomItem6 = (random.choice(saveItem))

    global saveRandomItem1
    global saveRandomItem2
    global saveRandomItem3
    global saveRandomItem4
    global saveRandomItem5
    global saveRandomItem6
    saveRandomItem1 = randomItem1
    saveRandomItem2 = randomItem2
    saveRandomItem3 = randomItem3
    saveRandomItem4 = randomItem4
    saveRandomItem5 = randomItem5
    saveRandomItem6 = randomItem6

    global saveNamarandomItem1
    global saveNamarandomItem2
    global saveNamarandomItem3
    global saveNamarandomItem4
    global saveNamarandomItem5
    global saveNamarandomItem6
    saveNamarandomItem1 = randomItem1.nama
    saveNamarandomItem2 = randomItem2.nama
    saveNamarandomItem3 = randomItem3.nama
    saveNamarandomItem4 = randomItem4.nama
    saveNamarandomItem5 = randomItem5.nama
    saveNamarandomItem6 = randomItem6.nama

def menu6():
    print(f'''
Hero beli item
{saveNamaHeroMagic1} membeli item {saveNamarandomItem1}
{saveNamaHeroMagic2} membeli item {saveNamarandomItem2}
{saveNamaHeroMagic3} membeli item {saveNamarandomItem3}
{saber.nama} membeli item {saveNamarandomItem4}
{benedetta.nama} membeli item {saveNamarandomItem5}
{chou.nama} membeli item {saveNamarandomItem6}
''')
    saveheroMagicRandom1.tambahItem(saveRandomItem1)
    saveheroMagicRandom2.tambahItem(saveRandomItem2)
    saveheroMagicRandom3.tambahItem(saveRandomItem3)
    saber.tambahItem(saveRandomItem4)
    benedetta.tambahItem(saveRandomItem5)
    chou.tambahItem(saveRandomItem6)
    os.system('pause')

def menu7():
    totalDamageSeranganPertama1 = saveheroMagicRandom1.basicAttack + saveRandomItem1.damage
    saber.magicDefense -= totalDamageSeranganPertama1

    totalDamageSeranganPertama2 = saber.basicAttack + saveRandomItem4.damage
    saveheroMagicRandom1.physicalDef -= totalDamageSeranganPertama2

    print("Battle dimulai")
    print("#"*50)
    print(f'''
{saveheroMagicRandom1.nama} menyerang {saber.nama} dengan basic attack + item {saveNamarandomItem1} sebesar {totalDamageSeranganPertama1}
magic defense {saber.nama} menjadi {saber.magicDefense}
hp {saber.nama} menjadi {saber.hp}''')
    
    print(f'''
{saber.nama} menyerang {saveheroMagicRandom1.nama} dengan basic attack + item {saveNamarandomItem4} sebesar {totalDamageSeranganPertama2}
physical defense {saveheroMagicRandom1.nama} menjadi {saveheroMagicRandom1.physicalDef}
hp {saveheroMagicRandom1.nama} menjadi {saveheroMagicRandom1.hp}''')
    totalDamageSeranganPertama3 = saveheroMagicRandom1.magicPower + saveheroMagicRandom1.skill.attack
    saber.magicDefense -= totalDamageSeranganPertama3
    
    print(f'''
{saveheroMagicRandom1.nama} menyerang {saber.nama} dengan magic attack + ultimate {saveheroMagicRandom1.skill.nama} sebesar {totalDamageSeranganPertama3}
magic defense {saber.nama} menjadi {saber.magicDefense}
hp {saber.nama} menjadi {saber.hp}''')
    
    if saveheroMagicRandom1.hp or saber.hp >= 0:
        totalDamageSeranganPertama4 = saber.physicalAttack + saber.skill.attack + saber.pasif.attack
        saveheroMagicRandom1.physicalDef -= totalDamageSeranganPertama4
        
        print(f'''
{saber.nama} menyerang {saveheroMagicRandom1.nama} dengan physic attack + ultimate {saber.skill.nama} + pasif sebesar {totalDamageSeranganPertama4}
physical defense {saveheroMagicRandom1.nama} menjadi {saveheroMagicRandom1.physicalDef}
hp {saveheroMagicRandom1.nama} menjadi {saveheroMagicRandom1.hp}''')
        if saveheroMagicRandom1.hp > saber.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom1.nama} WIN" )
            print("#"*50)
        else:
                print("#"*50)
                print(f"{saber.nama} WIN" )
                print("#"*50)
    else:
        if saveheroMagicRandom1.hp > saber.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom1.nama} WIN" )
            print("#"*50)
        else:
            print("#"*50)
            print(f"{saber.nama} WIN" )
            print("#"*50)

    #3 vs 3 kedua
    totalDamageSeranganKedua1 = saveheroMagicRandom2.basicAttack + saveRandomItem2.damage
    benedetta.magicDefense -= totalDamageSeranganPertama1

    totalDamageSeranganKedua2 = benedetta.basicAttack + saveRandomItem5.damage
    saveheroMagicRandom2.physicalDef -= totalDamageSeranganPertama2

    print("Battle dimulai")
    print("#"*50)
    print(f'''
{saveheroMagicRandom2.nama} menyerang {benedetta.nama} dengan basic attack + item {saveNamarandomItem2} sebesar {totalDamageSeranganKedua1}
magic defense {benedetta.nama} menjadi {benedetta.magicDefense}
hp {benedetta.nama} menjadi {benedetta.hp}''')
    
    print(f'''
{benedetta.nama} menyerang {saveheroMagicRandom2.nama} dengan basic attack + item {saveNamarandomItem5} sebesar {totalDamageSeranganKedua2}
physical defense {saveheroMagicRandom2.nama} menjadi {saveheroMagicRandom2.physicalDef}
hp {saveheroMagicRandom2.nama} menjadi {saveheroMagicRandom2.hp}''')
    totalDamageSeranganKedua3 = saveheroMagicRandom2.magicPower + saveheroMagicRandom2.skill.attack
    benedetta.magicDefense -= totalDamageSeranganKedua3
    
    print(f'''
{saveheroMagicRandom2.nama} menyerang {benedetta.nama} dengan magic attack + ultimate {saveheroMagicRandom2.skill.nama} sebesar {totalDamageSeranganKedua3}
magic defense {benedetta.nama} menjadi {benedetta.magicDefense}
hp {benedetta.nama} menjadi {benedetta.hp}''')
    if saveheroMagicRandom2.hp or benedetta.hp >= 0:
        totalDamageSeranganKedua4 = benedetta.physicalAttack + benedetta.skill.attack + benedetta.pasif.attack
        saveheroMagicRandom2.physicalDef -= totalDamageSeranganPertama4
        print(f'''
{benedetta.nama} menyerang {saveheroMagicRandom2.nama} dengan physic attack + ultimate {benedetta.skill.nama} + pasif sebesar {totalDamageSeranganKedua4}
physical defense {saveheroMagicRandom2.nama} menjadi {saveheroMagicRandom2.physicalDef}
hp {saveheroMagicRandom2.nama} menjadi {saveheroMagicRandom2.hp}''')
        if saveheroMagicRandom2.hp > benedetta.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom2.nama} WIN" )
            print("#"*50)
        else:
                print("#"*50)
                print(f"{benedetta.nama} WIN" )
                print("#"*50)
    else:
        if saveheroMagicRandom2.hp > benedetta.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom2.nama} WIN" )
            print("#"*50)
        else:
            print("#"*50)
            print(f"{benedetta.nama} WIN" )
            print("#"*50)

    #3 vs 3 ketiga
    totalDamageSeranganKetiga1 = saveheroMagicRandom3.basicAttack + saveRandomItem3.damage
    chou.magicDefense -= totalDamageSeranganPertama1

    totalDamageSeranganKetiga2 = chou.basicAttack + saveRandomItem6.damage
    saveheroMagicRandom3.physicalDef -= totalDamageSeranganPertama2


    print("Battle dimulai")
    print("#"*50)
    print(f'''
{saveheroMagicRandom3.nama} menyerang {chou.nama} dengan basic attack + item {saveNamarandomItem3} sebesar {totalDamageSeranganKetiga1}
magic defense {chou.nama} menjadi {chou.magicDefense}
hp {chou.nama} menjadi {chou.hp}''')
    
    print(f'''
{chou.nama} menyerang {saveheroMagicRandom3.nama} dengan basic attack + item {saveNamarandomItem6} sebesar {totalDamageSeranganKetiga2}
physical defense {saveheroMagicRandom3.nama} menjadi {saveheroMagicRandom3.physicalDef}
hp {saveheroMagicRandom3.nama} menjadi {saveheroMagicRandom3.hp}''')
    totalDamageSeranganKetiga3 = saveheroMagicRandom3.magicPower + saveheroMagicRandom3.skill.attack
    chou.magicDefense -= totalDamageSeranganPertama3
    
    print(f'''
{saveheroMagicRandom3.nama} menyerang {chou.nama} dengan magic attack + ultimate {saveheroMagicRandom3.skill.nama} sebesar {totalDamageSeranganKetiga3}
magic defense {chou.nama} menjadi {chou.magicDefense}
hp {chou.nama} menjadi {chou.hp}''')
    if saveheroMagicRandom3.hp or chou.hp >= 0:
        totalDamageSeranganKetiga4 = chou.physicalAttack + chou.skill.attack + chou.pasif.attack
        saveheroMagicRandom3.physicalDef -= totalDamageSeranganPertama4
        
        print(f'''
{chou.nama} menyerang {saveheroMagicRandom3.nama} dengan physic attack + ultimate {chou.skill.nama} + pasif sebesar {totalDamageSeranganKetiga4}
physical defense {saveheroMagicRandom3.nama} menjadi {saveheroMagicRandom3.physicalDef}
hp {saveheroMagicRandom3.nama} menjadi {saveheroMagicRandom3.hp}''')
        if saveheroMagicRandom3.hp > chou.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom3.nama} WIN" )
            print("#"*50)
        else:
                print("#"*50)
                print(f"{chou.nama} WIN" )
                print("#"*50)
    else:
        if saveheroMagicRandom3.hp > saber.hp:
            print("#"*50)
            print(f"{saveheroMagicRandom3.nama} WIN" )
            print("#"*50)
        else:
            print("#"*50)
            print(f"{chou.nama} WIN" )
            print("#"*50)        


while True:
    menu = int(input('''
Selamat Datang di Magic VS Physical
Pilihan :
1. Lihat daftar hero magic
2. Lihat daftar hero pyhical
3. Lihat skill hero magic
4. Lihat skill hero physical
5. Pilih hero & buat item
6. Beli item
7. Battle
8. Keluar
Masukan pilih : '''))
    
    if menu == 1:
        menu1()
    elif menu == 2:
        menu2()
    elif menu == 3:
        menu3()
    elif menu == 4:
        menu4()
    elif menu == 5:
        menu5()
    elif menu == 6:
        menu6()
    elif menu == 7:
        menu7()
    elif menu == 8:
        print("Keluar")
        break
    else:
        print("Masukan menu dengan benar!")