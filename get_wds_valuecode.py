import requests
import time
import json


def get_timestamp():
    return int(time.time() * 1000)





headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://data.stats.gov.cn/easyquery.htm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'm': 'getOtherWds',
    'dbcode': 'fsnd', # 月度数据 hgyd 季度数据 hgjd 年度数据 hgnd 分省年度fsnd 
    'rowcode': 'zb',
    'colcode': 'sj',
    'wds': '[]',
    'k1': get_timestamp(),
} # 请求数据




response = requests.get('https://data.stats.gov.cn/easyquery.htm', params=params, headers=headers, verify=False)
data=json.loads(response.text)
province_code = [item['code'] for item in data['returndata'][0]['nodes']] # 省份代码
print(province_code)