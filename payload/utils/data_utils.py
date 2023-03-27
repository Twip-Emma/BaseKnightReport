'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:55:54
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 09:56:47
'''
import json


def load_data(path: str) -> dict:
    return json.load(open(path, 'r', encoding='utf8'))


def save_data(path: str, data: dict) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
        f.close()
