"""
Fibonacci Serisi yeni bir sayoıyıönceki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,24...........
"""
ilk_sayı = 1
ikincisayi = 1

fibonacci = [ilk_sayı,ikincisayi]
for i in range(10):
	
	ilk_sayı,ikincisayi = ikincisayi,ilk_sayı + ikincisayi 
	
	fibonacci.append(ikincisayi)
print(fibonacci)

