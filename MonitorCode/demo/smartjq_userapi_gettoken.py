import requests
import threading
import json
import time

successCount = 0
errorCount = 0


def fun_timer():
    timer = threading.Timer(1, fun_timer)
    timer.start()
    global successCount
    global errorCount
    headers = {'content-type': 'application/json',
               'sign': '921A6CD22FD7A59456B980BB1A2AA2D680CC732FD210D8BA3174734B61610E87'
               }
    timeBeforeRequest = time.time()  # 请求前
    r = requests.get(
        'http://211.136.105.113/smartjq-prod/user/api/v1/app/baseuser/getTokenByUserId?userId=fa10a91b-4356-46ab-8eaa-95c79011cd00',
        headers=headers)
    # 需要配置header参数
    result = r.json()
    timeAfterResponse = time.time()  # 返回后
    timeSpend = int((timeAfterResponse - timeBeforeRequest) * 1000)

    if r.status_code < 400:
        if result['status'] == '0000_0':
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'GetToken接口执行成功，使用时间：', timeSpend,
                  'ms')
            successCount = successCount + 1
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'GetToken接口执行失败，使用时间：', timeSpend,
                  'ms', r.text)
            errorCount = errorCount + 1
            file_object = open('log.txt', 'a')
            try:
                tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                    time.time())) + ' GetToken接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                    timeSpend) + 'ms，' + r.text
                file_object.write(tempstr)
                file_object.write('\n')
            finally:
                file_object.close()
    else:
        print('GetToken接口执行失败，http状态：', r.status_code, '，使用时间：', timeSpend, 'ms', r.text)
        errorCount = errorCount + 1
        file_object = open('log.txt', 'a')
        try:
            tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                time.time())) + ' GetToken接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                timeSpend) + 'ms，' + r.text
            file_object.write(tempstr)
            file_object.write('\n')
        finally:
            file_object.close()
    print('总执行次数：', successCount + errorCount, '成功次数：', successCount, '失败次数：', errorCount)


timer = threading.Timer(1, fun_timer)
timer.start()
