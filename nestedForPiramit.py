x = int(input("Piramit Yuksekligi:"))
for i in range(1,x+1):
    for j in range(1,x-i+1):
        print(" " , end="")
    for k in range(1,2*i):
        print("*",end="")
    print()