import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("stock_data.csv")
print(data.head(5))
print(data.shape)
print(data.info())

data["MA5"]=data["Price"].rolling(5).mean()
data["MA20"]=data["Price"].rolling(20).mean()
print(data[["Date","Price","MA5","MA20"]].tail(10))




plt.plot(data["Date"],data["Price"],label="Price")
plt.plot(data["Date"],data["MA5"],label="MA5")
plt.plot(data["Date"],data["MA20"],label="MA20")
plt.xlabel("Date")
plt.ylabel("Price and Rolling Averages (Dollars)")
plt.title("Changes in Price and Rolling Averages over 60 Days")
plt.legend()
plt.show()

plt.figure()
plt.plot(data["Date"],data["Rolling_volatility"]*50,label="Rolling_volatility")
plt.plot(data["Date"],data["Price"],label="Price")
plt.xlabel("Date")
plt.ylabel("Rolling Volatility")
plt.title("Change in Rolling Volatility over 60 Days")
plt.legend()
plt.show()

data["Peak"]=data["Price"].cummax()

print(data[["Price","Peak"]])

data["Drawdown"]=(data["Price"]-data["Peak"])/data["Peak"]
print(data[["Date","Price","Peak","Drawdown"]])

max_drawdown=data["Drawdown"].min()

plt.figure()
plt.plot(data["Date"],data["Drawdown"],legend="drawdown")
plt.xlabel("Date")
plt.ylabel("Drawdowns")
plt.title("Looking at Drawdowns over the Course of 60 Days")
plt.legend()
plt.show()
