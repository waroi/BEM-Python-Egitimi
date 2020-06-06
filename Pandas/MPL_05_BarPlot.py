import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid/covid_19_data.csv")

# türkiye=df[df["Country/Region"]=="Turkey"]
# plt.bar(türkiye.Deaths,türkiye.Recovered)
# plt.show()

# sayı=np.array([1,2,3,4,5,6,7,8,9])
# karesi=sayı**2
# plt.bar(sayı,karesi)
# plt.xlabel("sayı değeri")
# plt.ylabel("sayının karesi")
# plt.title("sayıların karesini alma")
# plt.show()


# ülke=["Türkiye","Abd","Almanya","İtalya","İspanya","Fransa","Güney Kore","Japonya","UK","Çin","Hindistan"]
# oran=[40,34.7,29.2,12.5,11.6,10.6,9.7,7.3,6.6,3.6,2.3]
# plt.xlabel("Ülkeler")
# plt.ylabel("Oranlar")
# plt.title("yoğun bakım yatak sayısı")
# plt.bar(ülke,oran)
# plt.show()