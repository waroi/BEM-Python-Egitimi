# Programlama Ödevi - Fonksiyonlar
# Not: Buradaki tüm problemler sizin algoritma yeteneğinizi oldukça geliştirecektir. O yüzden zorlandığınız noktalarda pes etmeyin. Üzerine kafa yormaya ve sürekli denemeye çalışın.

# Problem 1
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

# Problem 2
# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

# Problem 3
# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

# Problem 4
# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

# Problem 5
# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)








































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

