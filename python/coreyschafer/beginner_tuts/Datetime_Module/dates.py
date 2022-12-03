import os
import datetime
import pytz

os.chdir('/var/www/html/fullstack_tuts/python/coreyschafer/beginner_tuts/Datetime_Module')

# # print(os.getcwd())

# #### Naive Datetimes

# # # d = datetime.date(2016, 7, 24)
# # # print(d)

# # tday = datetime.date.today()
# # print(tday)
# # print(tday.year)
# # print(tday.day)
# # print(tday.weekday())
# # print(tday.isoweekday())

# # # # #  Weekday
# # # # Monday 0 Sunday 6

# # # # # Isoweekday
# # # # Monday 1 Sunday 7


# ## Timedeltas

# # tday = datetime.date.today()

# # tdelta = datetime.timedelta(days=7)

# # # print(tday - tdelta)

# # # date2 = date1 + timedelta
# # # timedelta = date1 + date2

# # bday = datetime.date(2023, 7, 25)

# # till_bday = bday - tday
# # print(till_bday)
# # print(till_bday.days)
# # print(till_bday.total_seconds())


# ## datetime.time

# # t = datetime.time(9, 30, 45, 100000)
# # print(t)
# # print(t.hour)


# dt = datetime.datetime(2022, 7, 26, 12, 30, 45, 100000)

# # tdelta = datetime.timedelta(days=7)
# tdelta = datetime.timedelta(hours=12)

# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)

# print()

# print(dt + tdelta)


# ## Alternative constructions in datetime

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2022, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_now = datetime.datetime.now(tz=pytz.UTC) # preferred method
# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)


# ## Converting to local Timezone
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Manila'))
# print(dt_mtn)

# print()

# ## Printing all time zone
# for tz in pytz.all_timezones:
#     print(tz)

# ## If we have a naive datime and  want it to become aware
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_mtn = datetime.datetime.now()
# mnl_tz = pytz.timezone('Asia/Manila')

# dt_mnl = mnl_tz.localize(dt_mtn)
# print(dt_mtn)


## ISO Format
dt_mnl = datetime.datetime.now(tz=pytz.timezone('Asia/Manila'))
# print(dt_mnl.isoformat())
print(dt_mnl.strftime('%B %d, %Y'))

## Converting from string
dt_str = 'December 04, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

## strftime - Datetime to String
## strptime - String to Datetime