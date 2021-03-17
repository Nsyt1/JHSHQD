# -*- coding:utf-8 -*-

import requests
import json

url = "https://jxjkhd.kerlala.com/activity/autographnew/register/31/jmXXMKmd"
headers = {
    'Authorization': 'Bearer',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    #下方自己数据
    'X-XSRF-TOKEN': 'eyJpdiI6Imtha0dtMmxMa202Y1N1b1V0eHBQWHc9PSIsInZhbHVlIjoiQ0M5WTFJZmx2Mm5pTnNYTjRHRUI4UHh0aWh2dWE3bE1qcGFOaXNaY3dMaXNhdkJmcHN2b1ZXOE5QdmcwS24waCIsIm1hYyI6IjViOTYyZTljZTkzYWY0ZjQxMGUyMWNhMDk2OTMyOWNlZjFjOGM0OTQ3ODQ3ZDg2MjkxYjg0MjkxYzA2N2E4ZjcifQ==',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jxjkhd.kerlala.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/jmXXMKmd/index?cityid=330100&userCityId=110000&u=578749ef-e658-4fba-a40f-e49df50c6050',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-CSRF-TOKEN':'',
    #下方自己数据
    'Cookie': 'XSRF-TOKEN=eyJpdiI6Imtha0dtMmxMa202Y1N1b1V0eHBQWHc9PSIsInZhbHVlIjoiQ0M5WTFJZmx2Mm5pTnNYTjRHRUI4UHh0aWh2dWE3bE1qcGFOaXNaY3dMaXNhdkJmcHN2b1ZXOE5QdmcwS24waCIsIm1hYyI6IjViOTYyZTljZTkzYWY0ZjQxMGUyMWNhMDk2OTMyOWNlZjFjOGM0OTQ3ODQ3ZDg2MjkxYjg0MjkxYzA2N2E4ZjcifQ%3D%3D; _session=eyJpdiI6IjFOdlwvUXlNR3ExXC9vanFPdzFTSWEzQT09IiwidmFsdWUiOiJZYnFIc3lWZTdkN1FISHJzVG5uellVaWJEZXhUWkZcL1A0bUx3S1IrTXpuSmJXZU5kdjhvZ1g5Q0ZmZjBxQ2lNQSIsIm1hYyI6ImJlNTIxNzQwMDYzYjQ5OTQ4MjMxMGJmNzYyODUxMzJmYmVjYjg1OWRiYjQ4NDUzYjgyNTY1NTBiYTA3NWJlM2MifQ%3D%3D; acw_tc=0e1d289e16155727666644582e6aab7453e9b01d87172c090c1972bf75; uid=CgIAEWAyjncuYByKAxEeAg=='
}
res = requests.post(url,headers=headers)
result = json.loads(res.content)
headers1 = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
if result['code'] == 10002:
    url1 = "https://sc.ftqq.com/SCT4665TFVeeQeY1LPtYlJ8scrnwHroz.send?text="+result['message']
    requests.get(url1,headers=headers1)
elif result['code'] == 20001:
    print('签到成功')
else:
    url1 = "https://sc.ftqq.com/SCT4665TFVeeQeY1LPtYlJ8scrnwHroz.send?text=token失效/领券成功！"
    requests.get(url1, headers=headers1)

#{'status': 'success', 'code': 10002, 'message': '签到成功', 'data': ''}
