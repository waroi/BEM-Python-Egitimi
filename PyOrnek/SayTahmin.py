# from random import randint
 
# rand=randint(1, 100)
# sayac=0
 
# while True:
#     sayac+=1
#     sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
#     if(sayi==0):
#         print("Oyunu İptal Ettiniz")
#         break
#     elif sayi < rand:
#         print("Daha Yüksek Bir Sayı Girin.")
#         continue
#     elif sayi > rand:
#         print("Daha Düşük Bir Sayı Girin.")
#         continue
#     else:
#         print("Rastele seçilen sayı {0}!".format(rand))
#         print("Tahmin sayınız {0}".format(sayac))
 

 # ---------------------------------------------------------------------

# input("""-----------------Sayı Tahmin Oyununa Hoşgeldiniz-----------------
# Kurallar:
# (1) Oyunun başında senden bir sayı yazman istenir.1 ile 100 arasında bir değer girmenizi istiyoruz.
# (2) 0 rakamını girerseniz hesaplama yapılmayacaktır.
# (3) Harf girerseniz yine işlem yapılmayacaktır.

# NOT=İstenilenin dışında girilen her değer hesaplanmayacaktır...
# -------İYİ OYUNLAR DİLERİZ-------
# Devam etmek için "enter" tuşuna basınız...""")
# print()


# print("""********************************
# ----------------İşlem Listesi---------
# 1. Sınırsız Hak
# 2. Sınırlı Hak (5 adet Hakkınız Bulunur)
# ****************************************
# """)

# while True:
#     isim = input("Lütfen İsminizi Giriniz : ")
#     secenek = input("Lütfen Oyun tarzınızı Seçiniz (Çıkış için 'q' ya basalım) : ")
#     if secenek == 'q' or secenek == 'Q':
#         print("Çıkış Yapıldı...")
#         quit()

#     elif secenek == "1":
#         print("------Sınırsız Hakkınızı Seçtiniz İyi Oyunlar Dileriz------")
#         print()

#         from random import randint
#         rand=randint(1, 100)
#         sayac=0
#         while True:
#             sayac+=1
#             sayi=int(input("1 ile 100 arasında değer girin (0 işleniniz geçersiz sayılır ve oyun iptal olur.):"))
#             if(sayi==0):
#                 print("Oyunu İptal Ettiniz")
#                 break
#             elif sayi < rand:
#                 print("Daha Yüksek Bir Sayı Girin.")
#                 continue
#             elif sayi > rand:
#                 print("Daha Düşük Bir Sayı Girin.")
#                 continue
#             else:
#                 print("Rastele seçilen sayı : {0}".format(rand))
#                 print("Tahmin sayınız : {0}  ".format(sayac))
#                 print("Harika İş Çıkardın  {0} , kazandınız.Bildiğiniz sayı {1}".format(isim,sayi))  
        
#     elif secenek == "2":
#         print("------ Sınırlı Hak Seçtiniz (5 adet Hakkınız Bulunur) İyi Oyunlar Dileriz------")
#         print()

#         import random
#         import time
#         sayi = random.randint(1,100)
#         tahmin_hakki = 5
#         while True:
#             tahmin = int(input("1 ile 100 arasında değer girin (0 işleniniz geçersiz sayılır ve oyun iptal olur.) : "))
#             if(tahmin==0):
#              print("Oyunu İptal Ettiniz")
#              break

#             if tahmin == sayi:
#              print("Sayı sorgulanıyor... ")
#              time.sleep(1)
#              print("Tebrikler! doğru bildiniz")
#              break
#             elif tahmin > sayi:
#              print("Sayı sorgulanıyor... ")
#              time.sleep(1)
#              tahmin_hakki-=1
#              print("Daha küçük küçük bir sayı giriniz")
#              print("Kalan tahmin hakkı: ",tahmin_hakki)
#             else:
#              print("Sayı sorgulanıyor... ")
#              time.sleep(1)
#              tahmin_hakki -= 1
#              print("Daha büyük bir sayı giriniz")
#              print("Kalan tahmin hakkı: ", tahmin_hakki)
#             if tahmin_hakki == 0:
#              print("KAYBETTİNİZ {0} : ".format(isim))
#              print("Tahmin hakkınız bitmiştir")
#              print("Bilgisayarın tahmini: ",sayi)
#              print("Kendinize Bu Kadar Güvenmeyin :D ")
#              break