# !/bin/python
# -*- coding:utf-8 -*-
import hashlib
import json
import random
import math


# 生成随机码，n为随机码的位数
def randomCode(n):
    seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cl = random.sample(seed, n)
    code = "".join(cl)
    return code


# 根据概率大小随机物品id,ratedict {id:rate}
def randomRate(ratedict):
    res = None
    if ratedict:
        total = sum(ratedict.values())
        rad = random.randint(1, total)
        cur_total = 0
        for k, v in ratedict.items():
            cur_total += v
            if rad <= cur_total:
                res = k
                break
    return res


# 去除字符串中的 空格 制表符 换行符
def stripStr(str):
    nstr = str.replace(" ", "").replace("\t", "").replace("\n", "").strip()
    return nstr


# 加载json配置文件
def loadConfig(configName):
    with open(configName, 'r') as f:
        config = json.loads(f.read())
    return config


# http请求参数校验
def httpVerify(params):
    signSecret = "MyVerifySecret"
    sitems = sorted(params.items(), key=lambda x: x[0])
    svalue = signSecret
    for sitem in sitems:
        if sitem[0] != "sign":
            svalue += "&" + str(sitem[0]) + "=" + str(sitem[1])
    ensign = hashlib.md5(svalue.encode(encoding='UTF-8')).hexdigest()
    if ensign == params.get("sign", ""):
        return True
    return False


# 游戏数据校验
def verifyData(data, sign, keys=[]):
    apiKey = '99e6e12ffb4a0e5f'
    verdata = dict()
    for key in keys:
        verdata[key] = data.get(key)
    verdata = json.dumps(verdata, sort_keys=True)
    mstr = 'gameData=' + verdata.replace(' ', '') + apiKey
    ensign = hashlib.md5(mstr.encode(encoding='UTF-8')).hexdigest()
    if ensign == sign:
        return True
    return False


# 字典根据多项规则排序
def orderDict(ordict, order=None):
    res = None
    # 字典根据key排序
    if order == 'k':
        res = sorted(ordict.iteritems(), key=lambda x: x[0])
    # 字典根据value排序
    if order == 'v':
        res = sorted(ordict.iteritems(), key=lambda x: x[1])
    # 按key排序，然后按value排序
    if order == 'kv':
        res = sorted(ordict.iteritems(), key=lambda x: (x[0], x[1]))
    # 先按value排序，然后按key排序
    if order == 'vk':
        res = sorted(ordict.iteritems(), key=lambda x: (x[1], x[0]))
    # 先按value升序排序，然后按key降序排序
    if order == 'vrk':
        res = sorted(ordict.iteritems(), key=lambda x: (x[1], -ord(x[0])))
    # 先按value降序排序，然后按key升序排序
    if order == 'rvk':
        res = sorted(ordict.iteritems(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
    return res


# 将num数字的第idx个位置的值修改为val的值
def RecordFlag(num, idx, val):
    count = int(num / math.pow(10, (idx-1))) % 10
    num = num + (val-count) * math.pow(10, (idx-1))
    return num



if __name__ == '__main__':
    print randomCode(10)
    mstr = " abc d e f\ng\nhi"
    print mstr
    print stripStr(mstr)
