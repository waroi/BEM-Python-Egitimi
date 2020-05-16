#SQLite veritabanını projemize dahil ederiz
import sqlite3
#veritabanı oluşturuyuz
vt=sqlite3.connect("okul.db")
#veritabanımıza imlec ekleyerek veritabanımızda işlemlerimizi gerçekleştireceğiz
islem=vt.cursor()


# islem.execute("CREATE TABLE Kitaplık(İsim TEXT,Yazar TEXT, YayınEvi TEXT,SayfaSayısı INT)") 
# eğer tablo varsa hata verir bu yüzden aşağıdaki yöntemi kullanabiliriz.

# #tablomuzu oluşturuyoruz
# islem.execute("CREATE TABLE IF NOT EXISTS ogrenci (adı TEXT, soyadı TEXT, numara INT)")
# #tablomuza eleman ekliyoruz
# islem.execute("INSERT INTO ogrenci VALUES('varol','maksutoglu',5)")
# vt.commit()#yapılan işlemin veritabanıda gerçekleştirilmesi sağlanır
# islem.execute("INSERT INTO ogrenci VALUES('deniz','toprak',6)")
# vt.commit()#yapılan işlemin veritabanıda gerçekleştirilmesi sağlanır


"""
#fonksiyon ile tablomuzu oluşturup ınput ile kullanıcıdan veri alarak tablo doldurmak
def tablo():
    imlec.execute("CREATE TABLE IF NOT EXIST müze (isim TEXT, adres TEXT, ücret INT)")
    con.commit()
    
def ankara():
    imlec.execute("INSERT INTO müze VALUES('Rahmi Koç Müzesi','Altındağ',5)")
    con.commit()

def istanbul(isim,adres,ücret):
    imlec.execute("INSERT INTO müze VALUES(?,?,?)",(isim,adres,ücret))
    con.commit()
                  
isim=input("isim:")
adres=input("adres:")
ücret=int(input("ücret:"))
istanbul(isim,adres,ücret)
con.close()
"""





# #tablodan verileri okumak
# islem.execute("SELECT*FROM ogrenci")
# vt.commit()


# #liste halinde verileri okur
# islem.execute("SELECT * FROM ogrenci")
# veri=islem.fetchall()
# print(veri)
# print()


# #verileri sıralı daha düzgün okuturuz
# islem.execute("SELECT * FROM ogrenci")
# veri=islem.fetchall()
# for i in veri:
#     print(i)


# #istenilen veriyi alırız
# islem.execute("SELECT adı FROM ogrenci")
# veri=islem.fetchall()
# for i in veri:
#     print(i)


# #istenilen sütunu al
# islem.execute("SELECT * FROM ogrenci WHERE adı='varol' ")
# veri=islem.fetchall()
# for i in veri:
#     print(i)    


# #verileri güncelleme
# islem.execute("UPDATE ogrenci SET numara = 12 WHERE  adı='varol' ")
# vt.commit()


# #verileri silme
# islem.execute("DELETE FROM ogrenci WHERE  adı='varol' ")
# vt.commit()


# # veritabanımızı kapatırız
# vt.close()



# Ödev 1: Müzik veri tabanı içerisinde Playlist bir tablo olacak, içerisine şarkılar kayıt edeceğiz(sanatçı adı, şarkı adı, süre.... Vs.)

# Ödev 2:

"""
#fonksiyon ile tablomuzu oluşturup ınput ile kullanıcıdan veri alarak tablo doldurmak
def tablo():
    imlec.execute("CREATE TABLE IF NOT EXIST müze (isim TEXT, adres TEXT, ücret INT)")
    con.commit()
    
def ankara():
    imlec.execute("INSERT INTO müze VALUES('Rahmi Koç Müzesi','Altındağ',5)")
    con.commit()

def istanbul(isim,adres,ücret):
    imlec.execute("INSERT INTO müze VALUES(?,?,?)",(isim,adres,ücret))
    con.commit()

isim=input("isim:")
adres=input("adres:")
ücret=int(input("ücret:"))
istanbul(isim,adres,ücret)
con.close()
"""