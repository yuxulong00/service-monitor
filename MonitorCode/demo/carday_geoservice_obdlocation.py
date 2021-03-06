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
               'Authorization': 'c63271cc86dcc4ee704df48e6f345197'
               }
    data = {'mapType': 2,
            'orgId': 122
            }
    timeBeforeRequest = time.time()  # 请求前
    r = requests.post(
        'https://www.car-day.cn/api-service/services/vehicle/queryObdLocation',
        data=json.dumps(data),
        headers=headers)
    # 需要配置header参数
    result = r.json()
    timeAfterResponse = time.time()  # 返回后
    timeSpend = int((timeAfterResponse - timeBeforeRequest) * 1000)

    if r.status_code < 400:
        if result['status'] == '0000_0':
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'ObdLocation接口执行成功，使用时间：', timeSpend,
                  'ms')
            successCount = successCount + 1
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'ObdLocation接口执行失败，使用时间：', timeSpend,
                  'ms', r.text)
            errorCount = errorCount + 1
            file_object = open('log.txt', 'a')
            try:
                tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                    time.time())) + ' ObdLocation接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                    timeSpend) + 'ms，' + r.text
                file_object.write(tempstr)
                file_object.write('\n')
            finally:
                file_object.close()
    else:
        print('ObdLocation接口执行失败，http状态：', r.status_code, '，使用时间：', timeSpend, 'ms', r.text)
        errorCount = errorCount + 1
        file_object = open('log.txt', 'a')
        try:
            tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                time.time())) + ' ObdLocation接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                timeSpend) + 'ms，' + r.text
            file_object.write(tempstr)
            file_object.write('\n')
        finally:
            file_object.close()
    print('总执行次数：', successCount + errorCount, '成功次数：', successCount, '失败次数：', errorCount)


timer = threading.Timer(1, fun_timer)
timer.start()
