class Ozellik():
    maxTur = 10

    def __init__(self, isim, gercekIsim, guc, yetenekPuani, evren):
        self.isim = isim
        self.gercekIsim = gercekIsim
        self.guc = guc
        self.yetenekPuani = yetenekPuani
        self.evren = evren

    def gucTopla(self):
        self.yetenekPuani += 1
        return f"{self.isim} gucunu topladi! Yeni yetenek puani: {self.yetenekPuani}"

    def dinlen(self):
        return f"{self.isim} dinleniyor..."

    def cekil(self):
        return f"{self.isim} oyundan cekildi!"

    def savas(self):
        return f"{self.isim} savasiyor! Yetenek Puani: {self.yetenekPuani}"


# Karakterler
marvelKarakterleri = {
    1: Ozellik("Daredevil", "Matt Murdock", "Ileri Dovus", 7, "Marvel"),
    2: Ozellik("Punisher", "Frank Castle", "Ileri Dovus", 6, "Marvel"),
    3: Ozellik("Ironman", "Tony Stark", "Ileri Teknoloji", 11, "Marvel"),
    4: Ozellik("Spiderman", "Peter Parker", "Ag", 9, "Marvel"),
    5: Ozellik("Thor", "Thor Odinson", "Cekic", 13, "Marvel"),
    6: Ozellik("Hulk", "Bruce Banner", "Guc", 9, "Marvel"),
    7: Ozellik("Wonderwoman", "Diana Prince", "Kontra", 10, "Marvel"),
    8: Ozellik("Deadpool", "Wade Wilson", "Silah", 10, "Marvel"),
    9: Ozellik("Kaptan America", "Steve Rogers", "Ozel", 10, "Marvel"),
}

dcKarakterleri = {
    1: Ozellik("Superman", "Clark Kent", "Uçma", 12, "DC"),
    2: Ozellik("Batman", "Bruce Wayne", "İleri Dövüş", 9, "DC"),
    3: Ozellik("Robin", "Dick Grayson", "Yardimci", 5, "DC"),
    4: Ozellik("Wondergirl", "Cassie Sandsmark", "Kontra", 4, "DC"),
    5: Ozellik("Starfire", "Kori Anders", "Gunes", 7, "DC"),
    6: Ozellik("Hawk", "Hank Hall", "Yardimci", 3, "DC"),
    7: Ozellik("Dove", "Dawn Granger", "Yardimci", 3, "DC"),
}

# Takım seçimi
takim = int(input("Takimini Sec\n1 - MARVEL\n2 - DC\nSeciminiz: "))

if takim == 1:
    print("\nMarvel Karakterleri:")
    for k, v in marvelKarakterleri.items():
        print(f"{k} - {v.isim}")
    secim = int(input("\nKarakterini Sec: "))
    karakter = marvelKarakterleri.get(secim, None)

elif takim == 2:
    print("\nDC Karakterleri:")
    for k, v in dcKarakterleri.items():
        print(f"{k} - {v.isim}")
    secim = int(input("\nKarakterini Sec: "))
    karakter = dcKarakterleri.get(secim, None)

else:
    print("Yanlis secim yaptiniz!")
    exit()

if karakter:
    print(f"\nSectiginiz karakter: {karakter.isim}\n")
else:
    print("Gecersiz secim!")
    exit()

# Oyun döngüsü
turSayisi = Ozellik.maxTur

while turSayisi > 0:
    print("\n--- TUR SEÇİMİ ---")
    secim = int(input("Bu Tur Ne Yapmak İstiyorsunuz?\n1 - Savaş\n2 - Güç Topla\n3 - Dinlen\n4 - Çekil\nSeçiminiz: "))

    if secim == 1:
        print(karakter.savas())
    elif secim == 2:
        print(karakter.gucTopla())
    elif secim == 3:
        print(karakter.dinlen())
    elif secim == 4:
        print(karakter.cekil())
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")

    turSayisi -= 1

print("\nOyun bitti!")
