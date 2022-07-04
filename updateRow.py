import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

mycursor = conn.cursor()

sql = "UPDATE student SET name = 'rahul' WHERE id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row update")
