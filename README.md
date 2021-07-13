# 字符画&字符动画

## 使用指南

使用前请先安装好依赖软件和包。

### 字符画

在控制台中输入：`python char_view.py <图片路径> <width> <height>`

例：`python char_view.py picture.png 45 45`

### 字符动画

在控制台中输入：`python char_anime.py <视频路径> <width> <height>`

例：`python char_anime.py video.mp4 80 45`

### 依赖

- 软件
  - python3、ffmpeg（需添加环境变量）
- 包
  - numpy
  - Pillow
  - PyQt5
  - pyinstaller

*包的安装命令：

```bash
pip install -r requirements.txt
```

### 注意

- 高度不能多于45，不然可能控制台放不下；同理宽度也是，尽量小于90吧。
- 图片/视频路径中不能包含空格

## 参考资料

1. https://www.bilibili.com/video/BV1aT4y1A7EF
2. https://gist.github.com/rossning92/bb1667e5e14a63148dcd61b4455ce52f