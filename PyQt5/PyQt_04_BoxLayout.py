import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam") # artık pencere içine göndermeden sadece isim vererek butonlarımızı oluturuyoruz
    cancel = QtWidgets.QPushButton("İptal")
    h_box = QtWidgets.QHBoxLayout() # h_box objemizi oluturuyoruz
    h_box.addStretch() # esnek boşluklar yerleştiriyoruz (yatay)
    h_box.addWidget(okay) # h_layout içine butonlarımızı yerleştirdik
    h_box.addWidget(cancel)
    v_box = QtWidgets.QVBoxLayout() # v_box objemizi oluturuyoruz
    v_box.addStretch() # v_layout içine esnek boşluk yerleştirdik (dikey) yerleştirdik
    v_box.addLayout(h_box) # v_layout içine h_layoutu komple yerleştirdik
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")
    pencere.setLayout(v_box) # pencerenin içine en üst layout olan v_box u verdik
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()