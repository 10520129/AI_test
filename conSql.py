import os
import sqlite3
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_conn():
    '''連接到資料庫，如果不存在，則報錯'''
    #if os.path.exists(path) and os.path.isfile(path):
    try:
        conn = sqlite3.connect("bot.db")
        #print('成功連接到數據庫')
        return conn
    #else:
    except:
        print('連接失敗')

def get_All():

    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * From test")
        data = cursor.fetchall()
        print(data)
        conn.close()
        return data
    except:
        print ("寫入資料庫失敗")
        print(sys.exc_info())
        conn.close()

def insert_NameByID(Name, ID):
    
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO test (ID, Name) VALUES (?, ?)", [ID, Name])
        conn.commit()
        conn.close()
    except:
        print ("寫入資料庫失敗")
        print(sys.exc_info())
        conn.close()

def get_NameByID(ID):

    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT Name From test WHERE ID = ?", [ID])
        data = cursor.fetchone()
        if data == None: return None
        conn.close()
        return data[0]
    except:
        print ("寫入資料庫失敗")
        print(sys.exc_info())
        conn.close()