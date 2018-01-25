import requests
import threading
import json
import time
import pymysql

# demo
# db = pymysql.connect("121.199.5.149", "root", "Gyg9w3t7xvmg9b2", "service_monitor")
db = pymysql.connect(
    host='121.199.5.149',
    port=3306,
    user='root',
    password='Gyg9w3t7xvmg9b2',
    db='service_monitor',
    charset='utf8'
)
cursor = db.cursor()
cursor.execute("INSERT INTO error(url,code,message) VALUES('http','0000_0','测试错误信息')")
db.commit()
cursor.close()
db.close()
# demo

successCount = 0
errorCount = 0


def fun_timer():
    # timer = threading.Timer(1, fun_timer)
    # timer.start()
    global successCount
    global errorCount
    headers = {'content-type': 'application/json',
               'Authorization': 'fcdadd5c3e140eb6bc9dc935365ec24f'
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
