<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-03-27 09:43:36
 * @LastEditors: 七画一只妖 1157529280@qq.com
 * @LastEditTime: 2023-03-31 10:13:39
 * @FilePath: \060坎公骑冠剑会战工具\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# BaseKnightReport
## 坎公会战工具（更新中）

### 这是什么？
> 1.这是游戏《坎公骑冠剑》游戏中公会战查询数据的工具
> 2.因为找遍github也没找到python版本的会战查询工具于是自己做了个
> 3.该项目输出内容为图片，直接测试可以前往`main.py`查看
> 4.如果您的机器人使用的是python语言的框架，那么可以自行融合进去并根据需要进行修改
> 5.如果您使用的是nonebot2(beta5-rc3)，可以根据下面我写的配置进行使用

### 已完成功能
>- 1.输出每日伤害报表
>- 2.输出总榜
>- 3.查询当前进度

### 使用方法
1.在payload目录下新建文件cookies.py并添加以下内容
~~~py
header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
    "connection": "keep-alive",
    "cookie": "你的cookies",
}
~~~

2.如何获取cookies？
>- 1.浏览器开启无痕模式
>- 2.打开百宝袋地址 https://www.bigfun.cn/tools/gt/
>- 3.使用B站登录
>- 3.在百宝袋页面按下【F12 没有F12右键审元素】打开DEV开发者工具 在【网络】一栏随便找到一个请求，找到Cookie字段并复制值
>- 4.关闭无痕窗口浏览器（不要使用bigfun退出登录 会导致接口失效 也不要切换账号会立刻失效）

3.如果您使用的是nonebot（beta5-rc3版本可用），可以将main.py删除，新增一个__init__.py文件，并在其加上以下内容
然后作为插件运行即可
~~~python
from pathlib import Path

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from .payload.dao import get_data, get_data_total, get_rate

BASE_PATH: str = Path(__file__).absolute().parents[0]


daily = on_command("战报", aliases={"每日战报", "每日", "日报"}, block=True, priority=1)
total = on_command("总榜", aliases={"总排行", "排行", "排行榜"}, block=True, priority=1)
rate = on_command("进度", aliases={"战况", "现在情况", "当前进度"}, block=True, priority=1)

# 日报
@daily.handle()
async def send_daily_report(bot: Bot, event: GroupMessageEvent):
    msg = str(event.get_message()).split()

    if len(msg) not in (1, 2):
        await daily.finish("请求格式错误，举例：\n战报\n战报 2023-03-20")

    try:
        if len(msg) == 1:
            img_path = await get_data()
        else:
            img_path = await get_data(msg[1])
    except Exception as e:
        await daily.finish(f"获取数据失败，错误信息：{e}")

    await daily.send(MessageSegment.image("file:///" + img_path))


@total.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = str(event.get_message()).split()
    if len(msg) != 1:
        await daily.finish("请求格式错误，举例：\n总榜")

    try:
        img_path = await get_data_total()
    except Exception as e:
        await daily.finish(f"获取数据失败，错误信息：{e}")

    await daily.send(MessageSegment.image("file:///" + img_path))


@rate.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = str(event.get_message()).split()
    if len(msg) != 1:
        await daily.finish("请求格式错误，举例：\n进度")

    try:
        img_path = await get_rate()
    except Exception as e:
        await daily.finish(f"获取数据失败，错误信息：{e}")

    await daily.send(MessageSegment.image("file:///" + img_path))
~~~


