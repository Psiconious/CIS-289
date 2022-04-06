import sqlite3
from sqlite3 import Error
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
"""
Name: Trever Cluney
Date: 02.27.22
Email: tlcluney@dmacc.edu
Overview: Creating and using database with sqllite3
"""


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


database = "weather_tracking.db"
sql_create_precipation_table = """CREATE TABLE IF NOT EXISTS precipitation(location text, date text, precipitation real, precip_type text, FOREIGN KEY(location) REFERENCES location(county))"""
sql_create_location_table = """CREATE TABLE IF NOT EXISTS location(county text PRIMARY KEY, state text)"""

my_conn = create_connection(database)

if my_conn is not None:
    create_table(my_conn, sql_create_location_table)
    create_table(my_conn, sql_create_precipation_table)

else:
    print("Error cannot create connection to database")

cur = my_conn.cursor()

with open('iowa_counties.csv') as input_file:
    data = csv.DictReader(input_file)
    to_db = [(i['county'], i['state']) for i in data]

    to_db_county = [item[0] for item in to_db]
    for x in range(0, len(to_db)):
        to_db_county[x] = tuple([to_db_county[x], to_db[x][1]])

with open('DSM_weater_dataset.csv', 'r') as input_file:
    data = csv.DictReader(input_file)
    to_db = [(i['date'], i['precipitation'], i['county']) for i in data]

    to_db_weather = [[] for item in to_db]
    for x in range(0, len(to_db)):
        to_db_weather[x] = tuple([to_db[x][0], to_db[x][1], to_db[x][2]])

with open('Waterloo_weather_dataset.csv', 'r') as input_file2:
    data = csv.DictReader(input_file2)
    to_db2 = [(i['date'], i['precipitation'], i['county']) for i in data]

    to_db_weather2 = [[] for item in to_db]
    for x in range(0, len(to_db2)):
        to_db_weather2[x] = tuple([to_db2[x][0], to_db2[x][1], to_db2[x][2]])


cur.executemany("REPLACE INTO location(county,state) VALUES(?,?);", to_db_county)
cur.executemany("REPLACE INTO precipitation(date, precipitation, location ) VALUES(?,?,?);", to_db_weather)
cur.executemany("REPLACE INTO precipitation(date, precipitation, location ) VALUES(?,?,?);", to_db_weather2)

with sqlite3.connect(database) as db:
    precipitation_in_inches = my_conn.execute('SELECT date,precipitation,location FROM precipitation').fetchall()

precipitation_in_millimeters = []
for incremeter in range(0, len(precipitation_in_inches)):
    precipitation_in_millimeters.append(((precipitation_in_inches[incremeter][1] * 25.4), precipitation_in_inches[incremeter][0], precipitation_in_inches[incremeter][2]))


with sqlite3.connect(database) as db:
    #pass
    my_conn.executemany('UPDATE precipitation SET precipitation=? WHERE date=? and location=?', precipitation_in_millimeters)

with sqlite3.connect(database) as db:
    database_dates = my_conn.execute('SELECT date FROM precipitation').fetchall()

updated_database_dates = []
for i in range(0, len(database_dates)):
    old_datetime = datetime.datetime.strptime(database_dates[i][0], '%Y-%m-%d')
    new_datetime = old_datetime - datetime.timedelta(days=1)
    new_datetime = new_datetime.strftime('%Y-%m-%d')
    #print(new_datetime)
    updated_database_dates.append((new_datetime, i+1))

#print(updated_database_dates)

my_conn.executemany('UPDATE precipitation SET date=? WHERE rowid=?', updated_database_dates)

my_conn.execute('DELETE FROM precipitation WHERE location="black hawk"')


my_conn.commit()
my_conn.close()

print(pd.read_sql_query('SELECT * FROM precipitation', sqlite3.connect(database)))
