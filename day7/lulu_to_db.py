import csv
import sqlite3
import codecs

con = sqlite3.connect("lulu.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Songs;")
cur.execute("CREATE TABLE Songs (Name, Artist, Duration);") # use your column names here

with codecs.open('lulu_mix_16.csv','rb', encoding = 'utf-8', errors ='ignore') as file:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(file) # comma is default delimiter
    to_db = [(i['Name'], i['Artist'], i['Duration']) for i in dr]

cur.executemany("INSERT INTO Songs (Name, Artist, Duration) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()