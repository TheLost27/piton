liste = ["345","sadas","324a","14","kemal"]
liste2=[]
try:
    for eleman in liste:
        eleman2 = int(eleman)
        liste2.append(eleman2)
except:
    print("Hata Oldu!!!")
finally:
	print("çalışıyor")
print(liste)
print(liste2)

    
