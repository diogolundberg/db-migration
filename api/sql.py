import re
from os import getcwd
from sys import path
from os.path import join, dirname
from api import db


def run_migration_file(sql):
    connection = db.connection()
    cursor = connection.cursor()

    file = open(join(getcwd(), 'migrations', sql))
    sql = "".join(file.readlines())
    sqls = re.split(r";$", sql, flags=re.MULTILINE | re.IGNORECASE)
    
    for sql in sqls:
        sql = sql.replace('\n', '')
        if len(sql) > 0:
            cursor.execute(sql)
            print sql

    connection.commit()
    connection.close()
