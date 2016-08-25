import os
import cx_Oracle
from configparser import ConfigParser
from sys import path
from os.path import join, dirname

config = ConfigParser()

try:
    config.read(join(os.getcwd(), 'config.cfg'))
    database = dict(config.items('Database'))
    host = database.get('host', 'localhost')
    port = database.get('port', '1521')
    service = database.get('service', 'XE')
    user = database['user']
    password = database['password']
except KeyError:
    print('Erro ao ler arquivo: ', str(join(os.getcwd(), 'config.cfg')))

def connection():
    dsn = cx_Oracle.makedsn(host, port, service)
    return cx_Oracle.connect(user=user, password=password, dsn=dsn)
