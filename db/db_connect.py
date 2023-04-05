import pymysql

# Connect to the MySQL server
# use whatever your credentials are for your mySQL database
DB_HOST = 'localhost:3306'
DB_USERNAME = 'root'
DB_PASSWORD = 'root'


conn = pymysql.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD)