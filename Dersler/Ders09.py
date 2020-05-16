# Iteretor oluşturma

liste = [1,2,3,4,5,6,7]
# print(dir(liste))

# for i in liste: #for ile iterasyona girme
#   print(i)

# iterator = iter (liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Normal bir liste oluşturma, RAM'de yer tutuyor
# def carp():
#   sonuc=[]
#   for i in range(0,10):
#     sonuc.append(i*2)
#   return sonuc
# print(carp())


# Generator ile liste oluşturma RAM'de tutulmaz
def carp():
  sonuc=[]
  for i in range(1,10):
    yield i*2
generator=carp()
for i in generator:
  print(i)