import datetime


class RentalSepeda:

    def __init__(self, unit =0):
        self. unit = unit

    def persediaanSepeda(self):
        print("Kami memiliki {} ketersediaan sepeda yang siap untuk disewa".format(self.unit))
        return self.unit

    def sepedaPerJam(self, n):
        if n <= 0:
            print("Persediaan Sepeda harus Positif")
            return None

        elif n > self.unit:
            print(
                "Maaf kami memiliki {} sepeda yang tersedia".format(self.unit))
            return None

        else:
            now = datetime.datetime.now()
            print("Anda telah menyewa {} sepeda per jam hari ini pada jam {}.".format(
                n, now.hour))
            print("Anda akan dikenakan biaya $5 untuk setiap jam per sepeda.")

            self.unit -= n
            return now

    def sepedaPerHari(self, n):
        if n <= 0:
            print("Persediaan Sepeda harus Positif")
            return None

        elif n > self.unit:
            print(
                "Maaf kami memiliki {} sepeda yang tersedia".format(self.unit))
            return None

        else:
            now = datetime.datetime.now()
            print("Anda telah menyewa {} sepeda setiap hari hari ini pada jam {}.".format(
                n, now.hour))
            print("Anda akan terkena biaya $20 setiap hari untuk 1 unit sepeda.")

            self.persediaan -= n
            return now

    def sepedaPerMinggu(self, n):
        if n <= 0:
            print("Persediaan Sepeda harus Positif")
            return None

        elif n > self.unit:
            print(
                "Maaf kami memiliki {} sepeda yang tersedia".format(self.unit))
            return None

        else:
            now = datetime.datetime.now()
            print("Anda telah menyewa {} sepeda setiap minggu hari ini pada jam {}.".format(
                n, now.hour))
            print("Anda akan dikenakan biaya $60 untuk setiap minggu per sepeda.")
            self.unit -= n

            return now

    def returnBike(self, request):
        """
        1. Terima sepeda sewaan dari pelanggan
        2. Mengisi ulang inventaris
        3. Kembalian Uang
        """
        waktuSewa, sewa, jumlahSepeda = request
        tagihan = 0

        if waktuSewa and sewa and jumlahSepeda:
            self.unit += jumlahSepeda
            now = datetime.datetime.now()
            periodeSewa = now - waktuSewa

            if sewa == 1:
                tagihan = round(periodeSewa.seconds / 3600) * 5 * jumlahSepeda

            elif sewa == 2:
                tagihan = round(periodeSewa.days) * 20 * jumlahSepeda

            elif sewa == 3:
                tagihan = round(periodeSewa.days / 7) * 60 * jumlahSepeda

            if (3 <= jumlahSepeda <= 5):
                print(
                    "Anda memenuhi syarat untuk promosi sewa Keluarga dengan diskon 30%")
                tagihan = tagihan * 0.7

            print("Akan menjadi ${}".format(tagihan))
            return tagihan
        else:
            print("Apakah Anda yakin Anda menyewa sepeda dengan kami?")
            return None


class Customer:

    def __init__(self):

        self.sepeda = 0
        self.sewa = 0
        self.waktuSewa = 0
        self.biaya = 0

    def requestBike(self):

        bikes = input("Berapa banyak sepeda yang ingin Anda sewa?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Yang Anda Masukkan bukan bilangan bulat positif!")
            return -1

        if bikes < 1:
            print("Jumlah sepeda harus lebih besar dari nol!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        if self.sewa and self.waktuSewa and self.bikes:
            return self.waktuSewa, self.sewa, self.bikes
        else:
            return 0, 0, 0


def main():
    toko = RentalSepeda(100)
    customer = Customer()

    while True:
        print("""
        ====== Toko Sewa Sepeda =======
        1. Tampilkan sepeda yang tersedia
        2. Sewa sepeda setiap jam $5
        3. Sewa sepeda per hari $20
        4. Sewa sepeda per minggu $60
        5. Kembalikan Sepeda
        6. Keluar
        """)

        pilih = input("Masukkan Pilihan: ")

        try:
            pilih = int(pilih)
        except ValueError:
            print("Yang Anda pilih tidak ada atau salah")
            continue

        if pilih == 1:
            toko.persediaanSepeda()

        elif pilih == 2:
            customer.waktuSewa = toko.sepedaPerJam(
                customer.requestBike())
            customer.sewa = 1

        elif pilih == 3:
            customer.waktuSewa = toko.sepedaPerHari(
                customer.requestBike())
            customer.sewa = 2

        elif pilih == 4:
            customer.waktuSewa = toko.sepedaPerMinggu(
                customer.requestBike())
            customer.sewa = 3

        elif pilih == 5:
            customer.tagihan = toko.returnBike(customer.returnBike())
            customer.sewa, customer.waktuSewa, customer.bikes = 0, 0, 0
        elif pilih == 6:
            break
        else:
            print("Masukkan pilihan angka antara 1-6 ")


if __name__ == "__main__":
    main()
