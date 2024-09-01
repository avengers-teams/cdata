import requests
import time
import json
import pandas as pd

class DataFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://data.stats.gov.cn/easyquery.htm',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.base_url = 'https://data.stats.gov.cn/easyquery.htm'

    def get_timestamp(self):
        return int(time.time() * 1000)

    def get_province_valuecode(self):
        params = {
            'm': 'getOtherWds',
            'dbcode': 'fsnd',
            'rowcode': 'zb',
            'colcode': 'sj',
            'wds': '[]',
            'k1': self.get_timestamp(),
        }
        response = self.session.get(self.base_url, params=params, headers=self.headers,verify=False)
        data = response.json()
        province_code = [item['code'] for item in data['returndata'][0]['nodes']]
        wds = [{"wdcode": "reg", "valuecode": item} for item in province_code]
        return wds

    def fetch_data(self, wds, dfwds):
        params = {
            'm': 'QueryData',
            'dbcode': 'fsnd',
            'rowcode': 'zb',
            'colcode': 'sj',
            'wds': json.dumps(wds),
            'dfwds': json.dumps(dfwds),
            'k1': self.get_timestamp(),
            'h': '1',
        }
        response = self.session.get(self.base_url, params=params, headers=self.headers,verify=False)
        data = response.json()
        return data

    def process_data(self, data):
        index = [item['cname'] for item in data['returndata']['wdnodes'][0]['nodes']]
        columns = [item['cname'] for item in data['returndata']['wdnodes'][2]['nodes']]
        dataset = [item['data']['data'] for item in data['returndata']['datanodes']]
        array = np.array(dataset).reshape(len(index), len(columns))
        province = data['returndata']['wdnodes'][1]['nodes'][0]['cname']
        df = pd.DataFrame(array, columns=columns, index=index)
        return df, province

    def get_index_valuecode(self, zb):
        params = {
            'id': zb,
            'dbcode': 'fsnd',
            'wdcode': 'zb',
            'm': 'getTree',
        }
        response = self.session.get(self.base_url, params=params, headers=self.headers,verify=False)
        data = response.json()
        new_index = {item['name']: item['id'] for item in data}
        return new_index
    
    def run(self):
        wds = self.get_province_valuecode()
        
            


if __name__ == '__main__':
    data_fetcher = DataFetcher()
    
    
