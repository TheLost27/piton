import datetime
x = datetime.datetime.__add__(input("Gün Giriniz: "))
print(x)
t = datetime.datetime.strftime(x,'%j')
print(t)


