
# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
#  Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
#  BKİ 18.5'un altındaysa -------> Zayıf
#  BKİ 18.5 ile 25 arasındaysa ------> Normal
#  BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
#  BKİ 30'un üstündeyse -------------> Obez

# #Cevap01 Eren bey:
# print("""*****************************
# Beden Kitle İndeksine Hoşgeldiniz"
# **********************************""")
# boy=float(input("Lütfen boy uzunluğunuzu (m) giriniz: "))
# kilo=int(input("Lütfen ağırlığınızı (kg) giriniz: "))

# hesaplama = kilo/(boy**2)
# print("Sizin Beden Kitle İndeksiniz: {} ".format(hesaplama))

# if (hesaplama<=18.5):
#     print("Zayıf")
# elif(hesaplama>=18.5  and hesaplama< 25):
#     print("Normal")
# elif(hesaplama>=25  and hesaplama< 30):
#     print("Fazla Kilolu")
# elif(hesaplama>=30):
#     print("Obez")

# # Cevap02 Giray bey:
# baslik='''**************************************
#     BOY-KİLO ENDEKSİ HESAPLAMA
# **************************************
# '''
# print(baslik)

# boy=float(input("Lütfen boyunuzu giriniz(m): "))
# kilo=int(input("Lütfen kilonuzu giriniz(kg): "))
# bki=int(kilo/(boy*boy))
# if (bki<=18.5):
#     print("Beden kitle endeksiniz {} 'dir.\nBKI oranına göre ZAYIF durumdasınız.".format(bki))
# elif (bki>18.5 and bki<=25):
#     print("Beden kitle endeksiniz {} 'dir.\nBKI oranına göre NORMAL durumdasınız.".format(bki))
# elif (bki>25 and bki<=30):
#     print("Beden kitle endeksiniz {} 'dir.\nBKI oranına göre FAZLA KİLOLU durumdasınız.".format(bki))
# elif (bki>30):
#     print("Beden kitle endeksiniz {} 'dir.\nBKI oranına göre OBEZ durumdasınız.".format(bki))
# else:
#     print("Yanlış bilgi girişi yapıld!!")

# # Cevap03 İlker bey:
# boy=float(input("Boyunuzu giriniz(cm):"))
# kilo=float(input("kilonuzu giriniz: "))
# x=kilo/((boy/100)**2)
# print("Vücut kitle index’iniz {}".format(round(x,2)))
# print("Durumunuz: ")

# if x <=18.5:
#     print("Zayıfsiniz")
# elif x <=25:
#     print("Normal kilodasiniz")
# elif x<=29:
#     print("Fazla kilolusunuz")
# elif x >= 30:
#     print("obezsiniz")

# #Cevap04 Hatice hanım:
# boy=float(input("boyunuzu giriniz(m):"))
# kilo=float(input("kilonuzu giriniz(kg)"))
# c=kilo/(boy*boy)
# print("beden kütle indeksiniz:{}'dir".format(c))
# if(c<18.5):
#     print("zayıf")
# elif(c>=18.5 and c<25):
#     print("normal")
# elif(c>=25 and c<30):
#     print("fazla kilolu")
# elif(c>=30):
#     print("obez")



# Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

# #Cevap01 Giray bey:
# sayi1=int(input("İlk sayıyı giriniz: "))
# sayi2=int(input("İkinci sayıyı giriniz: "))
# sayi3=int(input("Üçüncü sayıyı giriniz: "))
# if (sayi1>sayi2 and sayi1>sayi3):
#     print("Girmiş olduğunuz en büyük sayı {} 'dir".format(sayi1))
# elif (sayi2>sayi1 and sayi2>sayi3):
#     print("Girmiş olduğunuz en büyük sayı {} 'dir".format(sayi2))
# else:
#     print("Girmiş olduğunuz en büyük sayı {} 'dir".format(sayi3))

# Cevap02
#**************Eren ÖZDEMİR************
# sayi1=int(input("1.Sayıyı Giriniz: "))
# sayi2=int(input("2.Sayıyı Giriniz: "))
# sayi3=int(input("3.Sayıyı Giriniz: "))
# if (sayi1 >= sayi2) and (sayi1 >= sayi3):
#    buyuksayi = sayi1
# elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
#    buyuksayi = sayi2
# elif (sayi3 >=sayi1) and (sayi3>=sayi2):
#     buyuksayi = sayi3                #yada else:buyuksayi = sayi3 de olur
# print(sayi1,",",sayi2,"ve",sayi3,"içinde büyük olan sayı: ",buyuksayi)
#2.soru farklı çözüm deneme
#------>******liste yöntemi ile denemek istedim onun için append komutunu araştırmak zorunda kaldım.<<<*****
# lst = [] ****************************
# sayiadeti = int(input("Kaç Sayı Girilecek: "))
# for n in range(sayiadeti):
#     sayi = int(input("Sayıyı Giriniz: "))
#     lst.append(sayi)
# print("Liste İçindeki En Büyük Sayı :", max(lst), "\nListe İçindeki En Küçük Sayı :", min(lst))

# # Cevap03 İlker bey:
# sayi1 = int(input("1. Sayı: "))
# sayi2 = int(input("2. Sayı: "))
# sayi3 = int(input("3. Sayı: "))
# if (sayi1 >= sayi2) and (sayi1 >= sayi3):
#    buyuk = sayi1
# elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
#    buyuk = sayi2
# else:
#    buyuk = sayi3
# print("Alinan sayilar içinde en büyük olan sayı",buyuk)



# Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
#     Vize1 toplam notun %30'una etki edecek.
#     Vize2 toplam notun %30'una etki edecek.
#     Final toplam notun %40'ına etki edecek.
#     Toplam Not >=  90 -----> AA
#     Toplam Not >=  85 -----> BA
#     Toplam Not >=  80 -----> BB
#     Toplam Not >=  75 -----> CB
#     Toplam Not >=  70 -----> CC
#     Toplam Not >=  65 -----> DC
#     Toplam Not >=  60 -----> DD
#     Toplam Not >=  55 -----> FD
#     Toplam Not <  55 -----> FF

# # Cevap01 
# #**************Eren ÖZDEMİR************
# vize1 = input("1.Vize Sonucu: ")
# vize2 = input("2.Vize Sonucu: ")
# Final = input("Final Sonucu: ")
# sonuc = int(vize1)*0.3 + int(vize2)*0.3 + int(Final)*(0.4)
# if(sonuc >=90):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("AA")
# elif(sonuc>=85):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("BA")
# elif(sonuc>=80):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("BB")
# elif(sonuc>=75):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("CB")
# elif(sonuc>=70):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("CC")
# elif(sonuc>=65):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("DC")
# elif(sonuc>=60):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("DD")
# elif(sonuc>=55):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("FD")
# elif(sonuc>=50):
#     print("Aldıgınız Harf Notu: ")
#     print(sonuc)
#     print("FF")
# else:
#     print("Kaldınız")        # -------------->Bunu koymamdaki amac tüm sınavlara 10 dediğimde hesaplamaması

# #Cevap02 İlker bey:
# vize1 = input("1. Vize:")
# vize2 = input("2. Vize:")
# Final = input("Final:")
# sonuc = int(vize1)*(3/10) + int(vize2)*(3/10) + int(Final)*(4/10)
# if(sonuc >=90):
#     print("AA")
# elif(sonuc>=85):
#     print("BA")
# elif(sonuc>=80):
#     print("BB")
# elif(sonuc>=75):
#     print("CB")
# elif(sonuc>=70):
#     print("CC")
# elif(sonuc>=65):
#     print("DC")
# elif(sonuc>=60):
#     print("DD")
# elif(sonuc>=55):
#     print("FD")
# elif(sonuc<55):
#     print("FF")

# #Cevap03 Fatih bey:
# vize1=int(input("Vize1 Nonutunuzu Giriniz: "))
# vize2=int(input("Vize2 Nonutunuzu Giriniz: "))
# final=int(input("Final Notunuzu Giriniz: "))
# toplamnot=int((vize1*0.3)+(vize2*0.3)+(final*0.4))
# if (toplamnot>=90):
#   print("Harf Notunuz: AA")
# elif (toplamnot>=85 and toplamnot<90):
#   print("Harf Notunuz: BA")
# elif (toplamnot>=80 and toplamnot<85):
#   print("Harf Notunuz: BB")
# elif (toplamnot>=75 and toplamnot<80):
#   print("Harf Notunuz: CB")
# elif (toplamnot>=70 and toplamnot<75):
#   print("Harf Notunuz: CC")
# elif (toplamnot>=65 and toplamnot<70):
#   print("Harf Notunuz: DC")
# elif (toplamnot>=60 and toplamnot<65):
#   print("Harf Notunuz: DD")
# elif (toplamnot>=55 and toplamnot<60):
#   print("Harf Notunuz: FD")
# elif (toplamnot>=50 and toplamnot<55):
#   print("Harf Notunuz: FF")
# else:
#   print("Malesef Dersten Kaldınız!")

# #Cevap04 Hatice Hanım:
# a=int(input("1.vize notunuzu giriniz:"))
# b=int(input("2.vize notunuzu giriniz:"))
# c=int(input("final notunuzu giriniz:"))
# vize_1=a*30/100
# vize_2=b*30/100
# final=c*40/100
# toplam_not=(vize_1)+(vize_2)+(final)
# print("toplam not:{}" .format(toplam_not))
# if(toplam_not>=90):
#     print("AA")
# elif(toplam_not>=85):
#     print("BA")
# elif(toplam_not>=80):
#     print("BB")
# elif(toplam_not>=75):    
#     print("CB")
# elif(toplam_not>=70):
#     print("CC")
# elif(toplam_not>=65):
#     print("DC")
# elif(toplam_not>=60):
#     print("DD")
# elif(toplam_not>=55):
#     print("FD")
# elif(toplam_not<55):
#     print("FF")

# #Cevap05 Giray bey:
# baslik='''**************************************
#     ORTALAMA HESAPLAMA ARACI
# **************************************
# '''
# print(baslik)
# vize1=int(input("1.vize notunuzu giriniz: "))
# vize2=int(input("2.vize notunuzu giriniz: "))
# final=int(input("Final notunuzu giriniz: "))
# ortalama=int((vize1*0.3)+(vize2*0.3)+(final*0.4))
# if (final<45):
#     print("Final notunuz {} olduğu için ortalamanız hesaplanamadı.\nDersten kaldınız!!".format(final))
# elif(ortalama>=90):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz AA 'dir".format(ortalama))
# elif(ortalama<90 and ortalama>=85):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz BA 'dir".format(ortalama))
# elif(ortalama<85 and ortalama>=80):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz BB 'dir".format(ortalama))
# elif(ortalama<80 and ortalama>=75):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz CB 'dir".format(ortalama))
# elif(ortalama<75 and ortalama>=70):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz CC 'dir".format(ortalama))
# elif(ortalama<70 and ortalama>=65):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz DC 'dir".format(ortalama))
# elif(ortalama<65 and ortalama>=60):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz DD 'dir".format(ortalama))
# elif(ortalama<60 and ortalama>=55):
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz FD 'dir".format(ortalama))
# else:
#     print("Ortalamanız {} 'dir.\nBaşarı notunuz FD 'dir.\nDersten kaldınız!!".format(ortalama))


# Problem 4
# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi 
# olduğunu bulmaya çalışın.
# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi 
# olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
# Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu 
# kullanabilirsiniz. Kullanımı şu şekildedir ;
# abs(-4)
# 4
# abs(5)
# 5

# # Cevap01 Giray bey:
# baslik='''
# Bulunabilecek geometrik şekiller
# 1-Üçgen
# 2-Dörtgen

# ***ÜÇGEN BELİRTME ŞARTI***
# |b-c|<a<b+c
# |a-c|<b<a+c
# |a-b|<c<a+b
# '''
# print(baslik)
# sekil=input("Hangi geometrik şekli bulmak istiyorsunuz?: ")
# if(sekil=="1"):
#     kenar1=int(input("1.kenarı giriniz: "))
#     kenar2=int(input("2.kenarı giriniz: "))
#     kenar3=int(input("3.kenarı giriniz: "))
#     if((abs(kenar1-kenar2)<kenar3<kenar1+kenar2) or (abs(kenar2-kenar3)<kenar1<kenar2+kenar3) or (abs(kenar1-kenar3)<kenar2<kenar1+kenar3)):
#         if(kenar1==kenar2 and kenar1==kenar3):
#             print("Girmiş olduğunuz kenar uzunluklarına göre bu üçgen bir EŞKENAR ÜÇGEN'dir")
#         elif(kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3):
#             print("Girmiş olduğunuz kenar uzunluklarına göre bu üçgen bir İKİZKENAR ÜÇGENDİR'dir")
#         else:
#             print("Girmiş olduğunuz kenar uzunluklarına göre bu üçgen bir SIRADAN BİR ÜÇGEN'dir")
#     else:
#         print("Girmiş olduğunuz kenar uzunlukları bir ÜÇGEN belirtmiyor!!")
# elif(sekil=="2"):
#     kenar1=int(input("1.kenarı giriniz: "))
#     kenar2=int(input("2.kenarı giriniz: "))
#     kenar3=int(input("3.kenarı giriniz: "))
#     kenar4=int(input("4.kenarı giriniz: "))
#     if(kenar1==kenar2 and kenar1==kenar3 and kenar1==kenar4):
#         print("Girmiş olduğunuz kenar uzunluklarına göre bu dörtgen bir KARE'dir")
#     elif((kenar1==kenar2 and kenar3==kenar4) or (kenar1==kenar3 and kenar2==kenar4) or (kenar1==kenar4 and kenar2==kenar3)):
#          print("Girmiş olduğunuz kenar uzunluklarına göre bu dörtgen bir DİKDÖRTGENDİR'dir")
#     else:
#          print("Girmiş olduğunuz kenar uzunluklarına göre bu dörtgen bir SIRADAN BİR DÖRTGEN'dir")
# else:
#     print("Yanlış veya eksik veri girdiniz..")

# # Cevap02
# #**************Eren ÖZDEMİR************
# print("""
# ****************************
# Üçgen veya Dörtgenin Şekli Bulma
# ****************************
# Üçgenin tipini hesaplamak için 1'e basın
# Dikdörtgenin tipini hesaplamak için 2'ye basın
# ***********************************
# """)
# cikti=input("Seçin yapın : ")
# if cikti =="1":
#     x=int(input("1.Kenarı Giriniz : "))
#     y=int(input("2.Kenarı Giriniz : "))
#     z=int(input("3.Kenarı Giriniz : "))
#     if (abs(y-z)<x and x<y+z) and (abs(x-z)<y and y<x+z) and (abs(x-y)<z and z<x+y):
#         if (x==y and x!=z) or (x==z and x!=y) or (y==z and y!=x):
#             print("Bu üçgen İkizkenar'dır.")
#         elif x==y==z:
#             print("Bu üçgen Eşkenar'dır.")
#         else:
#           print("Standart üçgen")
#     else:
#         print("Bu ölçüler bir üçgen bulunamadı.")
# elif cikti =="2":
#     a=int(input("1.Kenarı girin : "))
#     b=int(input("2.Kenarı girin : "))
#     c=int(input("3.Kenarı girin : "))
#     d=int(input("4.Kenarı girin : "))
#     if a==b==c==d:
#         print("Bu şekil Kare'dir.")
#     elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
#         print("Bu şekil Dikdörtgen'dir.")
#     else:
#         print("Sıradan bir Dörtgen.")
# else:
#   print("Yanlış seçim yaptınız")




































# Çözümler
# Problem 1

# boy = float(input("Boyunuzu Giriniz:"))
# kilo = int(input("Kilonuzu Giriniz:"))

# bki =  kilo / (boy ** 2)

# if (bki < 18.5):
#     print("Zayıf")
# elif (bki >= 18.5 and bki < 25):
#     print("Normal")
# elif (bki >= 25 and bki < 30):
#     print("Fazla Kilolu")
# else:
#     print("Obez")

# Boyunuzu Giriniz:1.74
# Kilonuzu Giriniz:76
# Fazla Kilolu

# Problem 2

# a =  int(input("a:"))

# b = int(input("b:"))

# c = int(input("c:"))

# if (a >= b and a >= c):
#     print("En büyük sayı:",a)
# elif (b >= a and b >= c):
#     print("En büyük sayı:",b)
# elif (c >= a and c >= b):
#     print("En büyük sayı:",c)
    
    

# a:5
# b:6
# c:4
# En büyük sayı: 6

# Problem 3

# vize1 = int(input("Vize1:"))
# vize2 = int(input("Vize2:"))
# final = int(input("Final:"))


# genel_not =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10

# if (genel_not >= 90):
#     print("AA")
# elif (genel_not >= 85):
#     print("BA")
# elif (genel_not >= 80):
#     print("BB")
# elif (genel_not >= 75):
#     print("CB")
# elif (genel_not >= 70):
#     print("CC")
# elif (genel_not >= 65):
#     print("DC")
# elif (genel_not >= 60):
#     print("DD")
# elif (genel_not >= 55):
#     print("FD")
# else:
#     print("FF")
    

# Vize1:40
# Vize2:90
# Final:70
# DC

# Problem 4

# şekil =  input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

# if (şekil == "Dörtgen"):
#     print("Lütfen kenarları sırayla giriniz.")
#     a = int(input("Kenar-1:"))
#     b = int(input("Kenar-2:"))
#     c = int(input("Kenar-3:"))
#     d = int(input("Kenar-4:"))
    
#     if (a == b and a == c and a == d):
#         print("Kare")
#     elif (a == c and b == d):
#         print("Dikdörtgen")
#     else:
#         print("Dörtgen")
        
    
    
# elif (şekil == "Üçgen"):
#     a = int(input("Kenar-1:"))
#     b = int(input("Kenar-2:"))
#     c = int(input("Kenar-3:"))
#     if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
#         if (a == b and a == c ):
#             print("Eşkenar Üçgen...")
#         elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
#             print("İkizkenar Üçgen....")
#         else:
#             print("Çeşitkenar Üçgen...")
#     else:
#         print("Üçgen belirtmiyor...")
        
# else:
#     print("Geçersiz Şekil...")

# Hangi şeklin tipini öğrenmek istiyorsunuz?Üçgen
# Kenar-1:3
# Kenar-2:3
# Kenar-3:3
# Eşkenar Üçgen...

