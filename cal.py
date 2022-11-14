import os
from PIL import Image
import pyocr
import glob

import datetime


def make(file_path):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    img = Image.open(file_path)

    txt = tool.image_to_string(
        img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
    )
    return txt


def main():
    file_paths = glob.glob("templates/*")
    to_dir = "outputs"

    for file_path in file_paths:
        txt = make(file_path)

        # パスからファイル名のみ(拡張子なし)を取得
        filename = os.path.splitext(os.path.basename(file_path))[0]

        # 出力先のパスを生成
        to_path = os.path.join(to_dir, filename + ".txt")

        # 出力先を生成したパスに変更
        with open(to_path, mode="w") as f:
            f.writelines(txt)


def calc():
    file_paths = glob.glob("outputs/*")
    nums = []
    for file_path in file_paths:
        # txt = make(file_path)

        with open(file_path, mode="r") as f:
            data = f.read()
            num = int(data)
            nums.append(num)

    total = sum(nums)
    today = datetime.date.today()
    day = today.strftime("%Y/%m/%d")
    print(f"{day}の摂取カロリーは{total}kcalです。")


# main()

calc()
