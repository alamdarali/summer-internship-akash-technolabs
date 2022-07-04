import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycursor = conn.cursor()

sql = "INSERT INTO student(name, email, mobil) VALUES ('musa', 'musa@gmailcom', 9854623175)"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount,"row inserted")
