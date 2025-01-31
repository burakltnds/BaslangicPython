from random import randint

def sayiOlustur():
    a=randint(0,50)
    if a <=10:
        print("0 ile 10 arasinda")
    elif a<=20 and a>10:
        print("11 ile 20 arasinda")
    elif a<=30 and a>20:
        print("21 ile 30 arasinda")
    elif a<=40 and a>30:
        print("31 ile 40 arasinda")
    elif a<=50 and a>40:
        print("41 ile 50 arasinda")
    return a

a=sayiOlustur()
count=10

while True:
    x=int(input("Tahmin Ettiginiz Sayi(0-50 Arasi):"))
    if count==0:
        print("Tahmin Hakkiniz Doldu Basarisiz Oldunuz")
        break
    elif a==x:
        print("Tebrikler Dogru Tahmin Sayiniz -> ",a)
        print("Basari Yuzdesi -> %",(count/10)*100)
        break
    else:
        print("Yanlis Tahmin Tekrar Deneyin")
        
    count=count-1