#!/usr/bin/env python3

from datetime import datetime
import re

def date_generator(init_date):
    re_obj =re.search('(\d{1,2})[-/](\d{1,2})[-/](\d+)', init_date)
    if re_obj is not None:
        (day,month,year) = re_obj.groups()
        print (day,month,year)
    return

date_generator('01-01-2010')
    
