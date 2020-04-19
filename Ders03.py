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