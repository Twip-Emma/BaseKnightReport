'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 09:01:10
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-04-04 10:42:33
FilePath: \060坎公骑冠剑会战工具\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from payload import dao
import asyncio



import asyncio
loop = asyncio.get_event_loop()

# 日报
# loop.run_until_complete(dao.get_data())

# 总伤害排行
# loop.run_until_complete(dao.get_data_total())

# 进度
print(loop.run_until_complete(dao.get_rate()))