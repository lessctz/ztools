# !/bin/python
# -*- coding:utf-8 -*-
import random


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


if __name__ == '__main__':
    print randomCode(10)
    str = " abc d e f\ng\nhi"
    print str
    print stripStr(str)
