# coding:utf8
# !/bin/python
# 时间格式相互转换封装工具

import time
import datetime
import calendar


# 将当前时间戳转换为时间字符串，默认为2018-06-01 13:37:04格式
def ctimeToDatetime(format="%Y-%m-%d %H:%M:%S"):
    timestamp = int(time.time())
    timearray = time.localtime(timestamp)
    strtime = time.strftime(format, timearray)
    return strtime


# 将时间戳转换为时间字符串，默认为2018-06-01 13:37:04格式
def timestampToDatetime(timestamp, format="%Y-%m-%d %H:%M:%S"):
    timearray = time.localtime(timestamp)
    strtime = time.strftime(format, timearray)
    return strtime


# 将时间字符串转换为时间戳，时间字符串默认为2018-06-01 13:37:04格式
def datetimeToTimestamp(strtime, format="%Y-%m-%d %H:%M:%S"):
    timearray = time.strptime(strtime, format)
    timestamp = int(time.mktime(timearray))
    return timestamp


# 字符串时间不同格式的转换，默认为2018-06-01 13:37:04格式到2018/06/01 13:37:04格式
def datetimeTransfomFormat(strtime, oformat="%Y-%m-%d %H:%M:%S", nformat="%Y/%m/%d %H:%M:%S"):
    timearray = time.strptime(strtime, oformat)
    strtime = time.strftime(nformat, timearray)
    return strtime


# 获取某年某月第一天开始时间戳,默认当前时间
def getMonthStart(year=None, month=None):
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    mstime = ctime.replace(year=year, month=month, day=1, hour=0, minute=0, second=0, microsecond=0)
    timestamp = int(time.mktime(mstime.timetuple()))
    return timestamp


# 获取某年某月最后一天结束时间戳,默认当前时间
def getMonthEnd(year=None, month=None):
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    mstime = ctime.replace(year=year, month=month, day=monthRange, hour=23, minute=59, second=59, microsecond=0)
    timestamp = int(time.mktime(mstime.timetuple()))
    return timestamp


# 获取某年某月下个月的第一天开始时间戳,默认当前时间
def getNextMonthStart(year=None, month=None):
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    if month == 12:
        year = year + 1
        month = 1
    else:
        month = month + 1
    mstime = ctime.replace(year=year, month=month, day=1, hour=0, minute=0, second=0, microsecond=0)
    timestamp = int(time.mktime(mstime.timetuple()))
    return timestamp


# 获取某年某月下个月的最后一天结束时间戳,默认当前时间
def getNextMonthEnd(year=None, month=None):
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    if month == 12:
        year = year + 1
        month = 1
    else:
        month = month + 1
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    mstime = ctime.replace(year=year, month=month, day=monthRange, hour=23, minute=59, second=59, microsecond=0)
    timestamp = int(time.mktime(mstime.timetuple()))
    return timestamp


# 获取某年某月的第一个星期几时间戳,默认当前时间,星期一
def getFirstWeek(year=None, month=None, wday=1):
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month

    day = datetime.date(year, month, 1)
    weekday = day.isoweekday()
    if weekday == wday:
        dis = 0
    else:
        dis = 7 - weekday + wday

    _time = "%d-%d-%d 00:00:00" % (year, month, 1 + dis)
    timeStr = time.strptime(_time, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeStr))
    return timeStamp


if __name__ == '__main__':
    print int(time.time())
