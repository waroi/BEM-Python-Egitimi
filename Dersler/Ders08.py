# Nesne Tabanlı Programlama

# liste= [1,2,3,4,5,6,7] #liste list class'ından türeyen bir objedir.
# liste.append(6)
# print(liste)
# print(type(liste))

# sozluk = dict() #sozluk dict class'ından türeyen bir objedir.
# print(type(sozluk))

#------------------class base tanımladıklarımız bütün class için geçerli ve her yerde aynıdır.
# class Araba():
#   marka="Citroen"
#   model="Pluriel"
#   renk="Turuncu"
#   beygir=120
#   def __init__(self):
#     print("init fonksiyonu çağırıldı")

# araba1=Araba()
# print(araba1)
# print(type(araba1))
# print(araba1.marka)
# print(araba1.model)
# print(araba1.renk)
# print(araba1.beygir)
# araba2=Araba()
# print(araba2.marka)
# print(araba2.model)
# print(araba2.renk)
# print(araba2.beygir)
# print(dir(araba1))
#----------------------------init ile özellik tanımlama
# class Araba():
#   def __init__(self,marka,model,renk,beygir):
#     print("init fonksiyonu çağırıldı")
#     self.marka=marka
#     self.model=model
#     self.renk=renk
#     self.beygir=beygir

# araba1=Araba("Citroen","Pluriel","Turuncu",120)
# araba2=Araba("Ford","Musteng","Kırmızı",300)
# print(araba1.marka)
# print(araba1.model)
# print(araba1.renk)
# print(araba1.beygir)
# print(araba2.marka)
# print(araba2.model)
# print(araba2.renk)
# print(araba2.beygir)


# #------------------init ile varsayılan değer ile birlikte tanımlama
# class Araba():
#   def __init__(self,marka="Bilgi Yok",model="Bilgi Yok",renk="Bilgi Yok",beygir=70):
#     print("init fonksiyonu çağırıldı")
#     self.marka=marka
#     self.model=model
#     self.renk=renk
#     self.beygir=beygir

# araba1=Araba(renk="Siyah")
# araba2=Araba(marka="Ferrari",renk="Kırmızı",beygir=300)
# print(araba1.marka)
# print(araba1.model)
# print(araba1.renk)
# print(araba1.beygir)
# print(araba2.marka)
# print(araba2.model)
# print(araba2.renk)
# print(araba2.beygir)

# -----------------------------Metod oluşturma
# class Yazilimci():
#   def __init__(self,isim,soyisim,numara,maas,diller):
#     self.isim=isim
#     self.soyisim=soyisim
#     self.numara=numara
#     self.maas=maas
#     self.diller=diller
#   def bilgileriGoster(self):
#     print("""
#     Çalışan Bilgisi:
#     İsim: {}
#     Soyisim: {}
#     Şirket Numarası: {}
#     Maaş: {}
#     Diller: {}
#     """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
#   def dilEkle(self,yeniDil):
#     print("Dil Ekleniyor...")
#     self.diller.append(yeniDil)
#   def maasZam(self,zamMiktar):
#     print("Maaş zammı uygulanıyor...")
#     self.maas+=zamMiktar
# yazilimci1=Yazilimci("Varol","Maksutoğlu",62514654,15000,["Python","Javasript","C#","Java"])
# yazilimci2=Yazilimci("Berkay","Çabuk",65465466,20000,["Python","C#","Java"])
# # print(yazilimci1.diller)
# # print("-------------------------------")
# # print(yazilimci2.diller)
# # yazilimci1.bilgileriGoster()
# # yazilimci2.bilgileriGoster()
# yazilimci2.dilEkle("Javascript")
# yazilimci2.maasZam(1000)
# yazilimci2.bilgileriGoster()


#-------------------------------Overriding(iptal etme - ezme)
# class Calisan():
#   def __init__(self,isim,maas,departman):
#     print("Çalışan sınıfının init fonksiyonu çalıştı")
#     self.isim=isim
#     self.maas=maas
#     self.departman=departman
#   def bilgileriGoster(self):
#     print("""
#     Çalışan Bilgisi:
#     İsim: {}
#     Maaş: {}
#     Departman: {}
#     """.format(self.isim,self.maas,self.departman))
#   def departmanDegistir(self,yeniDepartman):
#     print("Departman Değiştiriliyor...")
#     self.departman=yeniDepartman
# class Yonetici(Calisan):
#   def __init__(self,isim,maas,departman,kisiSayisi):
#     print("Yönetici sınıfının init fonksiyonu çalıştı")
#     self.isim=isim
#     self.maas=maas
#     self.departman=departman
#     self.kisiSayisi=kisiSayisi
#   def zamYap(self,zamMiktar):
#     print("Maaşa Zam Yapılıyor")
#     self.maas+=zamMiktar
# yonetici1=Yonetici("Varol Maksutoğlu",14000,"Yazılım",10)
# yonetici1.departmanDegistir("Yönetim")
# yonetici1.zamYap(500)
# yonetici1.bilgileriGoster()




class Calisan():
  def __init__(self,isim,maas,departman):
    print("Çalışan sınıfının init fonksiyonu çalıştı")
    self.isim=isim
    self.maas=maas
    self.departman=departman
  def bilgileriGoster(self):
    print("""
    Çalışan Bilgisi:
    İsim: {}
    Maaş: {}
    Departman: {}
    """.format(self.isim,self.maas,self.departman))
  def departmanDegistir(self,yeniDepartman):
    print("Departman Değiştiriliyor...")
    self.departman=yeniDepartman
class Yonetici(Calisan):
  def __init__(self,isim,maas,departman,kisiSayisi):
    super().__init__(isim,maas,departman)
    print("Yönetici sınıfının init fonksiyonu çalıştı")
    self.kisiSayisi=kisiSayisi
  def zamYap(self,zamMiktar):
    print("Maaşa Zam Yapılıyor")
    self.maas+=zamMiktar
yonetici1=Yonetici("Varol Maksutoğlu",14000,"Yazılım",10)
yonetici1.departmanDegistir("Yönetim")
yonetici1.zamYap(500)
yonetici1.bilgileriGoster()
