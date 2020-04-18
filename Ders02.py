# string parametreleri
# a="string ifade"
# print(a.upper()) # bütün karakterleri büyütür
# a="String İfade"
# print(a.swapcase()) # küçük karakterler büyük büyükler küçülür
# a="STRİNG İfade"
# print(a.lower()) # bütün karakterleri küçültür

# print("Bilişim Eğitim Merkezi",end="***\n")
# print("Bilişim Eğitim Merkezi")
# print("Bilişim Eğitim Merkezi")

# print("www","github","com",sep=".")
# print(*"PYTHON",sep="\n")

# liste veri tipi tanımlama: int, float, string ve liste veri tipleri barındırabilir. Yani iç içe listelerde yapabiliriz.
# ornekListe=[2,5,4.3,"python","deneme", ["ikinci","liste",56]] 
# print(len(ornekListe))
# print(ornekListe[3])

# a="ornek"
# print(type(a))
# print(a)
# b=list(a) # değişken içindeki ifadeyi karakter dizisi olarak listeye dönüştürme.
# print(b)
# print(type(b))
# print(b[2])

# a=48
# ornekListe=[2,5,4.3,"python","deneme", "deneme", ["ikinci","liste",56]]
# ornekListe.insert(0,"Liste")
# ornekListe.insert(2,a) # insert ile liste içerisine istediğimiz index için bir eleman ekleyebiliriz.
# ornekListe.remove("deneme") # remove ile liste içerisinden istediğiniz elemanı silebilirsiniz.
# ornekListe.pop(5) # pop ile istediğiniz indexteki elemanı silebilirsiniz, index vermezseniz son elemanı siler.
# print(ornekListe)

# gunler=["pazartesi","salı","carşamba","perşembe","cuma","cumartesi","pazar"]
# gunler.sort() # sort ile stringleri alfabetik sıralayabiliyoruz.
# print(gunler)

gunler=["pazartesi","salı","carşamba","perşembe","cuma","cumartesi","pazar","cuma"]
# print(gunler.index("cuma"))
# gunler.reverse() # reverse listenin sıralamasını tam tesine çevirir.
# print(gunler.index("cuma")) #index içerine verilen elamanın listede kaçıncı sırada olduğunu verir.
# print(gunler.count("cuma")) #count elamanın liste içinde kaç kere kullanıldığını verir.
# print(gunler)
gunler2=gunler.copy()
# print(gunler2)
gunler2.clear()
print(gunler2)
