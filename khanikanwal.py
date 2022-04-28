#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Khani.so'):
    os.system('curl -L https://raw.githubusercontent.com/KANWAL-KhHANI/Khanikanwal/main/Khani.cpython-310.so > Khani.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://raw.githubusercontent.com/KANWAL-KhHANI/Khanikanwal/main/kanwal.cpython-310.so > kanwal.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/KANWAL-KhHANI/Khanikanwa/main/update.txt').text
if 'khanikanwal' in go:
    if bit == '64bit':
        from Khani import reg
        reg()
    elif bit == '32bit':
        from kanwal import reg
        reg()
else:
    os.system('rm -rf Khani.so kanwal.so')
    os.system('curl -L https://raw.githubusercontent.com/KANWAL-KhHANI/Khanikanwal/Kanwal.cpython-310.so > Khani.so')
    os.system('curl -L https://raw.githubusercontent.com/KANWAL-KhHANI/Khanikanwal/main/khani.cpython-310.so > Kanwal.so')
    if bit == '64bit':
        from Khani import reg
        reg()
    elif bit == '32bit':
        from kanwal import reg
        reg()
