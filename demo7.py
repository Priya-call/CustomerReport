import  mysql.connector
import pandas as pd
import psycopg2
import json

conn =  mysql.connector.connect(user='root', password='root',
                          host='localhost', database='northwind')  

connpg =  psycopg2.connect(user='gismaster', password='first#1234',
                          host='aim-postgredb.caleitwp8flw.us-east-2.rds.amazonaws.com', database='northwind') 

connpg.autocommit = True
curpg = connpg.cursor()

cur = conn.cursor()
cur.execute("SELECT * FROM result")

rows = cur.fetchall()   
alldata = ''
print(rows)

rowLength = len(rows)
rowRange = rowLength - 1
a = []

for item in range(0, rowLength):
    if(item == rowRange):    
      #alldata = alldata + ("{" + f"  \"first_name\":\"{r[0]}\",\"id\":\"{r[1]}\",\"order_date\":\"{r[2]}\",\"shipped_date\":\"{r[3]}\", \"shipping_fee\":\"{r[4]}\",\"Quantity\":\"{r[5]}\",\"unit_price\":\"{r[6]}\",\"product_name\":\"{r[7]}\"" + "}")
      alldata = alldata + ( "{" + f" \"first_name\":\"{r[0]}\",\"id\":\"{r[1]}\",\"order_date\":\"{r[2]}\",\"shipped_date\":\"{r[3]}\", \"shipping_fee\":\"{r[4]}\",\"Quantity\":\"{r[5]}\",\"unit_price\":\"{r[6]}\",\"product_name\":\"{r[7]}\"" + "}" )   
      
    else:
      alldata = alldata + ("{" + f"  \"first_name\":\"{r[0]}\",\"id\":\"{r[1]}\",\"order_date\":\"{r[2]}\",\"shipped_date\":\"{r[3]}\", \"shipping_fee\":\"{r[4]}\",\"Quantity\":\"{r[5]}\",\"unit_price\":\"{r[6]}\",\"product_name\":\"{r[7]}\"" + "},")
          
          
#jsonFile.close()
conn.commit()
cur.close()
conn.close()
connpg.commit()
connpg.close()
          