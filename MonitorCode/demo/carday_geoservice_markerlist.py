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
               'Authorization': 'fcdadd5c3e140eb6bc9dc935365ec24f'
               }
    data = {'currentPage': 1,
            'geofenceName': None,
            'mapType': 2,
            'markerId': None,
            'markerType': "MARKER",
            'numPerPage': 10,
            'provinceId': None
            }
    timeBeforeRequest = time.time()  # 请求前
    r = requests.post(
        'https://www.car-day.cn/api-service/services/marker/list',
        data=json.dumps(data),
        headers=headers)
    result = r.json()
    timeAfterResponse = time.time()  # 返回后
    timeSpend = int((timeAfterResponse - timeBeforeRequest) * 1000)

    if r.status_code < 400:
        if result['status'] == '0000_0':
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'MarkerList接口执行成功，使用时间：', timeSpend,
                  'ms')
            successCount = successCount + 1
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'MarkerList接口执行失败，使用时间：', timeSpend,
                  'ms', r.text)
            errorCount = errorCount + 1
            file_object = open('log.txt', 'a')
            try:
                tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                    time.time())) + ' MarkerList接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                    timeSpend) + 'ms，' + r.text
                file_object.write(tempstr)
                file_object.write('\n')
            finally:
                file_object.close()
    else:
        print('MarkerList接口执行失败，http状态：', r.status_code, '，使用时间：', timeSpend, 'ms', r.text)
        errorCount = errorCount + 1
        file_object = open('log.txt', 'a')
        try:
            tempstr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                time.time())) + ' MarkerList接口执行失败，http状态' + str(r.status_code) + '，使用时间：' + str(
                timeSpend) + 'ms，' + r.text
            file_object.write(tempstr)
            file_object.write('\n')
        finally:
            file_object.close()
    print('总执行次数：', successCount + errorCount, '成功次数：', successCount, '失败次数：', errorCount)


timer = threading.Timer(1, fun_timer)
timer.start()
