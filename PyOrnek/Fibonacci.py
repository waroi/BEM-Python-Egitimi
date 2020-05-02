"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
1,1,2,3,5,8,13,21,34...............
"""
ilkSayi = 1
ikinciSayi = 1
fibonacci = [ilkSayi,ikinciSayi]
for i in range(10):
    ilkSayi,ikinciSayi = ikinciSayi,ilkSayi + ikinciSayi
    fibonacci.append(ikinciSayi)
print(fibonacci)