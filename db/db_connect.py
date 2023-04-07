import pymysql

from db.db_credentials import *

conn = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD)
