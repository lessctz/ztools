# coding:utf8
# !/bin/python
"""
时间格式相互转换封装工具
"""

import time
import datetime
import calendar


def ctimeToDatetime(format="%Y-%m-%d %H:%M:%S"):
    """
    将当前时间戳转换为时间字符串，默认为2018-06-01 13:37:04格式
    :param format: 字符串的格式
    :return: 时间字符串
    """
    timestamp = int(time.time())
    timearray = time.localtime(timestamp)
    strtime = time.strftime(format, timearray)
    return strtime


def timestampToDatetime(timestamp, format="%Y-%m-%d %H:%M:%S"):
    """
    将时间戳转换为时间字符串，默认为2018-06-01 13:37:04格式
    :param timestamp: 时间戳
    :param format: 字符串的格式
    :return: 时间字符串
    """
    timearray = time.localtime(timestamp)
    strtime = time.strftime(format, timearray)
    return strtime


def datetimeToTimestamp(strtime, format="%Y-%m-%d %H:%M:%S"):
    """
    将时间字符串转换为时间戳，时间字符串默认为2018-06-01 13:37:04格式
    :param strtime: 时间字符串
    :param format: 字符串的格式
    :return: 时间戳
    """
    timearray = time.strptime(strtime, format)
    timestamp = int(time.mktime(timearray))
    return timestamp


def datetimeTransfomFormat(strtime, oformat="%Y-%m-%d %H:%M:%S", nformat="%Y/%m/%d %H:%M:%S"):
    """
    字符串时间不同格式的转换，默认为2018-06-01 13:37:04格式到2018/06/01 13:37:04格式
    :param strtime:字符串时间
    :param oformat:转换前格式
    :param nformat:转换后格式
    :return:转换后字符串时间
    """
    timearray = time.strptime(strtime, oformat)
    strtime = time.strftime(nformat, timearray)
    return strtime


def getMonthStart(year=None, month=None):
    """
    获取某年某月第一天开始时间戳,默认当前时间
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
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


def getMonthEnd(year=None, month=None):
    """
    获取某年某月最后一天结束时间戳,默认当前时间
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
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


def getMonthEnd2(year=None, month=None):
    """
    获取某年某月的结束时间戳
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    next_month = datetime.datetime.now().replace(year=year, month=month, day=28, hour=23, minute=59, second=59, microsecond=0) + datetime.timedelta(4)
    return next_month - datetime.timedelta(days=next_month.day)


def getFirstWeek(year=None, month=None, wday=1):
    """
    获取某年某月的第一个星期几时间戳,默认当前时间,星期一
    :param year: 年
    :param month: 月
    :param wday: 星期
    :return: 时间戳
    """
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

    timestr = "%d-%d-%d 00:00:00" % (year, month, 1 + dis)
    timetuple = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(timetuple))
    return timestamp


def getNextMonthStart(year=None, month=None):
    """
    获取某年某月下个月的第一天开始时间戳,默认当前时间
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
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


def getNextMonthEnd(year=None, month=None):
    """
    获取某年某月下个月的最后一天结束时间戳,默认当前时间
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
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


def getPreMonthStart(year=None, month=None):
    """
    获取某年某月的上月开始时间戳
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    pstime = (ctime.replace(year=year, month=month, day=1, hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(1)).replace(day=1)
    timestamp = int(time.mktime(pstime.timetuple()))
    return timestamp


def getPreMonthEnd(year=None, month=None):
    """
    获取某年某月的上月结束时间戳
    :param year: 年
    :param month: 月
    :return: 时间戳
    """
    ctime = datetime.datetime.now()
    if year:
        year = int(year)
    else:
        year = ctime.year
    if month:
        month = int(month)
    else:
        month = ctime.month
    petime = ctime.replace(year=year, month=month, day=1, hour=23, minute=59, second=59, microsecond=0) - datetime.timedelta(1)
    print petime
    timestamp = int(time.mktime(petime.timetuple()))
    return timestamp


if __name__ == '__main__':
    print int(time.time())
