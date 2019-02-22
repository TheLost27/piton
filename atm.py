bakiye = 1000 #bakiyemiz 1000 tl olsun.

while True:
    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Yeniden Bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL' dir.".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Tutar:"))

        bakiye += miktar
    elif(işlem == "3"):
        miktar = int(input("Çekmek İstediğiniz Tutar:"))

        if(bakiye - miktar < 0):
            print("LÜTFEN GEÇERLİ MİKTAR GİRİNİZ!!!")
            print("Bakiyeniz {} TL' dir".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("LÜTFEN GEÇERLİ İŞLEM GİRİNİZ!!!!")

