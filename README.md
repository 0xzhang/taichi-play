# taichi-play

使用太极图形做一些好玩的东西:stuck_out_tongue_winking_eye:

## 效果展示

### [Game of Life](game_of_life/)

![gol](game_of_life/gol.gif)

## 整体结构

```
├── LICENSE
├── README.md
├── game_of_life
│   ├── README.md
│   ├── beacon.gif
│   ├── blinker.gif
│   ├── game_of_life.py
│   ├── glider.gif
│   └── gol.gif
└── requirements.txt
```

## 运行环境

```
[Taichi] version 0.7.32, llvm 10.0.0, commit 6652f94f, linux, python 3.8.8
```

## 生成GIF

在图片目录下

```shell
ti video -f 50
ti gif -i video.mp4
```

