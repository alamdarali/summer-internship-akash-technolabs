import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycursor = conn.cursor()

sql = "DELETE FROM student WHERE id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row delete")
