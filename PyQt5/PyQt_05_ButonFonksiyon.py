import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget): #Pencere classımızı oluşturuyoruz (QtWidgets.QWidget'tan miras alıyoruz)
    def __init__(self): # init de kendi metodumuzu çağırdığımız için mirası ezmiş oluyoruz, 
        super().__init__() # bunun için super ile miras aldığımız initi çağırıyoruz.
        self.init_ui() # kendi metodumuzu çağırıyoruz
    def  init_ui(self): # metodumuzu yazıyoruz
        self.yazı_alanı = QtWidgets.QLabel("Bana henüz tıklanmadı..")
        self.buton = QtWidgets.QPushButton("Bana Tıkla")
        self.say = 0 # sayacı sofordan başlattık
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click) # buton tıklandığında click metodunu çağırıyoruz
        self.show()
    def click(self):
        self.say += 1 # sayacımızı artırıyoruz
        self.yazı_alanı.setText("Bana " + str(self.say) + " defa tıklandı.") # label'a tıklama sayısını yazdırıyoruz.
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere() # Pencere classından bir pencere objesi oluşturuyoruz.
sys.exit(app.exec_())