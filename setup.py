from os import listdir
from os.path import join
from sys import path
from distutils.core import setup
import fnmatch

migrations = [f for f in listdir(join(path[0], 'migrations'))]
migrations = ['migrations/' + f for f in fnmatch.filter(migrations, '*.sql')]

setup(
    name='db-migrate',
    version='1.0',
    description='A generic database migration tool',
    url='https://github.com/diogolundberg/db-migration',
    author='Diogo Lundberg',
    author_email='diogo@lundberg.com.br',
    packages=['api'],
    install_requires=['cx_Oracle'],
    console=['migrate.py'],
    data_files=[('../', ['config.cfg']), ('migrations/', migrations)],
    options={
        "py2exe": {
            "compressed": 0,
            "optimize": 1,
            "xref": False,
            "skip_archive": False,
            "bundle_files": 0,
            "includes": ['decimal', 'uuid'],
            "dist_dir": 'build/scripts',
        }
    }
)

bat = open('build/migrate.bat', 'w')
bat.write('@echo off\n')
bat.write('chcp 1252\n')
bat.write('mode con: cols=160 lines=1000\n')
bat.write('migrate' + '\n')
bat.write('cmd')
bat.close()
