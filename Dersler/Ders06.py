# Gömülü Fonksiyonalar
# a=10
# print(type(a))

# map() fonksiyonu
# def carp(x):
#   return x*2
# a=map(carp, [1,2,3,4,5,6,7,8,9])
# print(list(a))

# lambda ile map kullanımı
# a=map(lambda x:x*2,[1,2,3,4,5])
# print(list(a))

# liste1=[1,2,3,4,5]
# liste2=[6,7,8,9,10]
# liste3=[3,1,6,4,2]
# carpim=map(lambda x,y,z:x*y*z,liste1,liste2,liste3)
# print(list(carpim))

# reduce() Fonksiyonu
# from functools import reduce
# toplam=reduce(lambda x,y:x+y,[1,2,3,4,5])
# print(toplam)

# filter() Fonksiyonu
# print(list(filter(lambda x:x%2==0,range(1,11))))

# zip() onksiyonu
# liste1=[1,2,3,4,5,6,7,8]
# liste2=[6,7,8,9,10,4,6,7]
# liste3=["Ankara","İstanbul","Giresun","Muğla","İzmir"]
# print(list(zip(liste1,liste2,liste3)))

# all() Fonksiyonu bir tane bile false olursa Flase döner
# liste=[1,2,3,4,5,"Python",True]
# print(all(liste))

# any() Fonksiyonu bir tane bile true olsa True döner
# liste=[True,False,False,False,1,2,"Python",0]
# print(any(liste))