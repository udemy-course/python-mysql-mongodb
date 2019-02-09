import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='demo'
)

cursor = connection.cursor()

# table create

sql = "CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))"
cursor.execute(sql)
connection.commit()

# insert data into table

sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
cursor.execute(sql, ('user1', 'password1'))
cursor.execute(sql, ('user2', 'password2'))
cursor.execute(sql, ('user3', 'password3'))
connection.commit()

# select data

sql = "SELECT id, username from users"
cursor.execute(sql)
while True:
    result = cursor.fetchone()  # fetchall()
    if not result:
        break
    print(result)

# update
sql = "update users set password=%s where username=%s"
cursor.execute(sql, ('password1111', 'user1'))
connection.commit()

# delete
sql = 'DELETE from users where id=%s'
cursor.execute(sql, (2,))
connection.commit()

connection.close()
