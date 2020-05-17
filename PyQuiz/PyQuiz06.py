# Programlama Ödevi - Nesne Tabanlı Programlama

# Proje 1
# Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.

# Proje 2
# Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
# Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.

# # #cevap01-GİRAY EKER
# class Computer():
#     def __init__(self,marka,islemci,ram,ekranKarti):
#         print("Bilgisayar sınıfının init fonksiyonu çalıştı.")
#         self.marka=marka
#         self.islemci=islemci
#         self.ram=ram
#         self.ekranKarti=ekranKarti
#     def pcBilgileri(self):
#         print(""""
#         BiLGİSAYAR ÖZELLİKLERİ
#         Işlemci:    {}
#         Ram:        {}Gb
#         Ekrankarti: {}Gb
#         Marka:      {}
#         """.format(self.islemci,self.ram,self.ekranKarti,self.marka))
#     def ramArttir(self,ramMiktar):
#             print("PC ram boyutu arttırılıyor.")
#             self.ram+=ramMiktar

# bilgisayar1=Computer("Toshiba","İntel i9",16,2)
# bilgisayar1.pcBilgileri()
# bilgisayar1.ramArttir(16)
# bilgisayar1.pcBilgileri()


# # Cevap 02 - Eren bey:
# class Pc():
#     def __init__(self,ÜrünAilesi,ÜrünSerisi,İsletimSistemi,EkranBoyutu,EkranCözünürlügü,EkranCözünürlükBicimi,
#     Bellek_RAM,İşlemciSerisi):
#         self.ÜrünAilesi = ÜrünAilesi 
#         self.ÜrünSerisi = ÜrünSerisi 
#         self.İsletimSistemi = İsletimSistemi
#         self.EkranBoyutu = EkranBoyutu
#         self.EkranCözünürlügü = EkranCözünürlügü
#         self.EkranCözünürlükBicimi = EkranCözünürlükBicimi
#         self.Bellek_RAM = Bellek_RAM
#         self.İşlemciSerisi = İşlemciSerisi
# pc1 = Pc (ÜrünAilesi = "Asus ZenBook", ÜrünSerisi = "Zenbook UX433" ,İsletimSistemi="Windows 10",EkranBoyutu=14.0,
# EkranCözünürlügü="1920x1080",EkranCözünürlükBicimi="Full HD",Bellek_RAM=16,İşlemciSerisi="Intel Core i7")
# print("Ürün Ailesi = ",pc1.ÜrünAilesi)
# print("Ürün Serisi = ",pc1.ÜrünSerisi)
# print("İsletim Sistemi = ",pc1.İsletimSistemi)
# print("Ekran Boyutu = ",pc1.EkranBoyutu)
# print("Ekran Cözünürlügü = ",pc1.EkranCözünürlügü)
# print("Ekran Cözünürlük Bicimi = ",pc1.EkranCözünürlükBicimi)
# print("Bellek(RAM) = ",pc1.Bellek_RAM)
# print("İşlemci Serisi = ",pc1.İşlemciSerisi)

# Cevap03 Berkay:
# class Bilgisayar():
#     def __init__(self,ram="8 GB",anakart="MSI MEG X399",ekrankarti="MSI gtx 1050 ti",islemci="AMD Ryzen 9 3900X 3.8/4.6GHz AM4",guckaynagi="FSP FSP700-60AHBC PSU"):
#         self.ram= ram
#         self.anakart= anakart
#         self.ekrankarti= ekrankarti
#         self.islemci=islemci
#         self.guckaynagi= guckaynagi

#     def sistemozelliklerinigoster(self):
#         print("Bilgisarın Genel Özellikleri")
#         print("RAM : {} \n ANAKART : {} \n EKRAN KARTI : {} \n İŞLEMCİ : {} \n GÜÇ KAYNAĞI : {} \n.".format(self.ram,self.anakart,self.ekrankarti,
#                                                                                                             self.islemci,
#                                                                                                             self.guckaynagi))
#     def anakart_degistir(self,anakart):
#         print("Anakart değiştirildi ",anakart)
#         self.anakart=anakart
# bilgisayar = Bilgisayar()

# print("""*******************

# Bilgisayar Uygulaması

# İşlemler ;

# 1. Bilgisayar Özellikleri

# 2. Anakart Değiştir

# Çıkmak için 'q' ya basın.
# *******************""")

# while True:
#     işlem = input("İşlemi Seçiniz:")
#     if (işlem == "q"):
#         print("Programdan Çıkılıyor...")
#         break
#     if (işlem == "1"):
#         bilgisayar=Bilgisayar()
#         bilgisayar.sistemozelliklerinigoster()
#     elif (işlem == "2"):
#         anakartlar = input("Eklemek istediğiniz anakartı girin:")
#         bilgisayar.anakart_degistir(anakartlar)



# Proje 3
# Bu projede ise 4 tane sınıfı oluşturun.
# Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
# Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
# Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
# At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.




#----------- Cevap01 - Berkay:
# import time


# class Hayvanlar():
#    def __init__(self, tur="Omurgasızlar ve Omurgalılar", yasamalani="Kara,Hava ve Su",
#                 beslenmecesiti="Etçil , Otçul veya Hem Etçil Hem Otçul", ayaksayisi="2 - 4 Arasında değişmektedir"):
#        self.tur = tur
#        self.yasamalani = yasamalani
#        self.beslenmecesiti = beslenmecesiti
#        self.ayaksayisi = ayaksayisi

#    def bilgilerigöster(self):
#        print("Hayvanların Genel Özellikleri")
#        print(
#            "1)Türü:{}\n2)Yaşam Alanı:{}\n3)Beslenme Çeşiti:{}\n4)Ayak Sayisi : {}\n".format(self.tur, self.yasamalani,
#                                                                                             self.beslenmecesiti,
#                                                                                             self.ayaksayisi))


# class Kopekler(Hayvanlar):
#   def __init__(self, tur="Memeli", yasamalani="Kara", beslenmecesiti="Etçil", ayaksayisi="4",
#                 tipiközellikeri=["Hızlılardır", "Fazla Doğum Yaparlar", "Ömürleri Kısadır"],
#                 cinsleri=["Rotweiler", "Dogo", "Pitbull"]):
#       super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
#       print("Köpek class'ının init fonksiyonu")
#       self.cinsleri = cinsleri
#       self.tipiközellikleri = tipiközellikeri

#   def bilgilerigöster(self):
#       print("Köpeklerin Genel Özellikeri")
#       print("1)Türü:{}\n2)Yaşam Alanı:{}\n3)Beslenme Çeşiti:{}\n4)Ayak Sayisi : {}\n5)Tipik Özellikleri:{}\n6)Cinsleri:{}\n".format(self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi, self.tipiközellikleri, self.cinsleri))

#   def cinsekle(self):
#       cins_listesi = input("Cinsleri araya virgül koyarak giriniz : ")
#       listeler = cins_listesi.split(",")
#       for i in listeler:
#           self.cinsleri.append(i)

#   def özellikekle(self):
#       tipik = input("Aralarına virgül koyarak özelliklerini giriniz.")
#       tipik_listesi = tipik.split(",")
#       for i in tipik_listesi:
#           self.tipiközellikleri.append(i)

#   def __str__(self):
#       return "Özellik sayısı :{}\nCins Sayısı :{}\n".format(len(self.tipiközellikleri), len(self.cinsleri))


# class Kuslar(Hayvanlar):
#   def __init__(self, tur="Memeli", yasamalani="Hava ve Kara", beslenmecesiti="Etçil", ayaksayisi="2",
#               tipiközellikleri=["Uçarlar", "Hızlılardır", "Uçma Mesefaleri 10 Km Çıkabilir"],
#               cinsleri=["Muhabbet Kuşu", "Sultan Papağanı", "Hint Bülbülü", "Amazon Papağanı"]):
#       print("Kuşların init Fonksiyonu")
#       super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
#       self.tipiközellikleri = tipiközellikleri
#       self.cinsleri = cinsleri

#   def bilgilerigöster(self):
#       print("Kuşların Genel Özellikeri")
#       print(
#           "1)Türü:{}\n2)Yaşam Alanı:{}\n3)Beslenme Çeşiti:{}\n4)Ayak Sayisi : {}\n5)Tipik Özellikleri:{}\n6)Cinsleri:{}\n".format(
#               self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi, self.tipiközellikleri, self.cinsleri))

#   def cinsekle(self):
#       cins_listesi = input("Cinsleri araya virgül koyarak giriniz : ")
#       listeler = cins_listesi.split(",")
#       for i in listeler:
#           self.cinsleri.append(i)

#   def özellikekle(self):
#       tipik = input("Aralarına virgül koyarak özelliklerini giriniz.")
#       tipik_listesi = tipik.split(",")
#       for i in tipik_listesi:
#           self.tipiközellikleri.append(i)

#   def __str__(self):
#       return "Özellik sayısı :{}\nCins Sayısı :{}\n".format(len(self.tipiközellikleri), len(self.cinsleri))


# class Atlar(Hayvanlar):
#   def __init__(self, tur="Memeli", yasamalani="Kara", beslenmecesiti="Otçul", ayaksayisi="4",
#               tipiközellikleri=["Hızlılardır", "Nalları Vardır", "Boyları Uzundur"],
#               cinsleri=["Dole pony", "Arap Atı", "İngiliz Atı"]):
#       print("Atlar class'ının init fonksiyonu")
#       super().__init__(tur, yasamalani, beslenmecesiti, ayaksayisi)
#       self.tipiközellikleri = tipiközellikleri
#       self.cinsleri = cinsleri

#   def bilgilerigöster(self):
#       print("Atların Genel Özellikeri")
#       print(
#           "1)Türü:{}\n2)Yaşam Alanı:{}\n3)Beslenme Çeşiti:{}\n4)Ayak Sayisi : {}\n5)Tipik Özellikleri:{}\n6)Cinsleri:{}\n".format(
#               self.tur, self.yasamalani, self.beslenmecesiti, self.ayaksayisi, self.tipiközellikleri, self.cinsleri))

#   def cinsekle(self):
#       cins_listesi = input("Cinsleri araya virgül koyarak giriniz : ")
#       listeler = cins_listesi.split(",")
#       for i in listeler:
#           self.cinsleri.append(i)

#   def özellikekle(self):
#       tipik = input("Aralarına virgül koyarak özelliklerini giriniz.")
#       tipik_listesi = tipik.split(",")
#       for i in tipik_listesi:
#           self.tipiközellikleri.append(i)

#   def __str__(self):
#       return "Özellik sayısı :{}\nCins Sayısı :{}\n".format(len(self.tipiközellikleri), len(self.cinsleri))


# while True:
#    print("""
#    ******************
#    Hayvanlar Aleminin Genel Özellikleri
#    *******************
#    1)Hayvanların Genel Özellikleri
#    2)Köpeklerin Genel Özellikleri
#    3)Kuşların Genel Özellikleri
#    4)Atların Genel Özellikleri
#    5)Çıkış
#    """)
#    seçim = input("İşleminizi Giriniz : ")
#    if seçim == "1":
#        hayvanlar = Hayvanlar()
#        hayvanlar.bilgilerigöster()
#    elif seçim == "2":
#        köpekler = Kopekler()
#        köpekler.bilgilerigöster()
#        time.sleep(1)
#        ber = input("1)Cins Ekleme\n2)Özellik Ekleme\n3)Özellik Ve Cins Sayıları\n4)Çıkış\n")
#        if ber == "1":
#            köpekler.cinsekle()
#        elif ber == "2":
#            köpekler.özellikekle()
#        elif ber == "3":
#            print(köpekler)
#        else:
#            print("Bu menüden Çıkış Yapılıyor")
#            time.sleep(1)
#    elif seçim == "3":
#        kuslar = Kuslar()
#        kuslar.bilgilerigöster()
#        time.sleep(1)
#        ber = input("1)Cins Ekleme \n2)Özellik Ekleme\n3)Özellik Ve Cins Sayıları\n5)Çıkış\n")
#        if ber == "1":
#            kuslar.cinsekle()
#        elif ber == "2":
#            kuslar.özellikekle()
#        elif ber == "3":
#            print(kuslar)
#        else:
#            print("Bu menüden Çıkış Yapılıyor")
#            time.sleep(1)
#    elif seçim == "4":
#        atlar = Atlar()
#        atlar.bilgilerigöster()
#        time.sleep(1)
#        ber = input("1)Cins Ekleme \n2)Özellik Ekleme\n3)Özellik Ve Cins Sayıları\n6)Çıkış\n")
#        if ber == "1":
#            atlar.cinsekle()
#        elif ber == "2":
#            atlar.özellikekle()
#        elif ber == "3":
#            print(atlar)
#        else:
#            print("Bu menüden Çıkış Yapılıyor")
#            time.sleep(1)
#    else:
#        print("İşleminiz Sonlandırılıyor...")
#        time.sleep(1)
#        break