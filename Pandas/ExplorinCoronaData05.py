import pandas as pd

df=pd.read_csv("covid/covid_19_data.csv")
print(df)

# print(df.shape) # Satır ve Sütun sayısı

# print(df.columns) # Kolonlar

# print(df.dtypes) # Data Tipleri

# print(df.head(10)) # ilk 10 satır

# print(df.tail(10)) # Son 10 satır

# print(df.info()) # Genel bilgi

# print(df.isnull().sum()) # Boş bilgilerin sayısı

# print(df.describe()) # Sütunların istatiksel özellikleri (int)

# print(df["Province/State"].describe()) # verilen string sütunun analizi

# a=(df.describe(include=["O"])) # Boş değere sahip olmayan string sütünların analizi
# print(a) 

# b=(df["Country/Region"].value_counts()) # Ülkelere göre veri sayısı
# print(b)

# print(df[df["Province/State"]=="Chicago"]) # Belirtilen şehirdeki  veriler