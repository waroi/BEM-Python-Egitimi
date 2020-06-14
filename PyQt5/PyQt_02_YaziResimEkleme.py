import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1 = QtWidgets.QLabel(pencere) # pencere objesi içerisinde etiket oluşturuyoruz
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("PyQt5/python.png")) # setPixmap içine görseli obje olarak atabilmek için Qpixmap i kullanıp görsel yolunu veriyoruz.
    etiket1.setText("Burası bir yazıdır.") # Label içine yazı yazmak için setText kullanıyoruz.
    etiket1.move(200,30) # etiketin konumu
    etiket2.move(70,100)
    pencere.setGeometry(100,100,500,500) # pencerenin konumu(ilk iki değer x,y konumu diğer ikideğer en boy uzunluğu)
    pencere.show()
    sys.exit(app.exec_())

Pencere()