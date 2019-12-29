import os
import pymysql
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_conn():
    '''連接到資料庫，如果不存在，則報錯'''
    #if os.path.exists(path) and os.path.isfile(path):
    try:
        conn = pymysql.connect(
            host = '1270.0.0.1',
            port = 3307,
            user = 'adgjmptw',
            password = '!Qaz2wsx3edc',
            database = 'AI',
        )
        #print('成功連接到數據庫')
        return conn
    #else:
    except:
        print('連接失敗')

def insert_ID_db(IDs):
    '''將指定ID放入資料庫'''
    
    conn = get_conn()
    cursor = conn.cursor()

    try:
        for ID in IDs:
            cursor.execute("SELECT COUNT(1) FROM face WHERE ID = {}".format(ID))
            if cursor.fetchone()[0]: continue
            cursor.execute("INSERT INTO face (ID) values ({})".format(ID))
        conn.commit()
        conn.close()
        #INSERT INTO `project`.`face` (`ID`) VALUES ('d');
    except :
        print ("寫入資料庫失敗")
        print(sys.exc_info())
        conn.close()

def get_NameByID(ID):

    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT Name From test WHERE ID = {ID}")
        name = cursor.fetchone()[0]
        conn.close()
        return name
    except:
        print ("寫入資料庫失敗")
        print(sys.exc_info())
        conn.close()