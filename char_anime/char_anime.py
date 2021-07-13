from os import system, listdir, mkdir
from os.path import exists
from shutil import rmtree
from sys import argv, exit
from time import sleep, time
from PIL import Image
import numpy as np
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication


symbols = np.array(list(' .-+*DXM'))


def prepare(path: str):
    if exists('out'):
        rmtree('out')
    mkdir('out')
    mkdir('tmp')
    system(f'ffmpeg -i {path} -r 25 -qscale:v 2 tmp/%d.jpg')
    system(f'ffmpeg -i {path} -vn out/audio.mp3')


def calculate(width: int, height: int):
    size = len(listdir('tmp'))
    paths = [f'tmp/{i+1}.jpg' for i in range(size)]
    print('字符动画生成 0.00%\r', end='')
    for i in range(size):
        img = Image.open(paths[i]).convert('L').resize((width, height))
        img = np.array(img)
        img = (img - img.min()) / (img.max() - img.min()) * (symbols.size - 1)
        ascii = symbols[img.astype(int)]
        lines = '\n'.join((''.join(r) for r in ascii))
        file = open(f'out/{i+1}.txt', 'w')
        file.write(lines)
        file.close()
        print('字符动画生成 {0:.2f}%\r'.format((i + 1) / size * 100), end='')
    print('字符动画生成 100.00%')
    rmtree('tmp')


def play(width: int, height: int):
    system(f'mode con cols={width} lines={height}')
    file = QUrl.fromLocalFile('out/audio.mp3')
    content = QMediaContent(file)
    player = QMediaPlayer()
    player.setMedia(content)
    player.setVolume(50)
    player.play()
    size = len(listdir('out')) - 1  # 有一个是音频文件
    start = time()
    for i in range(size):
        file = open(f'out/{i+1}.txt', 'r')
        print(file.read(), end='')
        file.close()
        sleep(0.04 - time() + start)
        start = time()


if __name__ == '__main__':
    app = QApplication(argv)
    path, width, height = argv[1], int(argv[2]) * 2, int(argv[3])
    if height > 45:
        raise Exception('错误：高度不可以大于45')
    prepare(path)
    calculate(width, height)
    play(width, height)
    while True: sleep(1)  # 按CTRL+C退出
