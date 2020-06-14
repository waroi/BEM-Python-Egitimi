import sys # sistem komutlarına ulaşmakiçin 
from PyQt5 import QtWidgets # PyQt5 modülünden widget classını çağırıyoruz.

def Pencere(): # fonksiyonumuzu oluşturuyoruz
    app = QtWidgets.QApplication(sys.argv)  # app oluşturuluyor
    pencere = QtWidgets.QWidget() # pencere objemizi oluşturuyoruz
    pencere.setWindowTitle("PyQt5 Ders 1") # pencere objemize başlık verdik
    pencere.show() # penceremizi gösterdik
    sys.exit(app.exec_()) # uygulamamızı döngüye sokuyoruz

Pencere() # fonksiyonumuz çalıştırıyoruz