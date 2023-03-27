'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 10:45:06
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 14:27:01
'''
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

from .function import f_get_damage_data
from .utils.image_utils import write_longsh, FontEntity
from .utils.data_utils import data_format

BASE_PATH: str = Path(__file__).absolute().parents[0]
FONT_PATH = f"{BASE_PATH}\\ttf\\yuanshen.ttf"


# 获取当日出刀表图
async def get_data():
    
    d_data: dict = await f_get_damage_data()

    # 数据整合（生成排版文字）
    text = "===今日数据===\n\n\n"
    index = 1
    d_data = data_format(d_data)
    for item in sorted(d_data, key = lambda i: i["damage_total"], reverse=True):
        text += f"""{index}.{item["user_name"]}({item["damage_num"]}) 总伤害：{item["damage_total"]}\n"""
        d_index = 1
        for d_tiem in item["damage_list"]:
            text += f""">>>>>{d_tiem["boss_name"]:>5}   {d_tiem["damage"]}\n"""
            d_index += 1
        index += 1
        text += "\n\n"

    # 图像处理
    fsize=20
    font = FontEntity(fsize=fsize, ttf_path=FONT_PATH)

    # 计算高度
    line, max_text = _get_max_size(text)
    dis = (50, 50)

    _f = ImageFont.truetype(FONT_PATH, 20)
    width, _ = _f.getsize(max_text)

    page_height = int((dis[0] * 2 + fsize * line) * 1.2)
    page_width = dis[1] * 2 + width

    text.split("#")
    bg = Image.new("RGB", (page_width, page_height), (255, 255, 255))
    image = write_longsh(font_entity=font, img=bg, text=text, dis=dis, mode="L")
    save_path = f"{BASE_PATH}\\cache\\daily_damage.jpg"
    image.save(save_path)
    return save_path


# 获取文本行数和最长字符串个数
def _get_max_size(text: str) -> tuple:
    """
    获取文本行数和最长字符串
    text:文本
    返回:(文本行数，最长字符串)
    """
    _text = text.split("\n")
    line = len(_text)

    max_line = 0
    max_text = ""
    for item in _text:
        this_line = len(item)
        if max_line < this_line:
            max_text = item
            max_line = this_line
    return line, max_text
