from multiprocessing.sharedctypes import Value
from pyperclip import copy, paste

def date(day, interval):
    begin_time, end_time = interval.split('-')
    print('2022-02-' + day + 'T' + begin_time + ':00')
    print('2022-02-' + day + 'T' + end_time + ':00')

def replace(s):
    s = s.replace(' *', '', -1)
    s = s.replace(' **', '', -1)
    s = s.replace('*', '', -1)
    s = s.replace('.', '', -1)
    s = s.replace('/', '', -1)
    s = s.replace('&', 'and', -1)
    s = s.replace('\r\n', ' ', -1)
    s = s.replace('-', '_', -1)
    s = s.replace(' + ', '_', -1)
    s = s.replace('+', '_', -1)
    s = s.replace('  ', ' ', -1)
    s = s.replace(' ', '_', -1)
    return s

def convert():
    s = paste()
    copy(replace(s))
