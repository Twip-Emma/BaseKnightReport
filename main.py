'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:01:10
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 17:32:45
FilePath: \060坎公骑冠剑会战工具\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from payload import dao
import asyncio



import asyncio
loop = asyncio.get_event_loop()

# loop.run_until_complete(dao.get_data("2023-03-10"))

loop.run_until_complete(dao.get_data_total())