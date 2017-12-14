#!c:\ProgramData\Anaconda3\python.exe

from datetime import datetime,timedelta
import re
import sys

class DateTimeValueError(Exception):
    pass

def date_generator(init_date,dt=1):
    deltatime = dt
    re_obj =re.search('(\d{1,2})[-/](\d{1,2})[-/](\d+)', init_date)
    if re_obj is not None:
        (day,month,year) = re_obj.groups()
    else:
        raise DateTimeValueError('Date Format Error')
    datestring = day + '/'  + month  + '/' + year
    while (True):
        dateobj = datetime.strptime( datestring ,'%d/%m/%Y') + timedelta(days = deltatime)
        yield dateobj
        deltatime +=dt

dg= date_generator('01-01-2010')
print (next(dg))
print (next(dg))
    

