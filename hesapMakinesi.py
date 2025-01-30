def hesapMakinesi(a,b,islem):
    if islem=="+":
        return a+b
    if islem =="-":
        return a-b
    if islem == "/":
        return a/b
    if islem == "*":
        return a*b

a=int(input("Birinci Sayi:"))
b=int(input("Ikinci Sayi:"))
islem=input("Islemi Sec:")

print(hesapMakinesi(a,b,islem))