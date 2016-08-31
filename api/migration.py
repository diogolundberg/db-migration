import os
import re
from os import getcwd
from sys import path
from os.path import join, dirname
from api import db
import subprocess

def get_filenames(dirname):
    files = os.listdir(dirname)
    files = filter(lambda x: x.endswith("sql"), files)
    files = [file.split(".")[0] for file in files]
    return sorted(files)


def run_file(filename, dirname='migrations'):
    cmdline = ['echo', 'exit', 'sqlplus', db.user + '/' + db.password + '@' + db.host, '@', join(getcwd(), 'migrations', filename)]
    process = subprocess.Popen(cmdline, stdout=subprocess.PIPE)
    return process.communicate()

def exists_schema_version():
    connection = db.connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM USER_TABLES WHERE TABLE_NAME = UPPER('SCHEMA_VERSION')")

    exists = bool(cursor.fetchone()[0])

    cursor.close()
    connection.close()
    return exists


def create_schema_version():
    connection = db.connection()
    cursor = connection.cursor()

    if not exists_schema_version():
        cursor.execute('CREATE TABLE SCHEMA_VERSION (VERSION VARCHAR2(12) NOT NULL)')

    cursor.close()
    connection.close()


def get_schema_version():
    connection = db.connection()
    cursor = connection.cursor()

    cursor.execute('SELECT VERSION FROM SCHEMA_VERSION ORDER BY VERSION')
    applied =  [x[0] for x in cursor.fetchall()]

    cursor.close()
    connection.close()

    return applied


def verify_applied_migrations(versions, applied):
    if len(applied) > len(versions):
        print "There are more versions applied then migrations files."
        return False

    for i, version in enumerate(applied):
        if version != versions[i]:
            if version not in versions:
                print "Version (" + version + ") not found in the migration files."
            else:
                print "Schema Version not synchronized with migration files."
            return False

    return True


def insert_version(version):
    connection = db.connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO SCHEMA_VERSION VALUES (:version)', version=version)
    connection.commit()
    cursor.close()
    connection.close()


def apply_migrations(filenames, schema_version):
    migrations = filenames[len(schema_version):]

    for migration in migrations:
        out, err = run_file(migration)
        print out, err
        insert_version(migration.split('__')[0])
        print 'Migration', migration, 'applied.'
