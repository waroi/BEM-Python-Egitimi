# Hata Yakalama
# try:
#   #hata çıkma ihtimali olan  kodlarımızı buraya yazıyoruz.
# except hata1:
#   #hata1 oluştuğunda çalışması gerekenler buraya yazılır.
# except hata2: 
#   #hata2 olduğunda çalışması gerekenler buraya yazılır.

# try:
#   sayi1=int(input("Birinci sayıyı giriniz: "))
#   sayi2=int(input("İkinci sayıyı giriniz: "))
#   sonuc=sayi1/sayi2
#   print("Sonuç:",sonuc)
# except ZeroDivisionError as hata1:
#   print(hata1)
#   print("Sayı sıfıra bölünemez tekrar deneyin.")
# except ValueError:
#   print("Lütfen karakter girmeyiniz, rakam giriniz.")
# except:
#   print("Beklenmeyen bir hata oluştu")
# finally:
#   print("Her durumda çalışacak satır")


# Moduller - Kendi modülümüzü yazma ve math modulu
# import modul
# import math
# # x=10
# # y=5
# # print(modul.bolme(x,y))
# print(dir(modul))

# Dosya işlemleri 
# Modlar:
# r: Sadece okumak için açar, imleç dosyanın başındadır.
# r+: Hem okuma hem yazma için dosyayı açar, imleç dosyanın başıdadır.
# w: Sadece yazmak için dosyayı açar. Dosya yoksa oluşturur. Dosya varsa silip tekrar oluşturur.
# w+:  Hem okuma hem yazma için dosyayı açar,  Dosya yoksa oluşturur. Varsa dosyayı silmez üzerine yazar.
# a: Ekleme yapmak için dosyayı açar. Dosya yoksa oluşturur. Dosya varsa imleç sondadır ve ekleme yapmamızı sağlar.
# a+:  Hem okuma hem ekleme için dosyayı açar, Dosya yoksa oluşturur. Dosya varsa imleç sondadır ve ekleme yapmamızı sağlar.
# import os
# dosya=open("deneme.txt","w")
# dosya.write("Ilk Dosyamiz")
# dosya.close()

# with open("deneme.txt","a") as dosya: # Dosyayı otomatik kapatıyor.
#   dosya.write("\nEkleme Yapildi")

# dosya=open("deneme.txt","a")
# dosya.writelines(["Merhaba","Python"])

# with open("deneme.txt","r") as dosya:
#   print(dosya.read())

# os.remove("deneme.txt")