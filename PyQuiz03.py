
# Programlama Ödevi - Döngüler

# Tebrikler! Bölümü başarıyla bitirdiniz. Şimdi, öğrendiklerinizin akılda kalması için ödevinizi yapma zamanı!
# Not: Buradaki tüm problemler sizin algoritma yeteneğinizi oldukça geliştirecektir. O yüzden zorlandığınız noktalarda pes etmeyin. 
# Üzerine kafa yormaya ve sürekli denemeye çalışın.

# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. 
# (1 + 2 + 3 = 6)

# # Cevap01 Fatih bey:
# sayi = int(input("Sayi Giriniz:"))
# toplam=0
# for i in range(1,sayi):
#     if(sayi%i == 0):
#         toplam +=i
# if(sayi == toplam):
#     print("Mükemmel Sayidir.")
# else:
#     print("Mükemmel Sayi Degildir")

# # Cevap02 Eren bey:
# sayi = int(input("Sayi Gir= "))
# pozitifBolenleriToplami=0
# for i in range(1,sayi):
#     if(sayi%i == 0):
#         pozitifBolenleriToplami +=i
# if(sayi == pozitifBolenleriToplami):
#     print("Girilen SAyi Mükemmel Sayi.")
# else:
#     print("Girilen Mükemmel Sayi Degil !!! ")

# #Cevap03 İlker bey:
# n = int(input("bir sayi giriniz: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if (sum1 == n):
#     print("mukemmel bir sayidir!")
# else:
#     print("mukemmel sayi degildir!")




# Problem 2
# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) 
# o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

# # Cevap01 Giray bey:
# sayi = int(input("Sayıyı Giriniz:"))
# basamak = str(sayi)
# toplam=0
# for x in basamak:
#     rakam = int(x)**len(basamak)
#     toplam += rakam 
# if(sayi == toplam):
#     print("Bu Bir Armstrong Sayısıdır.")
# else:
#     print("Armstong Sayısı Degildir.")

# # Cevap02 Eren bey:
# while True:
#     girdi=input("Sayı girin (Çıkmak için 'q' ya basın.) : ")
#     if girdi=="q":
#         break
#     uzunluk=len(girdi)
#     toplam=0
#     for i in range(uzunluk):
#         toplam = toplam + int(girdi[i])**uzunluk
#     if(toplam==int(girdi)):
#         print("Girdiğiniz Sayı Bir Armstrong Sayıdır!")
#     else:
#         print("Girdiğiniz Sayı Armstrong Bir Sayı Değildir!")

# # Cevap03 İlker bey:
# num = int(input("enter a number: "))
# length = len(str(num))
# sum = 0
# temp = num
# while(temp != 0):
#   sum = sum + ((temp % 10) ** length)
#   temp = temp // 10
# if sum == num:
#   print("armstrong number")
# else:
#   print("not armstrong number")

# # Cevap04 Eren bey:
# sayi = int(input("Sayıyı Giriniz:"))
# basamak = int(input("Basamak Sayısını Giriniz:"))
# toplam =0
# i = sayi
# for x in (str(sayi)):  
#     toplam += int(x) ** basamak   
# if(sayi == toplam):
#     print("Bu Bir Armstrong Sayısıdır.")
# else:
#     print("Armstong Sayısı Degildir.")


# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
# İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.

# # Cevap01 Eren bey:
# for x in range(1,10):
#     for y in range(1,10):
#         print("{} x {} = {}".format(x,y,x*y))

# Cevap02 Eren bey:
# c = int(input("Sayi giriniz:"))  #kullanicidan veri aliniyor
# sayi = c
# for a in range (1,sayi+1):    #1.sutun sayilarini olusturuyor
#     for b in range (1,11):    #2. sutunun 1 den 10 a kadar olan sayilarini olusturuyor
#         carp = a*b
#         if carp == a*b:
#             print(a,"x",b,":",carp)    #ekrana yazdirma
#             if b == 10:     #10 lari yazdirdiktan sonra bir satir bosluk birakir
#                 print("\n")
    


# Problem 4
# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
# Kullanıcı "q" tuşuna bastığı zaman 
# döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
# İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.


# # Cevap01 Giray bey:
# toplam=0
# while True:
#     sayi=input("Sayı giriniz(programdan çıkmak için 'Q' tuşuna basın): ")
#     if sayi=="q" or sayi=="Q":
#         print("Toplamınız {}'dir.Programdan çıkılıyor.".format(toplam))
#         break
#     else:
#         toplam+=int(sayi)

# # Cevap02 Eren bey:
# toplam=0
# print("İşlemi durdurmak için ise Ç ye veya ç ye basınız\n")
# while True:
#   sayi=input("Sayıyı Giriniz:  ")
#   if sayi=="Ç" or sayi=="ç":
#     print("Toplam: ",toplam)
#     break
#   else:
#     toplam+=int(sayi)
# print("\nGirdiğiniz sayıların toplamı=", toplam)

# # Cevap03 İlker bey:
# print("Toplamlarini bulmak icin sayi giriniz.sonucu almak icin '0' a basiniz.")
# count = 0
# sum = 0
# number = 1
# while (number != 0):
#   number = int(input("Sayı girin"))
#   sum = sum + number
#   count += 1
# if(count == 0):
# 	print("bir sayi giriniz")
# else:
# 	print("girdiginiz sayilarin toplami: ", sum)



# Problem 5
# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

# # Cevap01 ERen bey:
# for a in range(1,101):
#   if a%3!=0:
#     continue
#   print(a)

# # Cevap02 Giray bey:
# for x in range(1,101):
#     if x%3!=0:
#         continue
#     else:
#         print(x,end=" ")

# # Cevap03 İlker bey:
# def bolum(count):
#     while count < 101:
#       print(count)
#       count=count+3;
# bolum(0)

# # Cevap04 Giray bey:
# list=[]
# for x in range(1,101):
#     if x%3!=0:
#         continue
#     list.append(x)
# print(list)

# #Cevap05 İlker
# for number in range(3, 100, 3):
#     print(number)


# Problem 6
# List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

# # Cevap01 Giray bey:
# list=[]
# for x in range(0,101,2):
#     list.append(x)
# print(list)

# #Cevap02 Fatih bey:
# list=[]
# for x in range(0,101,2):
#     list.append(x)
# print(list)

# Cevap03 Eren bey:
# ciftsayılar=[]
# for i in range(1,101):
#     if i%2==0:
#         ciftsayılar.append(i)
# print(ciftsayılar)

# # Cevap04 Fatih bey:
# for number in range(2, 100, 2):
  
#     print(number)


















































# Çözümler
# Problem 1

# sayı = int(input("Sayı:"))

# i = 1
# toplam = 0
# while (i < sayı):
#     if (sayı % i == 0):
#         toplam += i
#     i += 1

# if (toplam == sayı):
#     print(sayı,"mükemmel bir sayıdır.")
# else:
#     print(sayı,"mükemmel bir sayı değildir.")

# Sayı:28
# 28 mükemmel bir sayıdır.




# Problem 2

# sayı = input("Sayı:")
# basamak_sayisi = len(sayı)
# sayı = int(sayı)
# basamak = 0
# toplam = 0

# gecici_sayı = sayı

# while (gecici_sayı > 0):
    
#     basamak = gecici_sayı % 10
    
#     toplam += basamak ** basamak_sayisi
    
#     gecici_sayı //= 10
    

# if (toplam == sayı):
#     print(sayı,"bir armstrong sayısıdır.")
# else:
#     print(sayı,"bir armstrong sayısı değildir.")
    

# Sayı:371
# 371 bir armstrong sayısıdır.




# Problem 3

# for i in range(1,11):
#     print("*************************************************")
#     for j in range(1,11):
        
#         print("{} x {} = {}".format(i,j,i*j))

# *************************************************
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# *************************************************
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
# *************************************************
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
# *************************************************
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
# *************************************************
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# *************************************************
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60
# *************************************************
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# *************************************************
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80
# *************************************************
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90
# *************************************************
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# 10 x 4 = 40
# 10 x 5 = 50
# 10 x 6 = 60
# 10 x 7 = 70
# 10 x 8 = 80
# 10 x 9 = 90
# 10 x 10 = 100




# Problem 4

# toplam = 0

# while True:
    
#     sayı = input("Sayı:")
    
#     if (sayı == "q"):
#         break
#     sayı = int(sayı)
    
#     toplam += sayı
    
# print("Girdiğiniz Sayıların Toplamı:",toplam)

# Sayı:1
# Sayı:2
# Sayı:3
# Sayı:4
# Sayı:5
# Sayı:6
# Sayı:7
# Sayı:q
# Girdiğiniz Sayıların Toplamı: 28




# Problem 5

# for i in range(1,101):
    
#     if (i % 3 != 0):
#         continue
#     print(i)

# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
# 33
# 36
# 39
# 42
# 45
# 48
# 51
# 54
# 57
# 60
# 63
# 66
# 69
# 72
# 75
# 78
# 81
# 84
# 87
# 90
# 93
# 96
# 99




# Problem 6

# liste = [x for x in range(1,101) if x % 2 == 0]
# print(liste)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

 

