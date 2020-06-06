import pandas as pd

df=pd.read_csv("covid/covid_19_data.csv")
print(df)

# sehir=df["Province/State"] # Şehir bilgisi
# print(sehir)

# us=df[["Province/State","Country/Region"]] # ülke ve şehir bilgileri
# print(us)

# #loc(satır,sütun) 
# c1=df.loc[1] # belli bir satıra ulaşmak
# print(c1)

# c2=df.loc[1:55] # belli satır aralığını almak (son değer dahil)
# print(c2)

# c3=df.loc[:,"Province/State"] # belli bir sütunu almak
# print(c3)

# c4=df.loc[:,["Province/State","Country/Region"]] # iki tane sütun değeri almak
# print(c4)

# c5=df.loc[3:45,["Province/State","Country/Region"]] # iki sütun için belli bir aralıkta satırı almak
# print(c5)

# c6=df.iloc[5] # istenen index değeri
# print(c6)

# c7=df[df.Deaths<10] # ölü sayısı 10 dan küçük olan değerler
# print(c7)

# c8=df[df.Recovered>55] # kurtulan hasta sayısı 55 den büyük olan değerler
# print(c8)