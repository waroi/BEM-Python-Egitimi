import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid/covid_19_data.csv")

türkiye=df[df["Country/Region"]=="Turkey"]
italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]

plt.scatter(türkiye.Deaths,türkiye.Recovered,color="red",label="Türkiyedeki ölen-kurtulan hasta sayıları") # scatterile birden fazla datayı aynı anda inceleyebiliriz
plt.scatter(italya.Deaths,italya.Recovered,color="blue",label="İtalyadaki ölen-kurtulan hasta sayıları")
plt.scatter(ispanya.Deaths,ispanya.Recovered,color="black",label="İspanyadaki ölen-kurtulan hasta sayıları")

plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı") 
plt.title("Dünyadaki Coronavirüs Analizi") 
plt.legend()
plt.show()  
 