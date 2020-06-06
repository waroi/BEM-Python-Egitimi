import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid/covid_19_data.csv")

# df.plot()
# plt.show() # grafiği gösterme (sadece int geğerler)

# df=df.drop("SNo",axis=1) # sno sütununu silme
# df.plot()
# plt.show()

# türkiye=df[df["Country/Region"]=="Turkey"] # türkiyede hangi şehirlerde corona görülüyor
# print(türkiye.columns)

# plt.plot(türkiye.Deaths,türkiye.Recovered,color="red",label="Türkiyede ölen-kurtulan hasta sayıları")
# plt.xlabel("Ölüm sayısı")
# plt.ylabel("Kurtulan hasta sayısı")
# plt.title("Türkiyedeki Coronavirüs Analizi")
# plt.legend() # etiketi en uygun yere yerleştirir
# plt.show()


# df.plot(grid=True,linestyle=":") # grafik biçimlendirme
# plt.show()
















