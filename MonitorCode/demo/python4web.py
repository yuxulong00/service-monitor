import requests
import threading
import json
import time

text = ''


def fun_timer():
    timer = threading.Timer(5, fun_timer)
    timer.start()

    global text

    headers = {'content-type': 'application/json',
               'Cookie': '_T_WM=9605751d64014bc93e7b1c382b691a94; SSOLoginState=1517551892; ALF=1520143892; SCF=AsyYw86-4UbVnlVsL-bQS3rUyBfIWd1vXw37DSPMncmxupO-ERkXbemtbK7wNbVDPKq4Lxr2Y1kgL_-H0GQLUy4.; SUB=_2A253cHFCDeRhGedJ61cQ-CvIzDyIHXVUmx8KrDV6PUNbktAKLUrDkW1NVnsZfkn8Au4EyYQVndImFYFwCknrc8RC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whux8sq1IA-gPZk0TJjsx0A5JpX5KMhUgL.Fo2Neh-p1h-XS052dJLoIpUI9gHEdEH81C-4BbHFSEH81CHF1FHWe7tt; SUHB=0y0YcTdX856_BC; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174; H5_INDEX_TITLE=Zeero%E9%9B%B7%E9%B8%A3; H5_INDEX=0_all'
               }
    r = requests.get(
        'https://m.weibo.cn/feed/friends?version=v4',
        headers=headers)
    try:
        result = r.json()
    except BaseException:
        print('error')
    else:
        mblog = result[0]['card_group'][0]['mblog']
        if text != mblog['text']:
            print(mblog['user']['screen_name'], ':', mblog['text'])
            text = mblog['text']

fun_timer()
