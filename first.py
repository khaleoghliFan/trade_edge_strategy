import pandas as pd
import numpy as np
import requests
from alpha_vantage.timeseries import TimeSeries
# methods = [method for method in dir(TimeSeries)
#            if callable(getattr(TimeSeries, method))
#            and not method.startswith("__")
#            and TimeSeries.__dict__.get(method)]
#
# print(methods)

api_key="2250Z48PTHVJVFAM"
symbol = "IBM"
interval = "5min"
data_folder="./data"
url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": symbol,
    "interval": interval,
    "apikey": api_key,
    "outputsize": "compact"  # or "full"
}
res=requests.get(url,params=params)
data_j=res.json()
just_5min=data_j["Time Series (5min)"]
frame=pd.DataFrame(just_5min).T
print(frame.info())
