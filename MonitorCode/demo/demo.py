import requests

r = requests.get(
    'http://jqdev.zeeroh5.com:8888/user/api/v1/app/baseuser/getTokenByUserId?userId=fa10a91b-4356-46ab-8eaa-95c79011cd00')

# =====Request=====
# post/json:r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# get/params:payload = {'key1': 'value1', 'key2': 'value2'};r = requests.get('http://httpbin.org/get', params=payload)
#
# =====Response=====
# 获取Request Url : r.url eg:http://jqdev.zeeroh5.com:8888/user/api/v1/app/baseuser/getTokenByUserId?userId=fa10a91b-4356-46ab-8eaa-95c79011cd00
# 获取Response Content : r.text eg:{"status":"0000_0","messages":["执行成功"],"result":"a0d8cb76-1ea3-37bc-b278-42113c23bc65"}
# 获取Request/Response编码 : r.encoding eg:UTF-8
# 设置Request/Response编码 : r.encoding eg:r.encoding = gbk，修改encoding后，再次通过r.text获取到的即为修改过编码的内容
# 获取Response字节 : r.content eg:b'{"status":"0000_0","messages":["\xe6\x89\xa7\xe8\xa1\x8c\xe6\x88\x90\xe5\x8a\x9f"],"result":"bf270fef-f24c-3f8f-84d4-b864be05506f"}'
# 将Response转换为JSON格式 : r.json() eg:j = r.json() print(j['status'])
# 获取Response 状态码 : r.status_code eg:200
# 获取原始socket response(应该是获取流) : r.raw eg:r = requests.get('https://api.github.com/events', stream=True) <urllib3.response.HTTPResponse object at 0x0000000003515668>
# 将Response分块 : r.iter_content eg:for chunk in r.iter_content(chunk_size=10) print(chunk) 每10个字节切一块，多用于文件流下载或log日志
#
for chunk in r.iter_content(chunk_size=10):
    print(chunk)
