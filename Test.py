# API from Alphavantage.co/
import requests
from statistics import mean
x = input("Choose Your symbol: ")
y = input("Input Date (yyyy-mm-dd): ")

# Can Change outputsize to compact, to reduce the amount of data


def fin_parse(x):
    req = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol={x}&apikey=EnterKeyHere")
    find = req.json()
    j = find['Time Series (Daily)'][y]
    a = float(j['1. open'])
    b = float(j['2. high'])
    c = float(j['3. low'])
    d = float(j['4. close'])
    print(f"Open: {a}")
    print(f"High: {b}")
    print(f"low: {c}")
    print(f"Close: {d}")
    print(f"Avg: {mean([b, c])}")


fin_parse(x)
