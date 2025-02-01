def bmi(kg,m):
    return kg/ m**2

kg=int(input("Kg Cinsinden Vucut Agirligi:"))
m=float(input("Metre Cinsinden Vucut Uzunlugu:"))
bmi=bmi(kg,m)
print(bmi)
if bmi <18.5:
    print("Zayif")
elif bmi<25 and bmi > 18.5:
    print("Normal")
elif bmi<30 and bmi > 25:
    print("Kilolu")
elif bmi<35 and bmi > 30:
    print("Obez")
else:
    print("Asiri Obez")