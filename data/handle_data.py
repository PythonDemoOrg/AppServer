# -*- coding: UTF-8 -*-

# Filename : handle_data.py
# author by : WeiQi

import json

def make_up(price):
    prices = {
        'limit': 1000,
        'subscribed': [],
        'others': [{
            'id': price[0],
            'title': str(price[1]),
            "thumbnail": str(price[2]),
            'description': str(price[3]),
            'done': False}]
    }
    return str(prices)

def add_header(others):
    res = {
        'limit': 1000,
        'subscribed': [],
        'others': json.loads(tableToJson(others))
    }
    return str(res)

def tableToJson(table):
    jsonData = []
    for row in table:
        flag = False
        if (row[4]==1):
            flag=True
        result = {}
        result['id'] = row[0]
        result['title'] = str(row[1])
        result['thumbnail'] = str(row[2])
        result['description'] = str(row[3])
        result['done'] = flag
        jsonData.append(result)
    jsondatar = json.dumps(jsonData, ensure_ascii=False)
    return jsondatar
    # 去除首尾的中括号
    # return jsondatar[1:len(jsondatar) - 1]