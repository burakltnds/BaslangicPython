class Ozellik():
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



class Oyun():
    def __init__(self,karakter,dusman):
        self.karakter=karakter
        self.dusman = dusman
        self.max=10
    
#oyunun calıstıgı yer
    def display(self):
        x=self.takimSec()
        y=self.karakterSec(x)    
        self.oyunDongusu(y,x)
        
#takım seçim       
    def takimSec(self):
        print("Takimlar\n1-DC\n2-Marvel")
        takimSec=int(input("Takimini Sec:"))
        if takimSec == 1:
            return 1 
        elif takimSec == 2:
            return 2
        else:
            return -1
#karakter seçim
    def karakterSec(self,takim):
        if takim==1:
            print("1-Superman\n2-Batman\n3-Robin\n4-Wondergirl\n5-Starfire\n6-Hawk\n7-Dove")
            sec=int(input("DC Karakterinizi Seciniz:"))
            return self.karakter[sec-1]
        elif takim==2:
            print("1-Daredevil\n2-Punisher\n3-Ironman\n4-Spiderman\n5-Thor\n6-Hulk\n7-Wonderwoman\n8-Deadpool\n9-Kaptan America" )
            sec=int(input("Marvel Karakterinizi Seciniz:"))
            return self.dusman[sec-1]
#düşman seçim
    def dusmanSec(self,takim):
        if takim==1:
            sec=int(input("Savasilacak Karakter Seciniz\n1-Daredevil\n2-Punisher\n3-Ironman\n4-Spiderman\n5-Thor\n6-Hulk\n7-Wonderwoman\n8-Deadpool\n9-Kaptan America\n"))
            return self.dusman[sec-1]
        elif takim==2:
            sec=int(input("Savasilacak Karakter Seciniz\n1-Superman\n2-Batman\n3-Robin\n4-Wondergirl\n5-Starfire\n6-Hawk\n7-Dove\n"))
            return self.karakter[sec-1]
#oynanış
    def oyunDongusu(self,karakterin,takim):
        while True:
            if self.max==0:
                print("Oyun Hakkiniz Doldu Oyun Bitti !!!")
                break
            self.max -=1
            print("1-Dinlen\n2-Guc Topla\n3-Savas\n4-Cekil\n")
            islem=int(input("Yapilacak Islem:"))
            if islem==1:
                print(karakterin.dinlen())
            elif islem ==2:
                print(karakterin.gucTopla())
            elif islem ==3:
                if takim == 1:
                    rakip = self.dusmanSec(takim)
                    if karakterin.yetenekPuani > rakip.yetenekPuani:
                        print(f"{karakterin.isim} {rakip.isim} e karsi kazandi")
                    else :
                        print(f"{rakip.isim} {karakterin.isim} i yendi oyun bitti !!!")
                        break
                elif takim==2:
                    rakip = self.dusmanSec(takim)
                    if karakterin.yetenekPuani > rakip.yetenekPuani:
                        print(f"{karakterin.isim} {rakip.isim} e karsi kazandi")
                    else :
                        print(f"{rakip.isim} {karakterin.isim} i yendi oyun bitti !!!")
                        break
            elif islem == 4:
                print(karakterin.cekil())
                break



# Karakterler
marvelKarakterleri = [
    Ozellik("Daredevil", "Matt Murdock", "Ileri Dovus", 7, "Marvel"),
    Ozellik("Punisher", "Frank Castle", "Ileri Dovus", 6, "Marvel"),
    Ozellik("Ironman", "Tony Stark", "Ileri Teknoloji", 11, "Marvel"),
    Ozellik("Spiderman", "Peter Parker", "Ag", 9, "Marvel"),
    Ozellik("Thor", "Thor Odinson", "Cekic", 13, "Marvel"),
    Ozellik("Hulk", "Bruce Banner", "Guc", 9, "Marvel"),
    Ozellik("Wonderwoman", "Diana Prince", "Kontra", 10, "Marvel"),
    Ozellik("Deadpool", "Wade Wilson", "Silah", 10, "Marvel"),
    Ozellik("Kaptan America", "Steve Rogers", "Ozel", 10, "Marvel"),]

dcKarakterleri = [
    Ozellik("Superman", "Clark Kent", "Uçma", 12, "DC"),
    Ozellik("Batman", "Bruce Wayne", "İleri Dövüş", 9, "DC"),
    Ozellik("Robin", "Dick Grayson", "Yardimci", 5, "DC"),
    Ozellik("Wondergirl", "Cassie Sandsmark", "Kontra", 4, "DC"),
    Ozellik("Starfire", "Kori Anders", "Gunes", 7, "DC"),
    Ozellik("Hawk", "Hank Hall", "Yardimci", 3, "DC"),
    Ozellik("Dove", "Dawn Granger", "Yardimci", 3, "DC"),
]

basla=Oyun(dcKarakterleri,marvelKarakterleri)
basla.display()