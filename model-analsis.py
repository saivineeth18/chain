import mysql.connector as sql
import requests
import time
from datetime import datetime
import pytz


mydb = sql.connect(host="127.0.0.1",user="root",password="",database="test")
print(mydb)