import time              
a= time.localtime()
print("Current Date and Time:",time.asctime(a))
print("Current year:",a[0])
print("Month of year:",a[1])
print("Week number:",time.strftime("%U",a))
print("Weekday (0=sunday):",time.strftime("%w",a))
print("Day of year:",time.strftime("%j",a))
print("Day of Month:",a[2])
print("Day of week (0=Monday):",a[6])

year =int(input("Enter your year:"))
if year %4==0:
    print("Leap Year")
else:
    print("Not leap Year")

from datetime import datetime 
date=input("Enter date(DD-MM-YYYY):")
b=datetime.strptime(date,"%d-%m-%Y")
print("Convert to string datetime",b)

from datetime import datetime
print(datetime.now().time())

from datetime import datetime
date ="July 1 14 2:43PM"
d=datetime.strptime(date,"%B %d %y %I:%M%p")
print(d)

from datetime import datetime,timedelta
today=datetime.now()
before=today-timedelta(days=5)
print("Current Date:",today.date())
print("5 Days Before:",before.date())

from datetime import datetime,timedelta
today=datetime.now().date()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterady:",yesterday)
print("Today:",today)
print("Tomorrow:",tomorrow)

from datetime import datetime,timedelta
now =datetime.now()
new=now+timedelta(seconds=5)
print("Current Time:",now.time())
print("After 5 seconds:",new.time())

from datetime import datetime
now =datetime.now()
milliseconds=now.timestamp()*1000
print(milliseconds)

from datetime import datetime
date =datetime(2015,6,16)
print(date.strftime("%U"))

from datetime import date
d1 =date(2000,2,28)
d2 =date(2001,2,28)
difference=d2-d1
print(difference)

from datetime import datetime
d1 =datetime(2026,7,14,10,0,0)
d2 =datetime(2026,7,15,12,30,20)
difference=d2-d1
days=difference.days
seconds=difference.seconds
hours=seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
print("Days:",days)
print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",seconds)

from datetime import datetime
dob=input("Enter Date of Birth(DD-MM-YYYY):")
birth=datetime.strptime(dob,"%d-%m-%Y")
today=datetime.today()
age=today.year-birth.year
if(today.month,today.day)<(birth.month,birth.day):
    age-=1
    print("Age=",age,"Years")



