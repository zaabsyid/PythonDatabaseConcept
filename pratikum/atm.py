class atm:
    def __init__(self, saldo):
        self.__saldo = saldo

    def setSaldo(self, saldoBaru):
        self.__saldo = saldoBaru

    def getSaldo(self):
        return self.__saldo

class hitung:
    def tambah(self, tambahSaldo):
        print("Saldo anda bertambah menjadi : ")
        self.__saldo + tambahSaldo

    def cekSaldo(self):
        print("Saldo anda tersisa : ")
        print("")
