
def hesapMakinesi(a,b,islem):
    if islem not in "+-/*^":
        return "yanlis islem secildi"
    if islem=="+":
        return a+b
    if islem =="-":
        return a-b
    if islem == "/":
        return a/b
    if islem == "*":
        return a*b
    if islem == "^":
        return a ** b


#main
while True:
    try:
        a=int(input("Birinci Sayi:"))
        b=int(input("Ikinci Sayi:"))
        islem=input("Islemi Sec:")
        print(hesapMakinesi(a,b,islem))
    except:
        print("Bir Yanlis Yapildi")