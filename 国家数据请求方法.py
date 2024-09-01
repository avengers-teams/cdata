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
    'm': 'QueryData',
    'dbcode': 'hgnd', # 月度数据 hgyd 季度数据 hgjd 年度数据 hgnd 分省年度fsnd 
    'rowcode': 'zb',
    'colcode': 'sj',
    'wds': '[{"wdcode":"reg","valuecode":"340000"}]',
    'dfwds': '[{"wdcode":"zb","valuecode":"A0S0B"},{"wdcode":"sj","valuecode":"LAST5"}]',
    'k1': get_timestamp(),
    'h': '1',
} # 请求数据


'''params = {
    'id': 'zb', # 如果请求根目录就是zb 请求子目录就是从根目录中返回的id值
    'dbcode': 'fsnd', # 月度数据 hgyd 季度数据 hgjd 年度数据 hgnd 分省年度fsnd 
    'wdcode': 'zb',
    'm': 'getTree',
} # 请求目录'''

response = requests.get('https://data.stats.gov.cn/easyquery.htm', params=params, headers=headers, verify=False)
json.loads(response.text)
print(response.text)