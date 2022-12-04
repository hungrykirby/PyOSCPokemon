import os
from PIL import Image, ImageDraw
import pyocr
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

RECT_RANGE = {
    'x': 990, # 個体値判定の場合には990でいいはず
    'y': 180, # ここの値を変更する。攻撃なら180
    'w': 100, # 個体値判定の場合には100でいいはず
    'h': 30, # 個体値判定の場合には30でいいはず
}

IMAGE_FILE_NAME = 'input02.jpg'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = os.environ.get("TESSERACT_CMD")
tools = pyocr.get_available_tools()
tool = tools[0]

# 文字を抽出したい画像のパスを選ぶ
img = Image.open('images/' + IMAGE_FILE_NAME)
draw = ImageDraw.Draw(img)

rect_xy = (RECT_RANGE['x'], RECT_RANGE['y'], RECT_RANGE['x'] + RECT_RANGE['w'], RECT_RANGE['y'] + RECT_RANGE['h'])

# 文字列を取得したい部分を切り抜く
img_region = img.crop(rect_xy)

draw.rectangle(rect_xy, fill=(250, 0, 0)) # 抽出した文字部分を塗りつぶす

width, height = img.size

# 文字列を取得したい画像範囲の文字を抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img_region.convert('L'), lang="jpn", builder=builder)

print(text)

img.show()
