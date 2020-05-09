import random
resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]
while True:
    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))
    kelime = random.choice(["ankara", "istanbul", "giresun", "izmir", "antalya", "bursa"])
    adim = 0
    tahmin = []
    while True:
        print(resim[adim])
        for i, char in enumerate(kelime):
            print(char if i in tahmin else "_"),    
        cevap = input("Kelimeyi Tahmin Edin: ")
        if cevap == kelime:
            print("Kazandınız!")
            break
        else:
            while True:
                rastgele = random.randint(0, len(kelime))
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break
            adim += 1
        if adim >= len(resim):
            print("Kaybettiniz!")
            break
    if not "y" == input("Tekrar Oynamak İstermisiniz? (y/n): "):
        break