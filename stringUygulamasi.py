
isim=input("Adinizi Giriniz:")
while True:
    print("Isleminizi Seciniz:\n0-Cikis Yap\n1-Harfleri Buyut\n2-Bas Harfi Buyut\n3-Isim Soyisim Ayirma\n4-Uzunlugunu Goster\n5-Kullanici Adi Olustur")
    secim=int(input("Seciminiz:"))
    if secim==1:
        print (isim.upper())
    elif secim==2:
        print (isim.capitalize())
    elif secim==3:
        isimListesi=isim.split()
        print (isimListesi)
    elif secim==4:
        print (len(isim))
    elif secim==5:
        isimListesi2 = isim.split()
        print(isimListesi2[0][0],isimListesi2[1][0],len(isim),sep="")
    elif secim==0:
        break
    else:
        print ("Yanlis Bir İslem Yaptiniz Tekrar Deneyiniz")
