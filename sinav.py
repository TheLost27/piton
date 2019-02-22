from datetime import date
from datetime import datetime
day = int(input("Gun Giriniz: "))
month = int(input("Ay Giriniz: "))
year = int(input("Yıl Giriniz: "))
t = date(year,month,day)
print(t.strftime("%j"))




