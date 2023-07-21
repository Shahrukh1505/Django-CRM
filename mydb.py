import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'comfy@1234'
)

#prepare a cursor object
cursorObject = dataBase.cursor()


#Create a database

cursorObject.execute("CREATE DATABASE appdata")

print("All done!")
