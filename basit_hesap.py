a = int(input("Birinci Sayı=")) #birinci sayi
b = int(input("İkinci Sayı="))  #ikinci sayi

işlem = input("İşlem Numarasını Giriniz.") #Buna göre koşullarımızı yazacağız.

if(işlem == "1"): #toplama işlemi
    print("{} ile {} ' nin toplam {} dır.".format(a,b,a+b))
elif(işlem == "2"): #çıkarma işlemi 
    print("{} ile {} ' nin farkı {} dır.".format(a,b,a-b))
elif(işlem == "3"): #çarpma işlemi
    print("{} ile {} ' nin çarpımı {} dır.".format(a,b,a*b))
elif(işlem == "4"): #bölme işlemi 
    print("{} ile {} ' nin bölümü {} dır.".format(a,b,a/b))
else:
    print("LÜTFEN GEÇERLİ İŞLEM GİRİNİZ!!!")

