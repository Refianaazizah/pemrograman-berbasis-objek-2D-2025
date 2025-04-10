class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."


manusia1 = Manusia("shinta", 19, "Surabaya")
manusia2 = Manusia("Edo", 21, "Malang")
manusia3 = Manusia("Fina", 26, "Jakarta")
manusia4 = Manusia("Riko", 17, "Badung")
manusia5 = Manusia("Lisa", 30, "Solo")


print(manusia1.berjalan())
print(manusia2.berlari())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berjalan())