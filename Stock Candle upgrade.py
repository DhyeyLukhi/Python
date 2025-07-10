import yfinance as yf
import mplfinance as mpf
import datetime

while True:
    try:
        symbol = input("Enter the name: ")
        data = yf.Ticker(symbol).history(period="1y")

        last_market_price = data['Close'].iloc[-1]

        print(f"Last Price: {last_market_price}")

        startdate = "2024-01-01"
        enddate = datetime.datetime.now().strftime('%F')

        stockdata = yf.download(symbol, start=startdate, end=enddate)

        mpf.plot(stockdata, type="candle", style="yahoo", title=f"{symbol} Candle chart")



    except Exception as e:
        print(e)


        # I have add the last price function in the code which will tell you the last price of the stock