class WNI():
    def __init__(self, nama):
        self.nama = nama
        self.ktp = KTP(34010212890003, "RI210102")

class KTP():
    def __init__(self, noKTP, idKTP):
        self.noKTP = noKTP
        self.idKTP = idKTP

    def cetakKTP(self):
        print("Nomor KTP ini:", self.noKTP, "dengan id:", self.idKTP)

def main():
    budi = WNI("Budi")
    budi.ktp.cetakKTP()

main()