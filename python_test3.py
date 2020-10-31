## 日付・時間
import datetime
lvm ='*'*20
##3.1　日付の取得
today = datetime.date.today()
todaydetail = datetime.datetime.today()
print(lvm)
print(today)
print(todaydetail)

print(lvm)
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

print(lvm)
print(today.isoformat())
print(todaydetail.strftime("%Y%m%d %H:%M:%S"))

##3.2 日付の計算
today = datetime.datetime.today()
print(today)
print(today + datetime.timedelta(days=1))
newyear = datetime.datetime(2021,1,1)
print(newyear + datetime.timedelta(days=7))
calc = newyear-today
print(calc.days)

##3.3 閏年の判定
import calendar
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))
print(calendar.leapdays(2010,2020))

