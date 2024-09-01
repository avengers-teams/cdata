import numpy as np
import requests
import time
import json
import pandas as pd

index = {}

def get_timestamp():
    return int(time.time() * 1000)

def make_request(params):
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
    try:
        response = requests.get('https://data.stats.gov.cn/easyquery.htm', params=params, headers=headers, verify=False)
        response.raise_for_status() 
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_province_valuecode():

    params = {
        'm': 'getOtherWds',
        'dbcode': 'fsnd',
        'rowcode': 'zb',
        'colcode': 'sj',
        'wds': '[]',
        'k1': get_timestamp(),
    } # 请求数据
    data = make_request(params=params)
    province_code = [item['code'] for item in data['returndata'][0]['nodes']] 
    wds = [{"wdcode":"reg","valuecode":item} for item in province_code]
    return wds

def fetch_data(wds,dfwds):
    params = {
        'm': 'QueryData',
        'dbcode': 'fsnd',
        'rowcode': 'zb',
        'colcode': 'sj',
        'wds': wds,
        'dfwds': dfwds,
        'k1': get_timestamp(),
        'h': '1',
    }
    data = make_request(params=params)
    return data

def process_data(data):
    index = [item['cname'] for item in data['returndata']['wdnodes'][0]['nodes']] # 指标
    columns=[item['cname'] for item in data['returndata']['wdnodes'][2]['nodes']] # 年份
    dataset = [item['data']['data'] for item in data['returndata']['datanodes']] # 数据
    array=np.array(dataset).reshape(len(index),len(columns))
    province = data['returndata']['wdnodes'][1]['nodes'][0]['cname']
    df = pd.DataFrame(array, columns=columns,index=index)
    return df ,province

def get_index_valuecode(zb):
    while True:
        params = {
            'id': zb,
            'dbcode': 'fsnd',
            'wdcode': 'zb',
            'm': 'getTree',
        }
        data = make_request(params=params)

        new_index = {item['name']: item['id'] for item in data}
        if new_index:
            global index
            index = new_index
            for k, v in new_index.items():
                print(f'{k}: {v}')
            id = input('请输入ID：')
            if id in new_index.values():
                get_index_valuecode(id)
                break
        else:
            break
    
    # 根据选择进行数据获取和处理
    for k, v in new_index.items():
        if v == id:
            print('请确认是否查询' + k + '数据')
            if input('是否继续查询？(y/n)') == 'y':
                wds = get_province_valuecode()
                for wd in wds:
                    data = fetch_data(json.dumps([wd]), json.dumps([{"wdcode":"zb","valuecode":v},{"wdcode":"sj","valuecode":"LAST10"}])) #调整年份LAST5 LAST10 LAST20
                    df, province = process_data(data)
                    print(df.head(10))
                    df.to_excel(f'{province}-{k}.xlsx')



get_index_valuecode('zb') 