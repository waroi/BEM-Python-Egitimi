# Programlama Ödevi - Fonksiyonlar
# Not: Buradaki tüm problemler sizin algoritma yeteneğinizi oldukça geliştirecektir. O yüzden zorlandığınız noktalarda pes etmeyin. Üzerine kafa yormaya ve sürekli denemeye çalışın.

# Problem 1
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

# Cevap01
# ###MÜKEMMEL SAYI BULMA(FONKSİYON)-GİRAY EKER#####
# def mukemmelSayi(sayi):
#     mukSayi=list()
#     toplam=0
#     for i in range(1,sayi):
#         if (sayi%i==0):
#             toplam +=i                
#     if(toplam == sayi):
#         mukSayi.append(toplam)
#     return mukSayi

# mukSayi=list()
# for sayi in range(1,1001):
#     if (mukemmelSayi(sayi)):
#         mukSayi.append(sayi)
# print("Mükemmel Sayılar Listesi: ",mukSayi)

#Cevap02
#Eren ÖZDEMİR
# mukemmel_mi = lambda sayi: sum(filter(lambda d: sayi % d == 0, range(1, sayi))) == sayi
# print(list(filter(mukemmel_mi, range(1, 1001))))

# Cevap03
#Eren ÖZDEMİR
# def mükemmel(sayı):
#     toplam = 0
#     for i in range(1,sayı):
#         if (sayı % i == 0):
#             toplam += i 
#     return toplam == sayı
# for i in range(1,1001):
#     if (mükemmel(i)):
#         print("Mükemmel Sayı:",i)


# Problem 2
# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

# Cevap01
#Eren ÖZDEMİR
# sayı1=int(input("1.Sayiyi Giriniz : "))
# sayı2=int(input("2.Sayiyi Giriniz : "))
# def ebob_bul(sayı1,sayı2):
#     i = 1
#     ebob = 1
#     while (i <= sayı1 and i <= sayı2 ):

#         if ( not (sayı1 % i) and not (sayı2 % i)):
#             ebob = i
#         i += 1
#     return ebob
# print("ebob: ",ebob_bul(sayı1,sayı2))

# Cevap02
##İKİ SAYININ EBOB-EKOK BULMA-GİRAY EKER#####
# def ebob(sayi1,sayi2):
#     list=[]
#     if sayi1>sayi2:
#         for i in range(1,sayi2+1):
#             if (sayi1%i==0 and sayi2%i==0):
#                 list.append(i)
#         list.sort()
#         print("Girilen iki sayının EBOB'u {} 'dır.".format(list[-1]))
#     elif sayi1<sayi2:
#         for i in range(1,sayi1+1):
#             if (sayi1%i==0 and sayi2%i==0):
#                 list.append(i)
#         list.sort()
#         print("Girilen iki sayının EBOB'u {} 'dır.".format(list[-1]))

# def ekok(sayi1,sayi2):
#     ekok=1
#     a=2  #ekok bulurken önce 2'ye bölerek başlarız 
#     while (sayi1>1 or sayi2>1):
#         if (sayi1%a==0 and sayi2%a==0):
#             ekok *= a
#             sayi1//=a
#             sayi2//=a
#         elif (sayi1%a==0 and sayi2%a!=0):
#             ekok *= a
#             sayi1//=a
#         elif (sayi1%a!=0 and sayi2%a==0):
#             ekok *= a
#             sayi2//=a
#         else:
#             a += 1 
#     print("Girilen iki sayının EKOK'u {}'dır".format(ekok))
#     return ekok


# print("""
# *************************************************************
# *               EBOB-EKOK BULMA ARACI                       *
# *************************************************************
# Hangi işlemi yapmak istediğinizi seçiniz?(Programdan çıkmak için "Q" ya basınız...)

# 1-) EKOK BULMA
# 2-) EBOB BULMA
# """)
# İ=1
# while İ>0:
#     islem=input("Yapmak istediğiniz işlemi seçiniz :")
#     sayi1=int(input("1.Sayıyı giriniz: "))
#     sayi2=int(input("2.Sayıyı giriniz: "))
#     if islem=="q" or islem =="Q":
#         print("Programdan çıkılıyor...İYİ GÜNLER")
#     elif islem=="1":
#         ekok(sayi1,sayi2)
#     elif islem=="2":
#         ebob(sayi1,sayi2)
#     else:
#         print("Yanlış yada eksik tuşlama yaptınız!!.")
#     devam=input("İşleme devam etmek istiyor musunuz?(Y/N): ")
#     if devam=="y" or devam=="Y":
#         İ+=1
#     else:
#         print("Programdan çıkılıyor...İYİ GÜNLER")
#         break


# Cevap03
# def ebob(num1,num2): 
#     i = 1
#     ebob = 1
#     while (i <= num1 and i <= num2 ):
#         if ( not (num1 % i) and not (num2 % i)):
#             ebob = i
#         i += 1
#     return ebob
# num1 = int(input("EBOB işlemi için 1. sayıyı giriniz: "))
# num2 = int(input("EBOB işlemi için 2. sayıyı giriniz: "))
# print("Ebob:",ebob(num1,num2))


# Problem 3
# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

#Cevap01
# def ekok(num1,num2):
#     i = 2
#     ekok = 1
#     while True:
#         if (num1 % i == 0 and num2 % i == 0):
#             ekok *= i
#             num1 //= i 
#             num2 //= i 
#         elif (num1 % i == 0 and not num2 % i == 0):
#             ekok *= i
#             num1 //= i
#         elif (not num1 % i == 0 and num2 % i == 0):
#             ekok *= i
#             num2 //= i
#         else:
#             i += 1
#         if (num1 == 1 and num2 == 1):
#             break
#     return ekok
# num1 = int(input("EKOK işlemi için 1. sayıyı giriniz: "))
# num2 = int(input("EKOK işlemi için 2. sayıyı giriniz: "))
# print("EKOK:",ekok(num1,num2))


# Cevap02
#Eren ÖZDEMİR
# def ekok_bul(sayı1,sayı2): 
#     i = 2
#     ekok = 1
#     while True:
#         if (sayı1 % i == 0 and sayı2 % i == 0):
#             ekok *= i
#             sayı1 //= i
#             sayı2 //= i
#         elif (sayı1 % i ==  0 and sayı2 % i != 0):
#             ekok *= i
#             sayı1 //= i
#         elif (sayı1 % i != 0 and sayı2 % i == 0):
#             ekok *= i
#             sayı2 //= i
#         else:
#             i += 1
#         if (sayı1 == 1 and sayı2 == 1):
#             break
#     return ekok
# sayı1 = int(input("1.Sayiyi Giriniz: "))
# sayı2 = int(input("1.Sayiyi Giriniz: "))
# print("Ekok:",ekok_bul(sayı1,sayı2))


# Problem 4
# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

# Cevaop01
#Eren ÖZDEMİR
# birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
# onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
# def yazma(a):
#     k = a % 10
#     m = a // 10
#     return onlar[m] + " " + birler[k]
# while True:
#     a = input("2 basamaklı Okunmasını istediğiniz bir sayı giriniz.(Çıkmak için q'ya basınız.)\n")
#     if (a =="q"):
#         print("Çıkış Yapıldı...")
#         break
#     else:
#         a = int(a)
#         print(" Girmiş oldugunuz \"{}\" sayısının yazılışı \"{}\" şeklindedir.".format(a,yazma(a)))

# Cevap02
####Girilen İki basamaklı sayının okunuşu-GİRAY EKER######
# def ikibas(sayi):
#     onlar_bas_oku=["Doksan","Seksen","Yetmiş","Altmış","Elli","Kırk","Otuz","Yirmi","On"]
#     birler_bas_oku=["Dokuz","Sekiz","Yedi","Altı","Beş","Dört","Üç","İki","Bir"]
#     rakam=[9,8,7,6,5,4,3,2,1]
#     kalan1=sayi%10
#     kalan2=sayi//10
#     if kalan1>0 and kalan2>0 and kalan2<10:
#         birler=birler_bas_oku[rakam.index(kalan1)]
#         onlar=onlar_bas_oku[rakam.index(kalan2)]
#         print("Girilen sayının okunuşu : {} {}".format(onlar,birler))
#     elif kalan1==0 and kalan2<10:
#         onlar=onlar_bas_oku[rakam.index(kalan2)]
#         print("Girilen sayının okunuşu : {}".format(onlar))
#     else:
#         print("Girmiş olduğunuz sayı iki basamaklı değildir.")
# sayi=int(input("İki basamaklı sayı giriniz: "))
# ikibas(sayi)

# Cevap03 - İpek Hanım
# birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
# onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
# def sayi_okuma(a):
#     k = a % 10
#     m = a // 10
#     return onlar[m] + " " + birler[k]
# while True:
#     number = input("2 basamaklı Okunmasını istediğiniz bir sayı giriniz. (Çıkmak için q'ya basınız.)\n")
#     if (number == "q" or number == "Q"):
#         print("Çıkış Yapıldı...")
#         break
#     elif(len(number)==2 or len(number)==1):
#         print(" Girmiş oldugunuz \"{}\" sayısının yazılışı \"{}\" şeklindedir.".format(number,sayi_okuma(int(number))))
#     else:
#         if(number.isdigit()):
#             number = input("2 basamaklı bir sayı giriniz. (Çıkmak için q'ya basınız.)\n")
#         else:
#             print("Sayı giriniz...")


# Problem 5
# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

# Cevap01
#######PISAGOR UCGENI BULMA-GİRAY EKER#########
# def pisagorBulma():
#     pısagorListesi = list()
#     for i in range(1,101):
#         for j in range(1,101):
#             c=(i**2 + j**2)**0.5
#             if (c == int(c)):
#                 pısagorListesi.append((i,j,int(c)))
#     return pısagorListesi
# print("Pisagor Listesi: ",pisagorBulma())

# Cevap02
#Eren ÖZDEMİR
# def pisagor_bul():
#     pisagor_listesi = list()
#     for i in range(1,101):
#         for j in range(1,101):
#             c = (i ** 2 + j ** 2) ** 0.5
#             if (c == int(c) ):
#                 pisagor_listesi.append((i,j,int(c)))
#     return pisagor_listesi
# for i in pisagor_bul():
#     print(i)



# # Hesap Makinası öğrneği
# def topla(a,b):
#     print("Sonucunuz: ",a+b)
# def carp(a,b):
#     print("Sonucunuz: ",a*b)
# def cıkar(a,b):
#     print("Sonucunuz: ",a-b)
# def bol(a,b):
#     print("Sonucunuz: ",int(a/b))
# baslik='''
# *************************************************************
# *         -HESAP MAKİNASI PROGRAMINA HOŞGELDİNİZ-           *
# *************************************************************
# PROGRAMDAN ÇIKMAK İÇİN 'Q'e BASIN!!!
# '''
# print(baslik)
# islemler=["+","-","*","/"]
# print("Yapılabilen işlemler:",islemler)
# i=1
# x=0
# sonuc=0
# while i>0:
#     giris=input("Hangi işlemi yapmak istiyorsunuz?: ")
#     if giris=="Q" or giris=="q":
#         print("Programdan çıkılıyor...İYİ GÜNLER.")
#         break
#     else:
#         if (x>1):
#             a=sonuc
#         else:
#             a=int(input("ilk sayıyı giriniz:"))
#         b=int(input("ikinci sayıyı giriniz:"))    
#         if giris==islemler[0]:
#             topla(a,b)
#         elif giris==islemler[2]:
#             carp(a,b)
#         elif giris==islemler[1]:
#             cıkar(a,b)
#         elif giris==islemler[3]:
#             bol(a,b)
#         else:
#             print("Yanlış İşlem Seçtiniz!!")    
#         cikis=input("Devam etmek istiyor musunuz?(Y/N):")
#         if cikis=="Y" or cikis=="y":
#             i+=1
#             devam=input("Aynı sonuç ile devam etmek istiyor musunuz?(Y/N) :")
#             if devam=="Y" or devam=="y":
#                 x=2
#             else:
#                 x=0        
#         else:
#             i=0
# else:
#     print("İYİ GÜNLER...:)")

































# Çözümler
# Problem 1

# def mukemmel(sayı):
    
#     toplam = 0
    
#     for i in range(1,sayı):
        
#         if (sayı % i == 0):
#             toplam += i
            
#     return toplam == sayı


# for i in range(1,1001):
#     if (mukemmel(i)):
#         print("Mükemmel Sayı:",i)
    

# Mükemmel Sayı: 6
# Mükemmel Sayı: 28
# Mükemmel Sayı: 496

# Problem 2

# def ebob_bulma(sayı1,sayı2):
    
#     i = 1
#     ebob = 1
#     while (i <= sayı1 and i <= sayı2 ):

#         if ( not (sayı1 % i) and not (sayı2 % i)):
#             ebob = i
#         i += 1
#     return ebob
# sayı1 = int(input("Sayı-1:"))
# sayı2 = int(input("Sayı-2:"))

# print("Ebob:",ebob_bulma(sayı1,sayı2))

# Sayı-1:15
# Sayı-2:100
# Ebob: 5

# Problem 3

# def ekok_bulma(sayı1,sayı2):
    
#     i = 2
#     ekok = 1
#     while True:
#         if (sayı1 % i == 0 and sayı2 % i == 0):
#             ekok *= i

#             sayı1 //= i
#             sayı2 //= i


#         elif (sayı1 % i ==  0 and sayı2 % i != 0):
#             ekok *= i

#             sayı1 //= i


#         elif (sayı1 % i != 0 and sayı2 % i == 0):
#             ekok *= i

#             sayı2 //= i
#         else:
#             i += 1
#         if (sayı1 == 1 and sayı2 == 1):
#             break
#     return ekok

# sayı1 = int(input("Sayı-1:"))
# sayı2 = int(input("Sayı-2:"))

# print("Ekok:",ekok_bulma(sayı1,sayı2))

# Sayı-1:12
# Sayı-2:24
# Ekok: 24

# Problem 4

# birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
# onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

# def okunus(sayı):
#     birinci = sayı % 10
#     ikinci = sayı // 10
    
#     return onlar[ikinci] + " " + birler[birinci]

    
# sayı =  int(input("Sayı:"))

# print(okunus(sayı))

# Sayı:17
# On Yedi

# def pisagor_bulma():
    
#     pisagor_listesi = list()
#     for i in range(1,101):
#         for j in range(1,101):

#             c = (i ** 2 + j ** 2) ** 0.5

#             if (c == int(c) ):
#                 pisagor_listesi.append((i,j,int(c)))

#     return pisagor_listesi

# for i in pisagor_bulma():
#     print(i)

# (3, 4, 5)
# (4, 3, 5)
# (5, 12, 13)
# (6, 8, 10)
# (7, 24, 25)
# (8, 6, 10)
# (8, 15, 17)
# (9, 12, 15)
# (9, 40, 41)
# (10, 24, 26)
# (11, 60, 61)
# (12, 5, 13)
# (12, 9, 15)
# (12, 16, 20)
# (12, 35, 37)
# (13, 84, 85)
# (14, 48, 50)
# (15, 8, 17)
# (15, 20, 25)
# (15, 36, 39)
# (16, 12, 20)
# (16, 30, 34)
# (16, 63, 65)
# (18, 24, 30)
# (18, 80, 82)
# (20, 15, 25)
# (20, 21, 29)
# (20, 48, 52)
# (20, 99, 101)
# (21, 20, 29)
# (21, 28, 35)
# (21, 72, 75)
# (24, 7, 25)
# (24, 10, 26)
# (24, 18, 30)
# (24, 32, 40)
# (24, 45, 51)
# (24, 70, 74)
# (25, 60, 65)
# (27, 36, 45)
# (28, 21, 35)
# (28, 45, 53)
# (28, 96, 100)
# (30, 16, 34)
# (30, 40, 50)
# (30, 72, 78)
# (32, 24, 40)
# (32, 60, 68)
# (33, 44, 55)
# (33, 56, 65)
# (35, 12, 37)
# (35, 84, 91)
# (36, 15, 39)
# (36, 27, 45)
# (36, 48, 60)
# (36, 77, 85)
# (39, 52, 65)
# (39, 80, 89)
# (40, 9, 41)
# (40, 30, 50)
# (40, 42, 58)
# (40, 75, 85)
# (40, 96, 104)
# (42, 40, 58)
# (42, 56, 70)
# (44, 33, 55)
# (45, 24, 51)
# (45, 28, 53)
# (45, 60, 75)
# (48, 14, 50)
# (48, 20, 52)
# (48, 36, 60)
# (48, 55, 73)
# (48, 64, 80)
# (48, 90, 102)
# (51, 68, 85)
# (52, 39, 65)
# (54, 72, 90)
# (55, 48, 73)
# (56, 33, 65)
# (56, 42, 70)
# (56, 90, 106)
# (57, 76, 95)
# (60, 11, 61)
# (60, 25, 65)
# (60, 32, 68)
# (60, 45, 75)
# (60, 63, 87)
# (60, 80, 100)
# (60, 91, 109)
# (63, 16, 65)
# (63, 60, 87)
# (63, 84, 105)
# (64, 48, 80)
# (65, 72, 97)
# (66, 88, 110)
# (68, 51, 85)
# (69, 92, 115)
# (70, 24, 74)
# (72, 21, 75)
# (72, 30, 78)
# (72, 54, 90)
# (72, 65, 97)
# (72, 96, 120)
# (75, 40, 85)
# (75, 100, 125)
# (76, 57, 95)
# (77, 36, 85)
# (80, 18, 82)
# (80, 39, 89)
# (80, 60, 100)
# (80, 84, 116)
# (84, 13, 85)
# (84, 35, 91)
# (84, 63, 105)
# (84, 80, 116)
# (88, 66, 110)
# (90, 48, 102)
# (90, 56, 106)
# (91, 60, 109)
# (92, 69, 115)
# (96, 28, 100)
# (96, 40, 104)
# (96, 72, 120)
# (99, 20, 101)
# (100, 75, 125)

