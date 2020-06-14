import pandas as pd
df=pd.read_csv("covid/covid_19_data.csv")

# a1=df.sort_values(by='Deaths',ascending=False).head(20) #♣ ölüm oranlarının azalan sıralaması (en fazla ölümolan 20 değer)
# print(a1)

# df.drop(34699) # istenilen satırı silmek (tabloya yanısımayacak)
# print(a1)

# df=df.drop(34699) # silme işleminin tabloya yansıması için atama yapmamız gerekir
# a1=df.sort_values(by='Deaths',ascending=False).head(20)
# print(a1)

# df.drop(34035,inplace=True) # istenilen satırı silmek direkt yansır
# a1=df.sort_values(by='Deaths',ascending=False).head(20)
# print(a1)

 
# df=df.drop("SNo",axis=1) # Sütun silmek (eksenin 1 olması gerek)
# print(df.sort_values(by='Deaths',ascending=False).head(20))

# 
# df=df.drop(columns="SNo")  # Sütun silmek (eksenin 1 olması gerek)
# print(df.columns)

# print(df.groupby("Province/State")["Deaths"].mean().head(10)) # şehir ve ortalama ölüm sayılarını gruplama
# print(df.groupby("Province/State")["Deaths"].max().head(10)) #  şehir ve en yüksek ölüm sayılarını gruplama

# print(df.groupby(["Province/State","Country/Region"])["Deaths"].max().head(10)) # ülke, şehir ve göre ölüm gruplama (ilk 10 değer)

# print(df.isnull().sum()) # nan değerlern toplamı

# df["Province/State"].fillna(method="ffill",inplace=True) # nan değerleri doldurmak

# print(df.isnull().sum()) # nan değerlern toplamı

#df=df.drop() # nan değerleri sile (ama diğer bilgilerde uçabilir)

