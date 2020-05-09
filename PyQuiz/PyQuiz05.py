# Problem 1
# Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
#          [(3,4),(10,3),(5,6),(1,9)]
# Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her 
# bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
#          [12, 30, 30, 9]
# Not : map() fonksiyonunu kullanmaya çalışın.



#*******************************************************************************
#Cevap-1-Giray EKER
# liste=[(3,4),(10,3),(5,6),(1,9)]
# a=map(lambda i:i[0]*i[1],liste)
# print(list(a))
#*******************************************************************************


#Cevap-2-
#Eren ÖZDEMİR
# def dikdörtgen_alan_hesapla(kenar):
#     return kenar[0] * kenar[1]
# liste = [(3,4),(10,3),(5,6),(1,9)]
# print(list(map(dikdörtgen_alan_hesapla,liste)))


# Cevap 03 - İpek Hanım
# list1 = []
# list2 = []
# rectangle = [(3,4),(10,3),(5,6),(1,9)]
# for i,j in rectangle:
#     list1.append(i)
#     list2.append(j)
# alan = map(lambda x,y:x*y,list1,list2)
# print(list(alan))


# Problem 2
# Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
#      [(3,4,5),(6,8,10),(3,10,7)]
# Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve 
# sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.
#      [(3, 4, 5), (6, 8, 10)]
# Not: filter() fonksiyonunu kullanmaya çalışın.

#Cevap 01 - Eren bey:
#Eren ÖZDEMİR
# def üçgen_mi(kenar):
#     if (abs(kenar[0]+kenar[1]) > kenar[2] and abs(kenar[0]+kenar[2]) > kenar[1] and abs(kenar[1]+kenar[2]) > kenar[0]):
#         return True
#     else:
#         return False
# liste = [(3,4,5),(6,8,10),(3,10,7)]
# print(list(filter(üçgen_mi,liste)))


# #*******************************************************************************
# #Cevap-2-Giray EKER - Dik üçgen
# liste=[(3,4,5),(6,8,10),(3,10,7)]
# print(list(filter(lambda x:(x[0]**2+x[1]**2)**0.5==x[2],liste)))
# #*******************************************************************************

# Cevap03 - İpek Hanım
# def pisagor(list):
#     if (list[0]**2 + list[1]**2 == list[2]**2):
#         return True
#     else:
#         return False
# triangle = [(3,4,5),(6,8,10),(3,10,7)]
# triangleList = list(filter(pisagor,triangle))
# print(triangleList)

# Problem 3
# Elinizde şöyle bir liste bulunsun.
#     [1,2,3,4,5,6,7,8,9,10]
# Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
# Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.


# Cevap01 - Eren ÖZDEMİR
# from functools import  reduce
# liste= [1,2,3,4,5,6,7,8,9,10]
# ciftsayilar = reduce(lambda x,y:x+y,filter(lambda sayi:sayi%2==0,liste))
# print(ciftsayilar)

# Cevap02 - Berkay bey:
# from functools import reduce
# liste=[1,2,3,4,5,6,7,8,9,10]
# def cift(sayi):
#     return sayi %2==0
# a=filter(cift,liste)
# b=reduce(lambda x,y:x+y,a)
# print(b)


# #****************************************************************
# #Cevap-3-Giray EKER
# from functools import reduce
# toplam=reduce(lambda x,y:x+y,list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))
# print("Toplam:",toplam)
# #****************************************************************

# # Cevap04 - İpek hanım:
# from functools import reduce
# evenList = list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10]))
# print(evenList)
# toplam = reduce(lambda x,y:x+y,evenList)
# print(toplam)


# Problem 4
# Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
#         isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#         soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
# Not: zip() fonksiyonunu kullanmaya çalışın.


 

# #******************************************************************************
# #Cevap-01-Giray EKER
# isimler=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisimler=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# adSoyad=list(zip(isimler,soyisimler))
# for i in adSoyad:
#     print("İsim Soyisim:",i[0]+" "+i[1])
# #******************************************************************************

# Cevap02 Berkay bey:
# isimler=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisimler=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# b=list(zip(isimler,soyisimler))
# print(*b, sep = "\n")


# #Cevap03
# #Eren ÖZDEMİR
# isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisimler=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# isimvesoyisim =zip(isimler,soyisimler)
# for i in isimvesoyisim:   #alt alta yazdırmak için bu komutu kullandım
#     print(i)
