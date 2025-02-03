def cafeListe():
    print("1-Cola - ₺50 - 200 Kalori")
    print("2-Gazoz -₺50 - 125 Kalori")
    print("3-Su - ₺25 - 0 Kalori")
    print("4-Turk Kahve - ₺55 - 30 Kalori")
    print("5-Espresso - ₺70 - 30 Kalori")
    print("6-Americano - ₺70 - 30 Kalori")
    print("7-Latte - ₺80 - 300 Kalori")

def cafe(x):
    icecek=["Cola","Gazoz","Su","Turk Kahve","Espresso","Americano","Latte"]
    fiyat =["₺50","₺50","₺25","₺55","₺70","₺70","₺80"]
    kalori = [200,125,0,30,30,30,300]
    birlesim = list(zip(icecek,fiyat,kalori))
    if x==1:
        return birlesim[0]
    if x==2:
        return birlesim[1]
    if x==3:
        return birlesim[2]
    if x==4:
        return birlesim[3]
    if x==5:
        return birlesim[4]
    if x==6:
        return birlesim[5]
    if x==7:
        return birlesim[6]
    return birlesim




#main
cafeListe()
x=int(input("Seciminizi Yapiniz:"))
print("Siparis Bilgisi")
print(cafe(x))