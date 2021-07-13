from sys import argv
# from os import system
from os.path import exists
from PIL import Image
import numpy as np


path = argv[1]
if not exists(path):
    raise Exception(r"错误：图片 {path} 不存在")
width, height = int(argv[2]), int(argv[3])
width *= 2  # 半角字符是长方形，乘2显示

symbols = np.array(list(" .-+*DXM"))

img = Image.open(path).convert("L").resize((width, height))
img = np.array(img)
img = (img - img.min()) / (img.max() - img.min()) * (symbols.size - 1)
ascii = symbols[img.astype(int)]
lines = "\n".join(("".join(r) for r in ascii))

# system("cls")
print(lines, end="")