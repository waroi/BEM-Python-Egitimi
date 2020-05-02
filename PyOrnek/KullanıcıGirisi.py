print("**********\nKullanıcı Girişi\n**********\n")
sys_kul_adı = "varol" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı
sys_parola  = "12345" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Parola
giris_hakki = 3
def kullanıcıGiris():
    global giris_hakki
    while True: # Kullanıcı Doğru Giriş Yaptığında ve Giriş Hakkı bittiğinde sona erecek.
        kullanıcı_adı = input("Kullanıcı Adı:")
        parola = input("Parola:")
        if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
            print("Kullanıcı Adı Hatalı...")
            giris_hakki -= 1
            print("Giriş Hakkı: ", giris_hakki)
        elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
            print("Parola Hatalı...")
            giris_hakki -= 1
            print("Giriş Hakkı: ", giris_hakki)
        elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):
            print("Kullanıcı Adı ve Parola Hatalı...")
            giris_hakki -= 1
            print("Giriş Hakkı: ", giris_hakki)
        else:
            print("Başarıyla Giriş Yaptınız...")
            break
        if (giris_hakki == 0 ):
            print("Giriş Hakkınız Bitti...")
            break
kullanıcıGiris()