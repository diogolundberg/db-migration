import db

connection = db.connection()
cursor = connection.cursor()

print connection.version
cursor.close()

connection.commit()
connection.close()
