import  sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    def baglanti_olustur(self): # Database bağlantısı oluşturuyoruz, database yoksa yeni oluşturuyor
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        baglanti.commit()
    def init_ui(self):
        self.kullanici_adi =  QtWidgets.QLineEdit() #kullanıcı adı ve parola alıyoruz kullanıcıdan
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) # parolayı gizliyoruz
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login) # tıklandığında metod çağırılıyor
        self.show()
    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()
        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par)) # girilen değerler ile tabloda arama yapılıyor
        data = self.cursor.fetchall() # tabloda veri varsa data içine atıyor
        if len(data) == 0: # verinin uzunluğu sıfırsa tabloda yok demektir, kullanıcı yok uyarısı veriyoruz
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else: # veri gelirse, kullanıcıyı selamlıyoruz
            self.yazi_alani.setText("Hoşgeldiniz " + adi)
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())