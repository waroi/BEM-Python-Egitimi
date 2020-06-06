import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid/covid_19_data.csv")

italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]

plt.hist(italya.Deaths,bins=10)
plt.xlabel("ölüm sayıları")
plt.ylabel("değer aralığı")
plt.title("italya coronavirüs analizi")
plt.show()

plt.hist(ispanya.Deaths,bins=10)
plt.xlabel("ölüm sayıları")
plt.ylabel("değer aralığı")
plt.title("ispanya coronavirüs analizi")
plt.show()