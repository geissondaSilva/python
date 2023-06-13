import config
import psycopg2
import os

conf = config.get()

def init():
    with open('./db.sql', 'r') as file:
        sql_script = file.read()
    con = conn()
    cur = con.cursor()
    cur.execute(sql_script)
    cur.close()
    con.commit()
    con.close()

def conn():
    return psycopg2.connect(
    host="localhost",
    database="python",
    user="postgres",
    password="postgres")
