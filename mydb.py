import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd= 'admin'

	)

cursorObject= database.cursor()

cursorObject.execute("CREATE DATABASE Redproject")

print("all done! ")