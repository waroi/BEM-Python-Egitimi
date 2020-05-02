# #ÖDEV
# # FİBONACCİ SAYI DİZİSİ-GİRAY EKER
# sayi1=0
# sayi2=1
# list=[]
# list.append(sayi1)
# list.append(sayi2)
# for i in range(0,30):
#     sayi3=sayi1+sayi2 
#     list.append(sayi3)
#     sayi1,sayi2=sayi2,sayi3
# print("Fibonacci Dizisi:",list)

# #PALİNDROM SAYI DİZİSİ-GİRAY EKER
# deger=input("Değeri girin :")
# if deger.isdigit():  #digit kontrolu için.
#     numara=int(deger)
#     temp=numara  #geçici değer
#     ters=0   #tersi hesaplamak için
#     for i in deger:
#         kalan=numara%10
#         ters=ters*10+kalan
#         numara=numara//10
#     if(temp==ters):
#         print("Girilen numara palindromdur")
#     else:
#         print("Girilen numara palindrom değildir.")
# else:
#     metin=str(deger)
#     if deger==metin[::-1]:
#         print("Girilen metin palindromdur.")
#     else:
#         print("Girilen metin palindrom değildir.")

#İpek hanım:
# number = int(input("Sayi giriniz:")) 
# fibonancci = []
# number1 = 0
# number2 = 1
# for i in range (1,number):
#     result = number1 + number2
#     number1, number2 = number2, result
#     fibonancci.append(number2)
# print(fibonancci) 

# #İpek hanım:
# number = int(input("Sayi giriniz:")) 
# number1 = 0
# number2 = 1
# print(number1, number2, sep="\t",end="\t")
# for i in range (1,number):
#     number1, number2 = number2, number1 + number2
#     print(number2,end="\t") 

#İpek hanım:
# while True:
#     print("Programı sonlandırmak için Q harfine basmanız gerekmektedir.")
#     myString = input("Palindrom olup olmadığını kontrol etmek istediğiniz veriyi giriniz: ")
#     reverseString = myString[::-1]
#     print(reverseString)
#     if (myString=="Q" or myString=="q"):
#         print("Programdan çıkılıyor...İYİ GÜNLER.")
#         break 
#     elif (myString.lower() == reverseString.lower()):
#         print(f'{myString} Palindrom olan bir string örneğidir.')
#         continue
#     else:
#         print(f'{myString} Palindrom olan string örneği değildir.')
#         continue



#Eren ÖZDEMİR*****Fibonnaci Serisi***    
# sayi = int(input ("İlk Kaç Sayının Fibonnaci Serisi Alınsın  : "))
# fibo1=1
# fibo2=1
# k=0
# for i in range (sayi):
#     if (i==0):
#         print (i)
#     elif (i<3):
#         print (1)
#     else :
#         print (fibo1+fibo2)    
#         k=fibo2
#         fibo2=fibo1+fibo2
#         fibo1=k
#Eren ÖZDEMİR*****Fibonnaci Serisi***  2. Yolu liste ile
# sayi = int(input("İlk Kaç Sayının Fibonnaci Serisi Alınsın : "))
# a = 1
# b = 1
# fibo = [a,b]
# for i in range(sayi):
#     a,b = b,a+b #b'yi a'ya attık, a+b'yi de b'ye attık
#     fibo.append(b) #listeye ekliyoruz.
# print(fibo)

#Eren ÖZDEMİR*****Fibonnaci Serisi***  3.yolu while döngüsü - Kontrol edilmeli

# fibo_baslangic = int(input("Dizinin hangi değerden başlamasını istersiniz: " ))
# fibo_max = int(input("Dizinin kaç eleman döndürmesini istersiniz : " ))
# sira=1                                           #eleman sırasını kontrol için başlangıç değeri giriyoruz
# sayi1 = 0                                        #başlangıç sayısını giricez
# sayi2 = fibo_baslangic                           #kullanıcının başlamasını istediği değeri değişkene atadık
# while (sira<=fibo_max):
#     sayi2 , sayi1 = (sayi1 + sayi2) , sayi2      #burada değişken yöntemi kullandık
#     print(sayi1)
#     sira += 1                                    #sırayı arttırıyoruz ve tekrar döngüye sokuyoruz

# def  fibonacci(sinir):
#     sayi1=0
#     sayi2=1
#     print(sayi1)
#     print(sayi2)
#     for i in range(sinir-2):
#         sayi3=sayi1+sayi2
#         print(sayi3)
#         sayi1=sayi2
#         sayi2=sayi3
# sinir=int(input("lütfen sayı giriniz"))
# fibonacci(sinir)


#*********palindrom hem sayi hemde değeri aynanda birliştirme
#Eren ÖZDEMİR
# metin = input("Metni  Giriniz : ")
# ters=metin[::-1]
# print("Girilen metin = %s" % (metin))
# print("Girilen metnin tersi = %s" % (ters))
# if ters == metin:
#     print("--->>>>> [[Girilen metin palindrome.]]<<<<<---")
# else:
#     print("--->>>>> [[Girilen metin palindrome değil.]]<<<<<---")

#Eren ÖZDEMİR HESAP MAKİNASI SONSUZ DÖNGÜLÜ
# print(
# """
# ####################################################
# #                                                  #
# #    HESAP MAKİNESİ UYGULAMASINA HOŞ GELDİNİZ!!!   #
# #                                                  #  
# ####################################################
# """)

# a=int(input("1.Sayıyı Giriniz: ")) 
# b=int(input("2.Sayıyı Giriniz: "))

# print("(1) Toplama İşlemi", "(2) Çıkarma İşlemi", "(3) Çarpma İşlemi", \
# "(4) Bölme İşlemi", "(5) Tabanlı Bölme", "(6) Kuvvet Hesaplama", \
# "(7) Karekök Hesaplama", sep="\n") 
# sec = input("Lütfen yapmak istediğiniz işlem numarasını giriniz(Çıkmak için Q) : ")
# print()

# if sec == "1":
#     print("---->> TOPLAMA İŞLEMİ <<-----")
#     print("{}  +   {}    =  {}".format(a, b, a+b))  
#     print("Sonuc : ",a+b )
    

# elif sec == "2":
#     print("---->> ÇIKARMA İŞLEMİ <<-----")
#     print("{}  -   {}    =  {}".format(a, b, a-b))
#     print("Sonuc : ",a-b )

# elif sec == "3":
#     print("---->> ÇARPMA İŞLEMİ <<-----")
#     print("{}  *   {}    =  {}".format(a, b, a*b))
#     print("Sonuc : ",a*b )

# elif sec == "4":
#     print("---->> BÖLME İŞLEMİ <<-----")
#     print("{}  /   {}    =  {}".format(a, b, a/b))
#     print("Sonuc : ",a/b )

# elif sec == "5":
#     print("---->> TABANLI BÖLME <<-----")
#     print("Bölünen Sayi  //   Bölen Sayi    =  {}".format(a, b, a//b))
#     print("{}  //   {}    =  {}".format(a, b, a//b))
#     print("Sonuç: " , a//b)  

# elif sec == "6":
#     print("---->> KUVVET HESAPLAMA <<-----")
#     print("{}  **   {}    =  {}".format(a, b, a**b))
#     print("Sonuç: ", a**b)  

# elif sec == "7":
#     print("---->> KARAKÖK HESAPLAMA <<-----")
#     print("{}  **0.5   {}    =  {}".format(a, a**0.5))
#     print("Sonuç: ", a**0.5) 
    
# elif sec == "Q" or "q":
#     print("---->> ÇIKIŞ YAPILDI <<-----")
#     quit()
# else :
#     print("Hatalı Giriş!!")  
# soru=input("Devam etmek için d ye basınız(Çıkmak için q)")
# while True:
#     if soru=="q": #2 tuş atadıgım zaman "q" or "Q" hata veriyor.
#         print("---->> ÇIKIŞ YAPILDI <<-----")
#         break
#     elif soru=="d":
#         print("---->> İŞLEMİNİZ DEVAM EDİYOR... <<-----")
#         a=int(input("1.Sayıyı Giriniz: "))
#         b=int(input("2.Sayıyı Giriniz: "))
#         print("(1) Toplama İşlemi", "(2) Çıkarma İşlemi", "(3) Çarpma İşlemi", \
#         "(4) Bölme İşlemi", "(5) Tabanlı Bölme", "(6) Kuvvet Hesaplama", \
#         "(7) Karekök Hesaplama", sep="\n")
#         sec2=input("Lütfen yapmak istediğiniz işlem numarasını giriniz(Çıkmak için q):")
#         if sec2=="1":
#             print("---->> TOPLAMA İŞLEMİ <<-----")
#             print("{}  +   {}    =  {}".format(a, b, a+b))  
#             print("Sonuc : ",a+b )
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")
#         elif sec2=="2":
#             print("---->> ÇIKARMA İŞLEMİ <<-----")
#             print("{}  -   {}    =  {}".format(a, b, a-b))
#             print("Sonuc : ",a-b )
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")
#         elif sec2=="3":
#             print("---->> ÇARPMA İŞLEMİ <<-----")
#             print("{}  *   {}    =  {}".format(a, b, a*b))
#             print("Sonuc : ",a*b )
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")

#         elif sec2=="4":

#             print("---->> BÖLME İŞLEMİ <<-----")
#             print("{}  /   {}    =  {}".format(a, b, a/b))
#             print("Sonuc : ",a/b )
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")

#         elif sec2=="5":

#             print("---->> TABANLI BÖLME <<-----")
#             print("Bölünen Sayi  //   Bölen Sayi    =  {}".format(a, b, a//b))
#             print("{}  //   {}    =  {}".format(a, b, a//b))
#             print("Sonuç: " , a//b)
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")
#         elif sec2=="6":
#             print("---->> KUVVET HESAPLAMA <<-----")
#             print("{}  **   {}    =  {}".format(a, b, a**b))
#             print("Sonuç: ", a**b)
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)") 
#         elif sec2=="7":
#             print("---->> KARAKÖK HESAPLAMA <<-----")
#             print("{}  **0.5   {}    =  {}".format(a, a**0.5))
#             print("Sonuç: ", a**0.5)
#             soru=input("Devam etmek için d ye basınız(Çıkmak için q)")
#         elif sec2=="q":
#                 print("---->> ÇIKIŞ YAPILDI <<-----")
#                 break
#         else:
#             print("Yanlış bir tuşa bastınız !")
#     else:
#         print("Yanlış bir tuşa bastınız lütfen programı yeniden çalıştırın !")
#         break


#Fonksiyonlar

# def merhaba():
#   print("Merhaba")
# merhaba()

# def topla(x,y):
#   print(x+y)
# topla(2,3)

# return ile geriye değer döndürebiliriz
# def topla(x,y):
#   return x+y
# toplam=topla(2,3)
# print(toplam)

# Args örneği
# def topla(*sayi):
#   print(sayi)
#   return sum(sayi)
# print(topla(1,3,5,7,8,9))

# # Kwargs örneği
# def users(**user):
#   print(type(user))
# users(isim='Varol', Soyisim='Maksutoğlu')

# Yerel Değişken
# def fonksiyon():
#   a=10 # => Yerel değişken
#   print(a)
# fonksiyon()
# print(a) # => Yerel değişkenen ulaşamam, çünkü silindi.

# # Global Değişken
# a=10
# def fonksiyon():
#   global a
#   a=5 # => Global
#   def icfonk():
#     global a
#     a=3 # => Yerel
#     print(a)
#   icfonk()
#   print(a)
# fonksiyon()
# print(a)

# lambda fonksiyonu
# def topla(a,b): # Normal Fonksiyon
#   return a+b
# print(topla(3,5))

# topla=lambda a,b:a+b # lambda Fonksiyon
# print(topla(3,5))
# print(topla(5,7))
# print(topla(topla(5,2),topla(3,4)))

# ciftmi=lambda sayi:(sayi%2==0)
# sayi=int(input("Bir sayı giriniz: "))
# a=ciftmi(sayi)
# if a:
#   print("Çift")
# else:
#   print("Tek")

# print("""****************
# Bir sayının bölenlerini bulma

# Programdan çıkmak için 'q' ya basın.
# ****************
# """)

# def bolenleri_bul(sayi):
#     bolen_listesi = []
#     for i in range(1,sayi+1):
#         if (sayi % i == 0):
#             bolen_listesi.append(i)
#     return bolen_listesi

# while True:
#     sayi = input("Sayı:")
#     if (sayi == "q"):
#         print("Programdan Çıkılıyor...")
#         break
#     else:
#         sayi = int(sayi)
#         print(bolenleri_bul(sayi))


# print("""****************
# Bir sayının asal olup olmadığını bulma

# Programdan çıkmak için 'q' ya basın.
# ****************
# """)
# def asal_mi(sayi):
#     for i in range(2,sayi):
#         if (sayi % i == 0 ):
#             return False
#     return True


# while True:
#     sayi = input("Sayı:")
#     if (sayi == "q"):
#         print("Programdan Çıkılıyor...")
#         break
#     sayi = int(sayi)
#     if (sayi == 1):
#         print(sayi, "asal bir sayı değildir.")
#     elif (sayi == 2):
#         print(sayi, "asal bir sayıdır.")
#     else:
#         if (asal_mi(sayi)):
#             print(sayi,"asal bir sayıdır.")
#         else:
#             print(sayi,"asal bir sayı değildir.")

