class Hero () :
    def __init__ (self, namaHero,  roleHero) :
        self.nama = namaHero
        self.role = roleHero

input1 = input("Masukan nama hero : ")
input2 = input("Masukan role hero : ")

uranus = Hero(input1, input2)
print(uranus)
print(uranus.nama)
print(uranus.role)