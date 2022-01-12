'''
时间处理相关的类
'''
import time
import datetime


def date_to_timestamp(date, time_format="%Y-%m-%d %H:%M:%S"):
    """
    @summary:
    ---------
    @param date:将"2011-09-28 10:00:00"时间格式转化为时间戳
    @param format:时间格式
    ---------
    @result: 返回时间戳
    """

    timestamp = time.mktime(time.strptime(date, time_format))
    return int(timestamp)


def timestamp_to_date(timestamp, time_format="%Y-%m-%d %H:%M:%S"):
    """
    @summary:
    ---------
    @param timestamp: 将时间戳转化为日期
    @param format: 日期格式
    ---------
    @result: 返回日期
    """
    if timestamp is None:
        raise ValueError("timestamp is null")

    date = time.localtime(timestamp)
    return time.strftime(time_format, date)


# 10位
def get_current_timestamp():
    return int(time.time())


# 13位
def get_current_13_timestamp():
    return int(round(time.time() * 1000))


# datetime_to_string
def datetime_to_string(inputDatetime):
    date_format = "%Y-%m-%d %H:%M:%S"
    return inputDatetime.strftime(date_format)


def get_current_date(date_format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(date_format)
    # return time.strftime(date_format, time.localtime(time.time()))


# 时间戳转换工具
def timesamp2time(timestamp=1462451334):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


# 字符串格式的时间 转为时间戳 返回int 型
def timestr2timestamp(dt=timesamp2time()):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp


# 判断是否在n天内  inputTime 是标准的时间格式 %Y-%m-%d %H:%M:%S
def less_than_n_day(inputTime, n):
    now = int(time.time())
    if isinstance(inputTime, str):
        last = timestr2timestamp(inputTime)
    if isinstance(inputTime, int):
        last = inputTime
    delta = now - last
    result = True if delta <= n * 86400 else False  # 一天是60*60*24=86400秒
    return result


# 获取当前小时
def get_current_hour_date():
    return get_current_date(date_format="%Y-%m-%d %H:00:00")


# 获取今天
def get_today_date():
    return get_current_date(date_format="%Y-%m-%d 00:00:00")


# 转换utc时间 加8小时 转为字符串
def utctime2localtime(utctime):
    try:
        # 处理第一种时间格式  2021-08-23T05:56:15Z
        utc_date = datetime.datetime.strptime(utctime, "%Y-%m-%dT%H:%M:%SZ")
        local_date = utc_date + datetime.timedelta(hours=8)
        local_date_str = datetime.datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')
    except:  # 处理另一种时间格式  2021-08-23T06:56:21.075Z
        utc_date = datetime.datetime.strptime(utctime, "%Y-%m-%dT%H:%M:%S.%fZ")
        local_date = utc_date + datetime.timedelta(hours=8)
        local_date_str = datetime.datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')
    # print(local_date_str)  # 2019-07-26 16:20:54
    return local_date_str


# 将本地时间转为utc时间
def localdatetime2utctime(localdatetime):
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    if isinstance(localdatetime, datetime.datetime):
        nbefore8 = localdatetime + datetime.timedelta(hours=-8)  # 本地时间 减去8小时后为当前的utc时间
    elif isinstance(localdatetime, str):
        localdatetime = datetime.datetime.strptime(localdatetime, '%Y-%m-%d %H:%M:%S')
        nbefore8 = localdatetime + datetime.timedelta(hours=-8)
    UTC_TIME = nbefore8.strftime(UTC_FORMAT)
    return UTC_TIME


if __name__ == '__main__':
    print(get_current_timestamp(), " ,", get_current_date())
    res = less_than_n_day(1626664753, 60)
    print(res)
    res = less_than_n_day("2021-06-19 11:19:18", 90)
    print(res)
    utcTime = "2021-11-09T02:30:03Z"
    print(utctime2localtime(utcTime))
    now_date = get_current_date()
    utc2 = localdatetime2utctime(now_date)
    print(utc2)
    print(get_current_hour_date())
    print(get_today_date())
