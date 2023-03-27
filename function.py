'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:05:56
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 09:07:20
FilePath: \060坎公骑冠剑会战工具\function.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import json
from pathlib import Path
import requests
import httpx

BASE_PATH: str = Path(__file__).absolute().parents[0]