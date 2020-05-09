from datetime import *
dogumTarihi = datetime.strptime(input("Doğum Tarihinizi Gün.Ay.Yıl Olarak Giriniz: "),"%d.%m.%Y")
yas = datetime.now() - dogumTarihi
print("O günden şu ana {} kadar saniye geçmiş ve kalbiniz ortalama {} kez atmış. :)".format(yas.total_seconds(), yas.total_seconds()*80))