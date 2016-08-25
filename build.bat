@echo off
rmdir /s /q "build/"
python setup.py py2exe
cmd
