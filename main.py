import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("stock_data.csv")
data.head(5)
data.shape
data.info()

data["MA5"]=data["Price"].rolling(5).mean()
data["MA20"]=data["Price"].rolling(20).mean()
data[["Date","Price","MA5","MA20"]].tail(10)




plt.plot(data["Date"],data["Price"],label="Price")
plt.plot(data["Date"],data["MA5"],label="MA5")
plt.plot(data["Date"],data["MA20"],label="MA20")
plt.xlabel("Date")
plt.ylabel("Price and Rolling Averages (Dollars)")
plt.title("Changes in Price and Rolling Averages over 60 Days")
plt.legend()
plt.show()

plt.figure()
plt.plot(data["Date"],data["Rolling_volatility"],label="Rolling_volatility")
plt.xlabel("Date")
plt.ylabel("Rolling Volatility")
plt.title("Change in Rolling Volatility over 60 Days")
plt.legend()
plt.show()