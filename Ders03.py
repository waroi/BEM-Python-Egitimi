# aylar=("ocak","şubat","mart","nisan","mayıs","haziran","temmuz","mayıs","haziran","temmuz") # tuple veri tipi (demet) parantez içinde yada parantezsiz tanımlanabilir, 
# aylar2="mayıs","haziran","temmuz" # virgül ile ayrılan herhangi veri tipi olabilir
# aylar3="ağustos", # tek elamanlı tuple verisi için verirnin sonunda virgül olmalı yoksa string olarak tanımlanacaktır.
# print(type(aylar3)) 
# print(aylar[:3])
# print(aylar[2:5])
# print(aylar[1:6:2])
# print(aylar[::2])
# print(aylar[::3])
# print(aylar.index("mart")) # index verdiğimiz değerin kaçıncı indexte olduğunu gösterir
# print("Listemiz içinde",aylar.count("temmuz"),"tane 'temmuz' var") # count verdiğimiz değerden kaç tane olduğunu verir

# dictionary (sözlük) veri tipi**
# dersler={"matematik":80,"Fizik":95,"Biyoloji":85,"Programlama":["Python","Javascript","C#","Java"]}
# dersler["Kimya"]=100
# print(dersler)
# print(len(dersler["Programlama"][1]))
# print(dersler.keys()) # keys metodu anahtar kelimeleri verir
# print(dersler.values()) # values metodu anahtarlar içerisindeki değerleri verir
# print(dersler.items()) # items metodu bütün itemleri getirir(key, values)
# dersler2=dersler.copy() # copy sözlüğün tamamının kopyasını alarak yeni bir değişken içerisine atabilir.
# print(dersler2)
# dersler2.clear()
# dersler2.pop("Fizik") # pop içerisine verilen anahtarı değeri ile birlikte sözlükten siler
# dersler2.popitem()
# dersler3={"matematik":90,"Fizik":100,"Biyoloji":95,"Programlama":["Python","Javascript","C#","Java","Kotlin"]}
# dersler3.update(dersler) # update ile sözlük versini başka bir sözlük versi ile güncelleyebiliriz.
# print(dersler3)

# Koşullar

#Mantıksal Operatörler
# == Eşittir
# != Eşit Değildir
# > Büyüktür
# >= Büyük Eşittir
# < Küçüktür
# <= Küçük Eşittir


# a=int(input("Birinci sayıyı giriniz: "))
# b=int(input("İkinci sayıyı giriniz: "))
# if(a==b):
#   print("Sayılar eşittir")
# else:
#   print("Sayılar eşit değildir")

# vize=int(input("Vize Nonutunuzu Giriniz: "))
# final=int(input("Final Notunuzu Giriniz: "))
# ortalama=int((vize*0.4)+(final*0.6))
# if (ortalama>=85):
#   print("Harf Notunuz: AA")
# elif (ortalama>=70 and ortalama<85):
#   print("Harf Notunuz: BA")
# elif (ortalama>=60 and ortalama<70):
#   print("Harf Notunuz: BB")
# elif (ortalama>=45 and ortalama<60):
#   print("Harf Notunuz: CB")
# elif (ortalama>=40 and ortalama<45):
#   print("Harf Notunuz: CC")
# elif (ortalama>=35 and ortalama<40):
#   print("Harf Notunuz: DC")
# elif (ortalama>=30 and ortalama<35):
#   print("Harf Notunuz: DD")
# else:
#   print("Malesef Dersten Kaldınız!")

# *** Giray beyin örneği
# vize=int(input("Vize notunuzu giriniz: "))
# final=int(input("Final notuuzu giriniz: "))
# ortalama=int((vize*0.4)+(final*0.6))
# if (final>=45):
#  if(ortalama>=85):
#     print("Harf notunuz: AA")
#  elif(ortalama>=70 and ortalama<85):
#     print("Harf notunuz :BA")
#  elif(ortalama>=60 and ortalama<70):
#     print("Ortalamanız:",ortalama)
#     print("Harf notunuz :BB")
#  elif(ortalama>=45 and ortalama<60):
#     print("Harf notunuz :CB")
#  elif(ortalama>=40 and ortalama<45):
#     print("Harf notunuz :CC")
#  elif(ortalama>=35 and ortalama<40):
#     print("Harf notunuz :DC")
#  elif(ortalama>=30 and ortalama<35):
#     print("Harf notunuz :DD")
#  else:
#     print("Malesef dersten kaldınız!")
# else:
#     print("Final notunuz 50'den düşük olduğu için kaldınız!!!")

# Hatice hanımın örneği
# vize=int(input("vize notunuzu giriniz:"))  
# final=int(input("final notunuzu giriniz:"))
# ortalama=int((vize*0.4)+(final*0.6))
# print(ortalama)
# if(final>=50):
#     if(ortalama>=85):
#         print("harf notunuz AA")
#     elif(ortalama>=70  and ortalama< 85):
#         print("harf notunuz BA")
#     elif(ortalama>=60 and ortalama<70  ):
#         print("harf notunuz BB")
#     elif(ortalama>=45 and ortalama<60 ):
#         print("harf notunuz CB")
#     else:
#         print("dersten kaldınız")
# else:
#     print(" FİNALDEN KALDINIZ")

# Gökhan beyin örneği
# vize=int(input("Vize Notunuzu Giriniz: "))
# final=int(input("Final Notunuzu Giriniz: "))
# ortalama=int((vize*0.4)+(final*0.6))
# if (final<45):
#     print("Final Notunuz 45'den Düşük Olduğu için Kaldınız")
# elif (ortalama>=85):
#     print("Harf Notunuz: AA")
# elif (ortalama>=70 and ortalama<85):
#         print("Harf Notunuz: BA")
# elif (ortalama>=60 and ortalama<70):
#         print("Harf Notunuz: BB")
# elif (ortalama>=45 and ortalama<60):
#         print("Harf Notunuz: CB")
# elif (ortalama>=40 and ortalama<45):
#         print("Harf Notunuz: CC")
# elif (ortalama>=35 and ortalama<40):
#         print("Harf Notunuz: DC")
# elif (ortalama>=30 and ortalama<35):
#         print("Harf Notunuz: DD")
# else:
#     print("Malesef Dersten Kaldınız")

# Erkan beyin örneği
# vize=int(input("vize notunuzu giriniz : "))
# final=int(input("final notunuzu giriniz : "))
# ortalama = int((vize*0.4)+(final*0.6))
# print(ortalama)
# if(final>=50):
#     if (ortalama>=85):
#         print("Harf Notunuz: AA")
#     elif(ortalama>=70 and ortalama<85):
#         print("Harf Notunuz: BA")
#     elif(ortalama>=60 and ortalama<70):
#         print("Harf Notunuz: BB")
#     elif(ortalama>=45 and ortalama<60):
#         print("Harf Notunuz: CB")
#     elif(ortalama>=40 and ortalama<45):
#         print("Harf Notunuz: CC")
#     elif(ortalama>=35 and ortalama<40):
#         print("Harf Notunuz: DC")
#     elif(ortalama>=30 and ortalama<35):
#         print("Harf Notunuz: DD")
#     else:
#         print("Malesef Dersten Kaldınız")
# else:
#     print("final notundan değerlendirmeye alınmadı")

# Berkay beyin örneği
# vize=int(input("Not giriniz"))
# final=int(input("Not giriniz"))
# ortalama=int((vize*0.4)+(final*0.6))
# if(final>=50):
#  if(ortalama>=85):
#     print("Harf Notunuz: AA")
#  elif(ortalama>=70 and ortalama<85):
#     print("Harf Notunuz : BA")
#  elif(ortalama>=60 and ortalama<70):
#     print("Harf Notunuz : BB")
#  elif(ortalama>=45 and ortalama<60):
#     print("Harf Notunuz: CB")
#  elif(ortalama>=40 and ortalama<45):
#     print("Harf Notunuz CC")
#  else:
#     print("Malesef Dersten Kaldınız")
# else:
#     print("Finalden düşük aldığın için kaldın")

# islemler=["+","-","*","/"]
# a=int(input("ilk sayıyı giriniz:"))
# x=input("yapılacak işlemi giriniz:")
# b=int(input("ikinci sayıyı giriniz:"))
# if x == islemler[0]:
#     print("Sonucunuz =",a+b)
# elif x ==islemler[2]:
#     print("Sonucunuz =",a*b)
# elif x== islemler[1]:
#     print("Sonucunuz =",a-b)
# elif x== islemler[3]:
#     print("Sonucunuz =",int(a/b))
# else:
#     print("Yanlış işlem seçtiniz")

# a=input("1. Aldığınız dersi giriniz: ")
# b=input("2. Aldığınız dersi giriniz: ")
# if (a=="Python" or a=="Php" or b=="Python" or b=="Php"):
#   print("Dersimize hoşgeldiniz.")
# else:
#   print("Başka derslerde görüşmek üzere")

# Giray İbrahim Eker:
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
#             sonuc=a+b
#             print("Sonucunuz:",sonuc)
#         elif giris==islemler[2]:
#             sonuc=a*b   
#             print("Sonucunuz:",sonuc)
#         elif giris==islemler[1]:
#             sonuc=a-b   
#             print("Sonucunuz:",sonuc)
#         elif giris==islemler[3]:
#             sonuc=int(a/b)   
#             print("Sonucunuz:",sonuc)
#         else:
#             print("Yanlış İşlem Seçtiniz!!")    
#         cikis=input("Devam etmek istiyor musunuz?(Y/N):")
#         if cikis=="Y" or cikis=="y":
#             i+=1
#             devam=input("Aynı sonuç ile devam etmek istiyor musunuz?(Y/N :")
#             if devam=="Y" or devam=="y":
#                 x=2
#             else:
#                 x=0        
#         else:
#             i=0
# else:
#     print("İYİ GÜNLER...:)")



# #**Eren ÖZDEMİR (Vize ve Final Ortlama Hesaplaması)** HATALI*****

# print("Vize ve Final Not Ortalaması Yapmaya Hoşgeldiniz")
# Vize=int(input("Lütfen Vize Notunuzu Giriniz: "))
# Final=int(input("Lütfen Final Notunuzu Giriniz: "))
# Ortalama=int((Vize*0.4)+(Final*0.6))
# print("Ortalamanız",Ortalama)
# if Ortalama<50:   # => Final değil ortalama karşılaştırılmış finalden düşük alsa bile geçebilir.
#     print ("Final Notunuz FF oldugu için Kaldınız Bütlerde Görüşürüz :D ")
# elif (Ortalama>=90):
#     print("Aldıgınız Harf Notu: AA")
#     print("Başarı Durumu:Çok İyi ") 
# elif (Ortalama<90):          # => Burda da karşılaştırma mantık hatası var, 90'dan küçük ne alırsa alsın AB geliyor.
#     print("Aldıgınız Harf Notu: AB")
#     print("Başarı Durumu:İyi ") 
# elif (Ortalama<80):
#     print("Aldıgınız Harf Notu: BB")
#     print("Başarı Durumu:İyi ") 
# elif(Ortalama<70):
#     print("Aldıgınız Harf Notu: CB") 
#     print("Başarı Durumu:Orta ")           
# elif(Ortalama>50 and Ortalama<60):
#     print("Aldıgınız Harf Notu: DF")
#     print("Başarı Durumu:Kötü ")


# # -----Eren ÖZDEMİR Hesap Makinası 
# print("HESAP MAKİNASI UYGULAMASINA HOŞGELİNİZ")


# a=int(input("1.Sayıyı Giriniz: ")) 
# b=int(input("2.Sayıyı Giriniz: "))


# print("Yapmak İstediğiniz İşlemi Seciniz\n1)Toplama\t2)Çıkarma\t3)Çarpma\t4)Bölme")  
# sec = input("Seçenekler: 1, 2, 3, 4 : ")
# print()



# if sec == "1":
#     print("---->> TOPLAMA İŞLEMİ <<-----")
#     print("{}  +   {}    =  {}".format(a, b, a+b))  
#     print("Sonuc",a+b )
    
 
# elif sec == "2":
#     print("---->> ÇIKARMA İŞLEMİ <<-----")
#     a=int(input("1.Sayıyı Giriniz: ")) 
#     b=int(input("2.Sayıyı Giriniz: "))
#     print("{}  -   {}    =  {}".format(a, b, a-b))
#     print("Sonuc",a-b )
# elif sec == "3":
#     print("---->> ÇARPMA İŞLEMİ <<-----")
#     print("{}  *   {}    =  {}".format(a, b, a*b))
#     print("Sonuc",a*b )
# elif sec == "4":
#     print("---->> BÖLME İŞLEMİ <<-----")
#     print("{}  /   {}    =  {}".format(a, b, a/b))
#     print("Sonuc",a/b )

# else :
#     print("Hatalı Giriş!!")
    

# islemD = input("Çıkmak için ' c ' ye basınız : ")
# if islemD == "c":
#         print("Çıkış Yapıldı.")
#         quit()

