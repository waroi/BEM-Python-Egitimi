from random import randint

rand=randint(1,100)
tahminSayac=0

while True:
  tahminSayac+=1
  sayi=int(input("1 ile 100 arasında bir değer giriniz (çıkmak için 0 girin): "))
  if (sayi==0):
    print("Oyunu iptal ettiniz.")
    break
  elif sayi < rand:
    print("Daha yüksek bir sayı girin.")
    continue
  elif sayi > rand:
    print("Daha küçük bir sayı girin.")
    continue
  else:
    print("Bildiniz sayı:",rand)
    print("Tahmin sayınız:",tahminSayac)
    
