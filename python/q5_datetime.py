# Hint:  use Google to find python function

####a) Use Python to compute days between start and stop date.
from datetime import datetime
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_format = "%m-%d-%Y"
d0 = datetime.strptime(date_start, date_format)
d1 = datetime.strptime(date_stop, date_format)
delta = d1 - d0
print delta.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  
date_format = "%m%d%Y"
d0 = datetime.strptime(date_start, date_format)
d1 = datetime.strptime(date_stop, date_format)
delta = d1 - d0
print delta.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_format = "%d-%b-%Y"
d0 = datetime.strptime(date_start, date_format)
d1 = datetime.strptime(date_stop, date_format)
delta = d1 - d0
print delta.days