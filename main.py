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
    'X-XSRF-TOKEN': 'eyJpdiI6Im83NXlOZTkwN09nRDZCdHpWaXMxR1E9PSIsInZhbHVlIjoicmJoRmpCaWhwTmo3SGtqSHlwNDk5NUFoUU5MejFMMTdHNTluSEFWZlpyeHBNdFRLcGVSR2h5eWNVTGUwaStYZWlJeGcyQXBuZlRCK1pRMWVJa0w5UkxMb0Q3N3VFcEtscURJdWZjejV4WUhud0VENTJqb2w4MzBQVXFhVHd6VVAiLCJtYWMiOiI5MDA5MjdiNDk5YmI4YmVmZWRhNGRlMWJlZjA4OTczNmMzZWRhNzc4M2MxOGJmNTg1OGRlODkxYWZkYjQwZjg5In0=',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jxjkhd.kerlala.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/jmXXMKmd/index?cityid=330100&userCityId=110000&u=578749ef-e658-4fba-a40f-e49df50c6050',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-CSRF-TOKEN':'',
    #下方自己数据
    'Cookie': 'XSRF-TOKEN=eyJpdiI6Im83NXlOZTkwN09nRDZCdHpWaXMxR1E9PSIsInZhbHVlIjoicmJoRmpCaWhwTmo3SGtqSHlwNDk5NUFoUU5MejFMMTdHNTluSEFWZlpyeHBNdFRLcGVSR2h5eWNVTGUwaStYZWlJeGcyQXBuZlRCK1pRMWVJa0w5UkxMb0Q3N3VFcEtscURJdWZjejV4WUhud0VENTJqb2w4MzBQVXFhVHd6VVAiLCJtYWMiOiI5MDA5MjdiNDk5YmI4YmVmZWRhNGRlMWJlZjA4OTczNmMzZWRhNzc4M2MxOGJmNTg1OGRlODkxYWZkYjQwZjg5In0%3D; _session=eyJpdiI6IkhZeEpSWTVDQUZ5M05TdU5scUNJWHc9PSIsInZhbHVlIjoiOXFRVC9sUkdxWHlEbmxNeFYydG4rZXY3QmhNc1k0VHlCRHVMTm0wUGdXZVBpcVVodjVkWjE4SHRLOS8wM1h3WHR5MnZNNUhPTVZySVlJdW1OQm9NQzJPSnMxSkVhVlhIbWRHMERWbUh2MmR5MlgzblJndXlGNUFuN1JRNU51MkIiLCJtYWMiOiJiZWY2NjJiYzUxOTQzMTAyNzY2NTg1OGRjYjIyMTFiNmI0OWJiZjA4ZjU5NWExN2IxNjVkYmMwZWM5ZGYxYmMwIn0%3D; acw_tc=3b258ea616202362989295198e89333f17f531ddef3954248aedf67b36; uid=CgIAEWAyjncuYByKAxEeAg=='
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
