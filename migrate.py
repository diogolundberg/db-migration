from api import db, sql

connection = db.connection()
cursor = connection.cursor()

print connection.version
cursor.close()

connection.commit()
connection.close()


sql.run_migration_file('teste.sql')
