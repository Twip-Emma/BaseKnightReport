'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-03-27 10:45:06
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-03-27 11:29:37
'''
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

from .function import f_get_damage_data
from .utils.image_utils import write_longsh, FontEntity

BASE_PATH: str = Path(__file__).absolute().parents[0]
FONT_PATH = f"{BASE_PATH}\\ttf\\yuanshen.ttf"


# 获取当日出刀表图
async def get_data():
    # 数据整合
    d_data: dict = await f_get_damage_data()
    text = "===今日数据===\n\n\n"
    index = 1
    for item in d_data:
        text += f"""{index}.{item["user_name"]}({item["damage_num"]})\n"""

        d_index = 1
        for d_tiem in item["damage_list"]:
            text += f"""     第{d_index}刀：{d_tiem["boss_name"]}(伤害：{d_tiem["damage"]})\n"""
            d_index += 1
        index += 1
        text += "\n\n"
    
    # 图像处理
    font = FontEntity(fsize=20,ttf_path=FONT_PATH)
    bg = Image.new("RGB",(1000,5000), (255,255,255))
    image = write_longsh(font_entity=font, img=bg, text=text, dis=(50,50))
    image.save(f"{BASE_PATH}\\cache\\text.jpg")
