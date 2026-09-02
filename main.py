import pandas as pd

data=pd.read_csv("stock_data.csv")
data.head(5)
data.shape
data.info()

data["MA5"]=data["Price"].rolling(5).mean()
data["MA20"]=data["Price"].rolling(20).mean()
data[["Date","Price","MA5","MA20"]].tail(10)