'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:01:10
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 09:01:15
FilePath: \060坎公骑冠剑会战工具\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pathlib import Path
import json

import requests

BASE_PATH: str = Path(__file__).absolute().parents[0]

header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
    "connection": "keep-alive",
    "cookie": "_csrf=mekWvfzPK-IVf-YiEAIc4eoP; b_lsid=AFE986CA_1871E29BF5C; buvid_fp=c52ea463c062bcf6b9494bb79ae4d1d9; buvid3=754387E2-CFA4-B1B1-903D-97B31B7EB30167159infoc; b_nut=1679838265; DedeUserID=178547325; DedeUserID__ckMd5=d90ee02c8bad0cdd; SESSDATA=8d68c5bd,1695390391,a47c4*31; bili_jct=d8e98203be854f3dcf0051d5077e378f; sid=feyups5p; buvid4=2E1ACAF3-F64A-4929-2DB6-0323FD8541FD97785-023032621-XHQUoS1U8prhT/1NEcFtEg==; session-api=ql9mo5oeroaimir6p10c0hc7f4; user-info=5287646",
}

URL_1 = f"""https://www.bigfun.cn/api/feweb?target=kan-gong-guild-report%2Fa&date="""
URL_2 = f"""https://www.bigfun.cn/api/feweb?target=kan-gong-guild-log-filter%2Fa"""

r1 = requests.get(
    URL_1, headers=header, verify=False)
print(r1.text)

r2 = requests.get(
    URL_2, headers=header, verify=False)
print(r2.text)
