b=int(input("Sayı Giriniz: "))
        

def fact(sayi):
    if (sayi == 1):
        return 1
    else:
        return sayi*fact(sayi-1)
a = fact(b)
print(a)

