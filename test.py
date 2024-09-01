import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://sousuo.www.gov.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'athenaAppKey': 'JdajL8x18Q4EulIMre8UxTOH7iKwiZMBDjF3yH4XF097e05yezTq4fI%2FsAk0sGqnnVbGQHt1BAC4LzFMH%2BxjLADJb6vvyAv5QScAHRyHzd2rfk1xZZ3YXiNVRfUz0SKx5gDXYEyj2e6Xi6DaIjAUoCuxzca4n9rRRqRS1cftvmU%3D',
    'athenaAppName': '%E5%9B%BD%E7%BD%91%E6%90%9C%E7%B4%A2',
}

json_data = {
    'code': '17da70961a7',
    'historySearchWords': [
        '农业',
    ],
    'dataTypeId': '107',
    'orderBy': 'time',
    'searchBy': 'title',
    'appendixType': '',
    'granularity': 'ALL',
    'trackTotalHits': True,
    'beginDateTime': '',
    'endDateTime': '',
    'isSearchForced': 0,
    'filters': [],
    'pageNo': 1,
    'pageSize': 20,
    'customFilter': {
        'operator': 'and',
        'properties': [],
    },
    'searchWord': '农业',
}

response = requests.post('https://sousuoht.www.gov.cn/athena/forward/2B22E8E39E850E17F95A016A74FCB6B673336FA8B6FEC0E2955907EF9AEE06BE', headers=headers, json=json_data)

#print(response.json().get('result').get('data').get('middle').get('list'))
datas = response.json().get('result').get('data').get('middle').get('list')

for data in datas:
    print(data.get('title_no_tag'))
    print(data.get('url'))