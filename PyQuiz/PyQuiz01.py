
# Problem 1
# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

# Cevap1: Giray bey:
# a=int(input("1.sayıyı giriniz: "))
# b=int(input("2.sayıyı giriniz: "))
# c=int(input("3.sayıyı giriniz: "))
# carpım=a*b*c
# print("Çarpma işlemi sonucunuz: {}",format(carpım))

# # Cevap2 Eren bey:
# a=int(input("1.Sayıyı Giriniz: ")) 
# b=int(input("2.Sayıyı Giriniz: "))
# c=int(input("3.sayıyı Giriniz: "))

# print("{}  *   {}  * {}   =  {}".format(a,b,c,a*b*c))
# print("Sonuc",a*b*c )

# # Cevap3 Gökhan bey:
# a=int(input("1. sayiyi giriniz: "))
# b=int(input("2. sayiyi giriniz: "))
# c=int(input("3. sayiyi giriniz: "))
# carpim=a*b*c
# print("{} * {} * {} = {}".format(a,b,c,carpim))


# Problem 2
# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

# # Cevap1 Erkan bey:
# boy=float(input("Boy Giriniz :"))
# kilo=int(input("Kilo Giriniz :"))
# vke = kilo / (boy*boy)
# print(vke)

# # Cevap2 Giray bey:
# #boy-kilo endeksi
# boy=float(input("Lütfen boyunuzu giriniz(m):"))
# kilo=int(input("Kilonuzu giriniz(kg): "))
# boy_kilo_endeks=kilo/(boy*boy)
# print("Beden kitle endeksiniz: {} 'dir".format(boy_kilo_endeks))


# # Cevap3 Eren bey:
# boy = float(input("Boyunuzu Giriniz:"))
# kilo = int(input("Kilonuzu Giriniz:"))
# hesaplama  = kilo/(boy**2)
# print(hesaplama)

# Cevap3 Gökhan bey:
# a=float(input("kilonuzu giriniz (kg) :"))
# b=float(input("boyunuzu giriniz (m)  :"))
# c=a/(b**2)
# print("Beden Kitle Endeksiniz : {}".format(c))


# Problem 3
# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar 
# ödemesini gerektiğini hesaplayın.

# # Cevap1 Giray bey:
# #araç-kilometre'de ne kadar yakıyor?
# yakim=float(input("Aracınız km'de ne kadar yakıyor?(tl): "))
# km_yol=int(input("Kaç km yol yaptınız?(km):"))
# tutar=int(yakim*km_yol)
# print("Ödemeniz gereken tutar {} TL'dir".format(tutar))

# # Cevap2 Fatih bey: Hatalı
# a=int(input("1km de yakit miktari(krs): "))
# b=int(input("aldigi toplam yol (km) "))
# c= float(a/100)
# d= float(c*a)
# print(d)

# #Cevap3 Eren bey:
# km = int(input("Yaptıgınız Yol ( KM ): "))
# yakit = float(input("Aracınız Ne Kadar Yakıyor  ( TL ): "))
# print("Sonuc:", km*yakit)

# #Cevap4 Erkan bey:
# km_fiyat=float(input("kilometre de yakılan yakıt bedeli :"))
# yapilan_km=float(input("kaç kilometre yapıldığını giriniz :"))
# ödeme=km_fiyat*yapilan_km
# print("tüketilen yakıt bedeli {}'dir".format(ödeme))

# #Cevap5 Gökhan bey:
# a=float(input("araciniz km'de ne kadar yakiyor (tl) :"))
# b=float(input("kaç km yol yaptiniz :"))
# c=a*b
# print("toplam harcadiğiniz para miktari : {}".format(c))

# Problem 4
# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

# #Cevap1 Giray bey:
# ad=input("Adınızı giriniz: ")
# soyad=input("Soyadınızı giriniz: ")
# numara=int(input("Numaranızı giriniz: "))
# print("Adınız :{}\nSoyadınız: {}\nNumaranız: {}".format(ad,soyad,numara))

# #Cevap2 Berkay bey:
# A=input("Adınızı girin:")
# B=input("Soyadınızı girin:")
# C=input("Numaranızı girin:")
# print("\n",A,"\n",B,"\n",C)

# #Cevap3 Hatice hanım:
# ad=input(" adınızı giriniz:")
# soyad=input("soyadınızı giriniz:")
# numara=int(input("numaranızı giriniz"))
# print(ad)
# print(soyad)
# print(numara)

# #Cevap4 Erkan bey:
# isim=str(input("adınızı giriniz:"))
# soyad=str(input("soyadınızı giriniz:"))
# numara=str(input("numaranızı giriniz:"))
# print(isim,soyad,numara,sep="\n")

# #Cevap5 Eren bey:
# a=input("Adınızı Giriniz: ")
# b=input("Soy Adınızı Giriniz: ")
# c=int(input("Numaranızı Giriniz"))
# print(a,b,c,sep="\n")

# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

# #Cevap1 Gireay bey:
# sayi1=int(input("1.Sayıyı giriniz:"))
# sayi2=int(input("2.Sayıyı giriniz:"))
# sayi3=sayi1
# sayi1=sayi2
# sayi2=sayi3
# print("1.sayı: {}\n2.Sayı: {}".format(sayi1,sayi2))

# #Cevap2 Eren bey ve İpek Hanım: a,b=b,a
# a=2
# b=3
# a,b = b,a
# print("a =",a)
# print("b =",b)

# #Cevap3 Erkan bey:
# ilk_sayi=int(input("ilk sayıyı girin :"))
# ikinci_sayi=int(input("ikinci sayıyı girin :"))
# print("ilk sayı için girilen değer {} ikinci sayı için girilen değer {}". format(ilk_sayi, ikinci_sayi))
# ilk_sayi,ikinci_sayi=ikinci_sayi,ilk_sayi
# print("ilk sayı için yeni değer {} ikinci sayı için yeni değer {}". format(ilk_sayi, ikinci_sayi))

# Problem 6
# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
# Hipotenüs Formülü: a^2 + b^2 = c^2

# #Cevap1 Giray bey:
# #dik üçgen hipotenüs uygulaması
# kenar1=int(input("1.kenarı giriniz: "))
# kenar2=int(input("2.kenarı giriniz: "))
# hipotenus=int(((kenar1**2)+(kenar2**2))**0.5)
# print("hipotenus uzunluğu :{}'dir".format(hipotenus))

# # #Cevap2 Berkay bey:
# a=float(input("Kenar uzunluğunu giriniz:"))
# b=float(input("Kenar uzunluğunu giriniz:"))
# c=(((a**2)+(b**2))**(1/2))
# print("Hipotenus",c)

# # # #Cevap3 Erkan bey:
# ilk_kenar=float(input("ilk kenarı girin :"))
# ikinci_kenar=float(input("ikinci kenarı girin :"))
# sonuc= (ilk_kenar**2)+(ikinci_kenar**2)
# print("hipotenüs : {}".format(sonuc**0.5))

# # Cevap4 Gökhan bey:
# a=int(input("1. dik kenar uzunluğunu giriniz:  "))
# b=int(input("2. dik kenar uzunluğunu giriniz: "))
# x=(a**2)+(b**2)
# c=x**0.5
# print("Hipotenüs Uzunluğu: ",c)


# # Cevap5 Hatice hanım:
# a=int(input("üçgenin birinci kenarını giriniz(hipotenüs dışındaki):"))
# b=int(input("üçgenin ikinci kenarını giriniz(hipotenüs dışındaki):"))
# c=a*a+b*b
# hipotenus=c**(1/2)
# print(hipotenus)

# #Cevap6 Eren bey:
# a = int(input("A uzunlugun Giriniz:"))
# b = int(input("B uzunlugunu Giriniz:")) 
# c = (a ** 2 + b ** 2) ** 0.5
# print("\nHipotenüs:",c)

# #Cevap7 Fatih bey:
# import math
# a=int(input("1.sayiyi giriniz: "))
# b=int(input("2.sayiyi yaziniz: "))
# hipotenus= math.sqrt(a**2+b**2)
# print(hipotenus)

# #Cevap8 Eren bey:
# a=int(input("ilk uzunlugu giriniz"))
# b=int(input("ikinci uzunlugu giriniz"))
# x=(a**2+b**2)**0.5
# print("Sonuc",x)


# Çözümler
# Soru 1

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))

# çarpım = a * b * c

# print("{} x {} x {} = {} dir".format(a,b,c,çarpım))

# a:1
# b:3
# c:10
# 1 x 3 x 10 = 30 dir

# Soru 2

# boy = float(input("Boy:"))
# kilo = int(input("Kilo:"))

# print("Beden Kitle İndeksi:",kilo / (boy ** 2))

# Boy:1.73
# Kilo:84
# Beden Kitle İndeksi: 28.06642386982525

# Soru 3

# yakan_miktar = float(input("Kilometrede yakan miktar:"))

# kilometre = int(input("Kaç km yol yaptınız:"))

# print("Tutar: {} tl".format(yakan_miktar * kilometre))

# Kilometrede yakan miktar:0.22
# Kaç km yol yaptınız:430
# Tutar: 94.6 tl

# Soru 4

# ad = input("Ad:")
# soyad = input("Soyad:")
# numara = input("Numara:")
# print("\nBilgiler...\n")
# print("{}\n{}\n{}".format(ad,soyad,numara))

# Ad:Mustafa Murat
# Soyad:Coşkun
# Numara:12345

# Bilgiler...

# Mustafa Murat
# Coşkun
# 12345

# Soru 5

# a = input("a:")
# b = input("b:")

# print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

# a,b = b,a

# print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))

# a:3
# b:4
# Değiştirilmeden Önce Değerler
# a: 3 b: 4

# Değiştirildikten Sonraki Değerler
# a: 4 b: 3

# Soru 6

# a = int(input("a:"))

# b = int(input("b:"))

# c =  (a ** 2 + b ** 2) ** 0.5

# print("Hipotenüs: ",c)

# a:3
# b:4
# Hipotenüs:  5.0

