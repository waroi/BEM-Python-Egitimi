# Eren bey
# baslik="TodoList Uygulaması".center(50,"*")
# print(baslik)
# name = '' # False
# while  not name.strip(): #burada isim girene kadar size isminizi giriniz der ve space bassanız kabul etmez
#     name = input('isminizi giriniz: ')
# print(f'Merhaba, {name} TodoList Uygulamasına Hoşgeldiniz.')
# print("""******************************************
# ----------------İşlem Listesi---------
# 1. Yeni Plan Ekle
# 2. Hazır Olan Planların Bir Kaçını Sil
# 3. Tüm Planları Sil
# 4. Güncel Planları Göster
# 5. Çıkış Yapar 
# 7. Güncel Planları İstedğin Gibi Sırala ve Çağır
# 8. İlk Kaç Plan Görmek İstersin
# """)
# import time
# import sqlite3
# tdl=sqlite3.connect("todolst.db")
# todolst=tdl.cursor()
# while True:
#     import time
#     secenek = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz : ")
#     if secenek == "5":
#         print("Çıkış Yapılıyor...")
#         time.sleep(1)
#         print("Çıkış Yapıldı Görüşmek Üzere")
#         quit()

#     if secenek == '1':
        
#         print("Plan Eklem Sayfasına Yönlendiriliyor...")
#         time.sleep(1)
#         print("Yeni Plan Ekleme Sayfasına Hoşgeldiniz  ".center(50,"*"))
        
#         todolst.execute("CREATE TABLE IF NOT EXISTS todolst(Plan_Numarasi,Yapılacak_Planlar,Tarih,Gün,Saat )")
#         tdl.commit()
#         def veri_ekleme(Plan_Numarasi,Yapılacak_Planlar,Tarih,Gün,Saat):
#             todolst.execute("INSERT INTO todolst VALUES(?,?,?,?,?)",(Plan_Numarasi,Yapılacak_Planlar,Tarih,Gün,Saat))
#             tdl.commit()
#         print("Yeni Planınız Nedir".center(100,"*"))
#         Plan_Numarasi=input("Plan Numaranız Kaç olsun : ")
#         Yapılacak_Planlar =input("Yeni Planınız : ")
#         Tarih = input("Yeni Planınızın Tarihi : ")
#         Gun = input("Yeni Planınızın Günü: ")
#         Saat = input("Yeni Planınızın Saati : ")
#         time.sleep(1)
#         veri_ekleme(Plan_Numarasi,Yapılacak_Planlar,Tarih,Gun,Saat)

#         print("Yeni Planlarınız Listeye Eklendi.")


#     elif secenek == "2":
#         print("Hazır Olan Planların Sayfasına Yönlendiriliyor...")
#         time.sleep(1)
#         print()
#         print("Silmek İstediğiniz Plan Numarası Sayfasına Hoşgeldiniz ".center(100,"*"))
#         secenek2 = input("Lütfen Silmek İstediğiniz Plan Numarasınız Yazınız : ")
#         if secenek2 == "1":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='1'")
#             tdl.commit()
#         elif secenek2 == "2":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='2'")
#             tdl.commit()
#         elif secenek2 == "3":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='3'")
#             tdl.commit()    
#         elif secenek2 == "4":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='4'")
#             tdl.commit()
#         elif secenek2 == "5":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='5'")
#             tdl.commit()
#         elif secenek2 == "6":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='6'")
#             tdl.commit()
#         elif secenek2 == "7":
#             todolst.execute("DELETE FROM todolst WHERE Plan_Numarasi='7'")
#             tdl.commit()

#     elif secenek == "3":
#         print("Tüm Planları Silme Sayfasına Yönlendiriliyor...")
#         time.sleep(1)
#         evetmihayirmi=input("Tüm Planları Silmek İstediğnizden Emin Misiniz :Evet ise ('E') Hayır ise ('H') basınız : ")
#         if evetmihayirmi=="e" or evetmihayirmi=="E":
#             print("Tüm planlarınız Siliniyor...")
#             time.sleep(1)
#             todolst.execute("DELETE FROM todolst")
#             tdl.commit()
            
            
            
#             print("Tüm planlarınız silindi.")
#         elif evetmihayirmi=="h" or evetmihayirmi=="H":
#             print("İşleminiz İptal Ediliyor...")
#             time.sleep(1)
#             print("İşleminiz iptal Edilmiştir ")
            
        
     
#     elif secenek == "4":
#         print("Güncel Plan Sayfasına Yönlendiriliyor...")
#         time.sleep(1)
#         print("Güncel Plan Sayfasına Hoşgeldiniz  ".center(100,"*"))  
#         todolst.execute("SELECT * FROM todolst")
#         veri=todolst.fetchall()
#         for i in veri:
#             print(i)
        

#     # elif secenek == "6":
#     #     print("Güncelleme Sayfası")
#     #     time.sleep(1)
#     #     print()
#     #     print("Güncelleme Yapmak İstediğiniz İşlemi Seçiniz ".center(100,"*"))
#     #     secenek3 = input("\n1.Plan_Numarasi \n2.Yapılacak_Planlar \n3.Tarih \n4.Gun \nSaat\n ------> : ")
#     #     if secenek3 == "1":
#     #         print("Plan_Numarasi Güncellemesine Hoşgeldiniz Hangi Plan Numarasını Değiştirmek İstiyorsumuz".center(50,"*"))
#     #         x=input("Değiştirmek İstedeğin Plan Numarası : ")
#     #         y=input("Plan Numarası Kaç Olsun : ")
#     #         todolst.execute("UPDATE todolst SET y='?' WHERE x='?' ")
#     #         tdl.commit
#     #         time.sleep(1)

#     elif secenek == "7":#Güncel Planları İstedğin Gibi Sırala ve Çağır
#         print("Güncel Planları İstediğin Gibi Listeleme Kısmını Hoşgeldiniz ")
#         secenek3=input("\n1.Saat (En Erken Saatten En Geç Saate Göre Sıralar) \n2.Saat(En Geç Saatten En Erken Saate Göre Sıralar)\n3.Tarih (En Geç Saatten En Erken Saate Göre Sıralar) \n4.Tarih(En Erken Saatten En Geç Saate Göre Sıralar) : ")
#         if secenek3 == "1":
#             print("En Erken Saatten En Geç Saate Göre Sıralanıyor...") 
#             time.sleep(1)
#             print("En Erken Saatten En Geç Saate  ".center(100,"*")) 
#             todolst.execute("SELECT * FROM todolst ORDER BY Saat DESC")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)
            
#         elif secenek3 == "2":
#             print("En Geç Saatten En Erken Saate Göre Sıralanıyor...")
#             time.sleep(1)
#             print("En Geç Saatten En Erken Saate  ".center(100,"*")) 
#             todolst.execute("SELECT * FROM todolst ORDER BY Saat ")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)
#         elif secenek3 == "3":
#             print("En Geç Tarihden En Erken Tarihe Göre Sıralanıyor...")
#             time.sleep(1)
#             print("En Geç Tarihten En Erken Tarihe  ".center(100,"*")) 
#             todolst.execute("SELECT * FROM todolst ORDER BY Tarih ")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)
#         elif secenek3 == "4":
#             print("En Erken Tarihden En Geç Tarihe Göre Sıralanıyor...")
#             time.sleep(1)
#             print("En Erken Tarihden En Geç Tarihe  ".center(100,"*")) 
#             todolst.execute("SELECT * FROM todolst ORDER BY Tarih DESC")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)

#     elif secenek == "8": #İlk Kaç Plan Görmek İstersin
#         print("Güncel Olan İlk Kaç Planı Göstermek İstiyorsunuz")
#         secenek4=input(" 1)ilk 1 \n2) İlk 2 \n3) İlk 3\n4) İlk 4\n5) İlk 5\n6) İlk 6\n7) İlk 7\n8) İlk 8\n9) İlk 9 : ")
#         if secenek4=="1":
#             print("Güncel İlk Planınız Gösteriliyor...")
#             print("Güncel İlk Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,1")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)
#         elif secenek4=="2":
#             print("Güncel İlk 2 Planınız Gösteriliyor...")
#             print("Güncel İlk 2 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,2")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  

#         elif secenek4=="3":
#             print("Güncel İlk 3 Planınız Gösteriliyor...")
#             print("Güncel İlk 3 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,3")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  
#         elif secenek4=="4":
#             print("Güncel İlk 4 Planınız Gösteriliyor...")
#             print("Güncel İlk 4 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,4")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  
#         elif secenek4=="5":
#             print("Güncel İlk 5 Planınız Gösteriliyor...")
#             print("Güncel İlk 5 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,5")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  
#         elif secenek4=="6":
#             print("Güncel İlk 6 Planınız Gösteriliyor...")
#             print("Güncel İlk 6 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,6")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  
#         elif secenek4=="7":
#             print("Güncel İlk 7 Planınız Gösteriliyor...")
#             print("Güncel İlk 7 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,7")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)  
#         elif secenek4=="8":
#             print("Güncel İlk 8 Planınız Gösteriliyor...")
#             print("Güncel İlk 8 Planınız  ".center(100,"*"))
#             todolst.execute("SELECT * FROM todolst LIMIT 0,8")
#             tdl.commit()
#             veri=todolst.fetchall()
#             for i in veri:
#                 print(i)   

#     else:
#         print("Lütfen Ekrandaki Rakamları Tuşlanıyınız")


# İpek Hanım
# Ödev: ToDo uygulaması yapın. Yapılacaklar listesi, listeye eleman eklenebilecek, 
# listeden istenilen elemanı silebilecek, Listenin görüntülenmesi

# import sqlite3

# connection = sqlite3.connect("toDoList.db")
# toDolist = connection.cursor()

# def create_db():
#     toDolist.execute("CREATE TABLE IF NOT EXISTS toDoList(Id INTEGER, Task TEXT, Due TEXT, Status INTEGER)")

# def insert_task():
#     print("New Task\n")
#     Id = int(input("Enter Id: "))
#     Task = input("Enter Task: ")
#     Due = input("Enter Due Date: ")
#     Status = int(input("Enter Status: "))

#     toDolist.execute("INSERT INTO toDoList VALUES(?, ?, ?, ?)", (Id, Task, Due, Status))
#     connection.commit()

# def select_task():  #   Aradığım Id tabloda yok ise şeklinde bir koşul nasıl ekleyebilirim ?
#     Id = input("Enter task Id to select: ")
#     toDolist.execute("SELECT * FROM toDoList WHERE Id=?",(Id))
#     data = toDolist.fetchall()
#     for row in data:
#         print("Id: " ,row[0])
#         print("Task: " ,row[1])
#         print("Due: " ,row[2])
        
# def display_record():
#     toDolist.execute("SELECT * FROM toDoList")
#     data = toDolist.fetchall()
#     print("Veriler:")
#     for i in data:
#         print(i)

# def delete_record():    # silme işlemi bittikten sonra display_record() fonksiyonunu çağırdığım zaman çalışmıyor ?
#     deleteId = input("Enter task Id to delete: ")
#     toDolist.execute("DELETE FROM toDoList WHERE Id=?",(deleteId))
#     connection.commit()
#     print("Delete...")
#     display_record()

# create_db()
# while True:
#     target = input("Select option: \n1. New Task\n2. Select Task\n3. Display Task\n4. Delete Tasks\nQ Quit\n")

#     if target == '1':
#         insert_task()
#     elif (target == '2'):
#         select_task()
#     elif target == '3':
#         display_record()
#     elif target == '4':
#         delete_record()
#     elif (target == "q" or target == "Q"):
#         connection.close()
#         print("Exit...")
#         break