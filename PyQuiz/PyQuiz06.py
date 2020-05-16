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



# Proje 3
# Bu projede ise 4 tane sınıfı oluşturun.
# Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
# Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
# Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
# At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
