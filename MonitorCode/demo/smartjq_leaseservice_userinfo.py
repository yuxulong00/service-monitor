import requests
import threading

successCount = 0
errorCount = 0


def fun_timer():
    timer = threading.Timer(1, fun_timer)
    timer.start()
    global successCount
    global errorCount
    headers = {'content-type': 'application/json',
               'token': '04f40c4d-9454-32b8-8741-f3fdeb60fbc9',
               'sign': 'B39C27D691ADE243899A600AF012E03903D2995C19C354D5628E32050C2FD5C0'
               }
    r = requests.get(
        'http://jqdev.zeeroh5.com:8888/lease/api/v1/app/user-info',
        headers=headers)
    # 需要配置header参数
    result = r.json()
    if result['status'] == '0000_0':
        print('分时用户接口执行成功，使用时间：', str(r.elapsed.microseconds)[:-3], 'ms')
        successCount = successCount + 1
    else:
        print('分时用户接口执行成功，使用时间：', str(r.elapsed.microseconds)[:-3], 'ms', r.text)
        errorCount = errorCount + 1
    print('总执行次数：', successCount + errorCount, '成功次数：', successCount, '失败次数：', errorCount)


timer = threading.Timer(1, fun_timer)
timer.start()
