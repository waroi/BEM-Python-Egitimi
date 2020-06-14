import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")
    buton = QtWidgets.QPushButton(pencere) # pencere objesi için buton oluşturuyoruz
    buton.setText("Burası bir butondur") # butonumuzun yazısını ekliyoruz
    etiket = QtWidgets.QLabel(pencere) # pencere objesi için etiket oluşturuyoruz
    etiket.setText("Merhaba Dünya") # etiketin yazısını yazıyoruz
    etiket.move(200,30) # etiketi konumlandırıyoruz
    buton.move(190,80) # butonu konumlandırıyoruz
    pencere.setGeometry(100,100,500,500) # pencerenin konumu ve boyutlarını ayarlıyoruz
    pencere.show()
    sys.exit(app.exec_())

Pencere()