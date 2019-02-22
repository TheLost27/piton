dizi = [1,2,3] 
dizi1 = [0,0,0]
dizi2 = dizi # dizinin id si dizi2 ye aktarılır.
dizi3 = dizi1.copy() # dizi3 e yeni id atanır. 
dizi.append(7) # diziye eklendiğinde dizi2 nin de idsi aynı yere bağlı olduğu için dizi2 yi yazdırıldığında 1,2,3,7 çıkar.
dizi1.append(11) # dizi1 ve dizi3 ün id leri farklı olduğu için dizi3 e 11 eklenmez ve dizi3 print edildiğinde 0,0,0 alınır. 
print(dizi2)
print(dizi3)
dizi = [] # burada en baştaki dizi listesinin idsi dizi2 yede tanımlı olduğu için yok olmazancak dizi listesinin id si değişir.
print(dizi2) # dizi2 nin id si değişmediği için çıktı 1,2,3,7 olarak gelir.

