import mysql.connector as sql
import requests
import time
from datetime import datetime
import pytz


mydb = sql.connect(host="127.0.0.1",user="root",password="",database="model")

mycursor = mydb.cursor()
ID = 2
while True:
    # BTC - BUSD
    url = "https://www.binance.com/api/v3/ticker/price?symbol=BTCBUSD"
    response = requests.get(url)
    BUSD = response.json()
    BTC_BUSD = float(BUSD['price'])

    # USD - INR
    url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=0e08f801c6dc90c950b8"
    response = requests.get(url)
    INR = response.json()
    F_USD_INR = float(INR['USD_INR'])
    USD_INR = round(F_USD_INR, 2)

    # BTC - INR
    url = "https://api.wazirx.com/api/v2/tickers"
    response = requests.get(url)
    WX = response.json()
    WRX_BTC_INR = float(WX["btcinr"]['last'])

    F_BIN_BTC_INR = BTC_BUSD * USD_INR
    BIN_BTC_INR = round(F_BIN_BTC_INR, 2)

    F_PROFIT_BTCINR = WRX_BTC_INR - BIN_BTC_INR
    PROFIT_BTCINR = round(F_PROFIT_BTCINR, 2)

    F_PROFIT_PERC = (PROFIT_BTCINR / WRX_BTC_INR) * 100
    PROFIT_PERC = round(F_PROFIT_PERC, 2)

    

    
    curr_time = time.localtime()
    time1 = time.strftime("%H:%M:%S", curr_time)
    
    # time
    tz_NY = pytz.timezone('Asia/Kolkata')   
    datetime_NY = datetime.now(tz_NY)  
    date = datetime_NY.strftime("%Y-%m-%d")


    # print('BTC_BUSD          :', BTC_BUSD)
    # print('USD_INR           :', USD_INR)
    # print('WRX_BTC_INR       :', WRX_BTC_INR)
    # print('BIN_BTC_INR       :', BIN_BTC_INR)
    # print('PROFIT_BTCINR     :', PROFIT_BTCINR)
    # print('PROFIT PERCENTAGE : ' + str(PROFIT_PERC) + '%')

    add_data = ("INSERT INTO price "
                "VALUES (%s,%s, %s, %s, %s, %s,%s,%s,%s)")
    data = (ID,BTC_BUSD,USD_INR, WRX_BTC_INR, BIN_BTC_INR,PROFIT_BTCINR,PROFIT_PERC,date,time1)
    mycursor.execute(add_data, data)
    mydb.commit()
    print("done")
    ID = ID + 1
    time.sleep(90)





