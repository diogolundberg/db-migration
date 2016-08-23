import os
import cx_Oracle
from configparser import ConfigParser
from sys import path
from os.path import join, dirname

config = ConfigParser()

try:
    config.read(join(os.getcwd(), 'config.cfg'))
    database = config['Database']
    host = database.get('HOST', 'localhost')
    port = database.get('PORT', '1521')
    service = database.get('SERVICE', 'XE')
    user = database['USER']
    password = database['PASSWORD']
except KeyError:
    print('Erro ao ler arquivo: ', str(join(os.getcwd(), 'config.cfg')))

def connection():
    dsn = cx_Oracle.makedsn(host, port, service)
    return cx_Oracle.connect(user=user, password=password, dsn=dsn)
