import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE student(id int(11), name VARCHAR(255), email VARCHAR(255), mobil bigint(20))")
