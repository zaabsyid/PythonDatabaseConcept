class karyawan():
    def __init__(self, nama, nrp):
        self.nama = nama
        self.nrp = nrp

    def gajian(self, honor):
        totalGaji = honor.gajiPokok + honor.lembur + honor.tunjangan
        totalGaji = totalGaji - honor.pajak
        print(self.nama, "mendapatkan Honor sebanyak", totalGaji)

class Honor():
    def __init__(self, gajiPokok, lembur, tunjangan, pajak):
        self.gajiPokok = gajiPokok
        self.lembur = lembur
        self.tunjangan = tunjangan
        self.pajak = pajak

def main ():
    arif = karyawan("Arif", "001")
    honor = Honor(4000000,100000,200000,50000)
    arif.gajian(honor)

main()