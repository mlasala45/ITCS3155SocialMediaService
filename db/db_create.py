import pymysql

# Connect to the MySQL server
# use whatever your credentials are for your mySQL database
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='BusterBitch123!')

# Create a new database
db_name = 'my_database'
cursor = conn.cursor()
cursor.execute(f'CREATE DATABASE {db_name}')

# Switch to the new database
cursor.execute(f'USE {db_name}')

# Create a new table called "users"
cursor.execute("""CREATE TABLE users (
                  id INT(11) NOT NULL AUTO_INCREMENT,
                  username VARCHAR(255) UNIQUE,
                  PRIMARY KEY (id)
                )""")

# Insert users into the "users" table
users = ['user1', 'user2', 'user3']
for user in users:
    cursor.execute("""INSERT INTO users (username)
                      VALUES (%s)""",
                   (user,))
                   
# Create a new table called "photos" owned by "user1"
cursor.execute("""CREATE TABLE user1_photos (
                  id INT(11) NOT NULL AUTO_INCREMENT,
                  photo BLOB,
                  caption VARCHAR(255),
                  PRIMARY KEY (id)
                )""")
cursor.execute("""INSERT INTO users_photos (user_id)
                  VALUES ((SELECT id FROM users WHERE username = 'user1'))""")
                  
# Insert data/photos into the "user1_photos" table
with open('photo1.jpg', 'rb') as f:
    photo_data = f.read()

caption = 'A beautiful sunset'
cursor.execute("""INSERT INTO user1_photos (photo, caption)
                  VALUES (%s, %s)""",
               (photo_data, caption))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
