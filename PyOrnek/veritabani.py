# #SQLite veritabanını projemize dahil ederiz
# import sqlite3
# #veritabanı oluşturuyuz
# vt=sqlite3.connect("okul.db")
# #veritabanımıza imlec ekleyerek veritabanımızda işlemlerimizi gerçekleştireceğiz
# islem=vt.cursor()


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


# # Cevap01 Giray:
# import sqlite3
# pl=sqlite3.connect("playList.db")
# play=pl.cursor()
# play.execute("CREATE TABLE IF NOT EXISTS playlist(SanatciAdi TEXT,SarkiAdi TEXT,SarkiSüresi FLOAT)")
# # play.execute("INSERT INTO playlist VALUES('Tarkan','Kuzu Kuzu',3)")
# # pl.commit()
# # play.execute("INSERT INTO playlist VALUES('Zeynep BASTIK','Uslanmıyor Bu',4)")
# # pl.commit()
# # play.execute("INSERT INTO playlist VALUES('Sebnem FERAH','Bugün',5)")
# # pl.commit()
# # play.execute("INSERT INTO playlist VALUES('Sebnem FERAH','Hoşçakal',5.0)")
# # pl.commit()


# play.execute("SELECT * FROM playlist")
# veri=play.fetchall()
# for i in veri:
#     print(i)

# ###Kullanıcının listeye müzik eklemesi
# def addMusic(SanatciAdi,SarkiAdi,SarkiSüresi):
#     play.execute("INSERT INTO playlist VALUES(?,?,?)",(SanatciAdi,SarkiAdi,SarkiSüresi))
#     pl.commit()

# sanatciAdi=input("SanatciAdi:")
# sarkiAdi=input("SarkiAdi:")
# sarkiSüre=float(input("SarkiSüresi:"))
# addMusic(sanatciAdi,sarkiAdi,sarkiSüre)
# pl.close()



# #verileri silme
# play.execute("DELETE FROM playlist WHERE  SarkiAdi='Kuzu Kuzu' ")
# pl.commit()






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