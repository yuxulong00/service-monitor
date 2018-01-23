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
               'token': 'f0e1630b-25b5-3d53-81d1-84d0fbf60249',
               'sign': '08C9E1BD2CB31AAEA1D976DECE97ADC95485AC761B5E5833EEF914A7D824B643'
               }
    r = requests.get(
        'http://211.136.105.113/smartjq-prod/bus/api/v1/app/qrcode?userId=001120180111000000579&refresh=false',
        headers=headers)
    # 需要配置header参数
    result = r.json()
    if result['status'] == '0000_0':
        print('二维码接口执行成功，使用时间：', str(r.elapsed.microseconds)[:-3], 'ms')
        successCount = successCount + 1
    else:
        print('二维码接口执行失败，使用时间：', str(r.elapsed.microseconds)[:-3], 'ms', r.text)
        errorCount = errorCount + 1
    print('总执行次数：', successCount + errorCount, '成功次数：', successCount, '失败次数：', errorCount)


timer = threading.Timer(1, fun_timer)
timer.start()
