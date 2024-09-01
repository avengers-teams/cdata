import requests
import json

index = {}

def get_index_valuecode(zb):
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
        'id': zb,
        'dbcode': 'fsnd',
        'wdcode': 'zb',
        'm': 'getTree',
    }

    response = requests.get('https://data.stats.gov.cn/easyquery.htm', params=params, headers=headers, verify=False)
    data = json.loads(response.text)



    new_index = {item['name']: item['id'] for item in data}
    if new_index:
        index.update(new_index)
        # 逐行打印字典
        for k, v in new_index.items():
            print(k, v)
    else:
        for k, v in index.items():
            print(k, v)
            print('请确认是否查询' + k + '数据')
            if input('是否继续查询？(y/n)') == 'y':
                
            id = input('请输入指标名称：')
            get_index_valuecode(id)



get_index_valuecode('zb') 
