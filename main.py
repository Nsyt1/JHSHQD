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
    'X-XSRF-TOKEN': 'eyJpdiI6Inp6b3dNeFpPZmlLNjdSa2hxZ3krUnc9PSIsInZhbHVlIjoiU3Z6RGpPanVWMkg3N0pUSnhtVWdIUWNCZEVZSVwvem1aTGJ6SE1BYUZVanA0d0l3K1wvYzU3V2IyY3B2VkU5cWtMIiwibWFjIjoiYTExYmI1OWY2ZWQ0Yjc1Yzg1NjdiOWI2NGZhMjI2YTEyNmE4M2Y1MGY4M2ZlYzY2MzVmM2Q0MDY0ZTcwYmZkNiJ9',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jxjkhd.kerlala.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/jmXXMKmd/index?cityid=330100&userCityId=110000&u=578749ef-e658-4fba-a40f-e49df50c6050',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-CSRF-TOKEN':'',
    #下方自己数据
    'Cookie': 'XSRF-TOKEN=eyJpdiI6Inp6b3dNeFpPZmlLNjdSa2hxZ3krUnc9PSIsInZhbHVlIjoiU3Z6RGpPanVWMkg3N0pUSnhtVWdIUWNCZEVZSVwvem1aTGJ6SE1BYUZVanA0d0l3K1wvYzU3V2IyY3B2VkU5cWtMIiwibWFjIjoiYTExYmI1OWY2ZWQ0Yjc1Yzg1NjdiOWI2NGZhMjI2YTEyNmE4M2Y1MGY4M2ZlYzY2MzVmM2Q0MDY0ZTcwYmZkNiJ9; _session=eyJpdiI6Im9idE9BRXRST1BhVzdFSFdDWU5tWVE9PSIsInZhbHVlIjoiYThZQUo3d29HcEVNRnBBU2RQZG03Y1hQNnZEblg2ejBGVitRVjUxK3o2SjA5eDAzMk9IWVo1VHBSM3V2bHNaNCIsIm1hYyI6IjlkZmEyZDEzNmQwYjgzYTE2ODdkMmI3OGY4Nzc2ZjJjN2RlYmE3MWFiNjE2NDIwODczNWQzZmExNWVlOWFhZDEifQ%3D%3D; acw_tc=3b258ea316172905528691043ea329c3183657410e34c1bc091cb2bf6c; uid=CgIAEWAyjncuYByKAxEeAg=='
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
    print('建行生活 签到成功')
else:
    url1 = "https://sc.ftqq.com/SCT4665TFVeeQeY1LPtYlJ8scrnwHroz.send?text=token失效/领券成功！"
    requests.get(url1, headers=headers1)

#{'status': 'success', 'code': 10002, 'message': '签到成功', 'data': ''}
