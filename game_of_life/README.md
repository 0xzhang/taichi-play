# Game of Life

## 背景介绍

John H Conway（1937-2020）于1970年发明生命游戏，一种二维的元胞自动机。这个游戏中有一个向各个方向无限延伸的二维世界，并且被划分为一个个细胞。任意一代中，每个细胞处于活着或死去的状态。游戏包含一套规则，描述了每一代细胞是如何进化的。

在二维世界中，一个细胞在垂直、水平和对角方向共相邻8个细胞。进化规则如下：

1. 1个活细胞相邻少于2个活细胞时，将死去；
2. 1个活细胞相邻多于3个活细胞时，将死去；
3. 1个活细胞相邻恰好2个或3个活细胞时，将存活；
4. 1个死细胞相邻恰好3个活细胞时，将复活。

为了简化对field边界处的处理，采用周期性的方式，对超出边界的field索引取模。

### 功能介绍

在GOL中出现了一些不同类型的模式，通常可以分为三类：

1. 静态（still lifes），在下一代不会发生变化；
2. 振荡器（oscillators），在有限进化次数后形状还原到初始状态；
3. 宇宙飞船（spaceships），能够在网格中移动和变换，经过有限进化次数后形状与初始状态相同，可以看作是一种会移动的振荡器。

目前提供以下4种初始化模式：

1. **init_random**()，以`live_ratio`为存活率随机生成活细胞。
2. **init_blinker**()，一种振荡器，在全局每个5x5的单元中设置活细胞。
3. **init_beacon**()，一种振荡器，在全局每个6x6的单元中设置活细胞。
4. **init_glider**()，一种宇宙飞船，在左上角设置。

## 效果展示

<a href="gol.gif"><img src="imgs/gol.gif" height=192px title="random"></a>
<a href="glider.gif"><img src="imgs/glider.gif" height=192px title="glider"></a>
<a href="blinker.gif"><img src="imgs/blinker.gif" height=192px title="blinker"></a>
<a href="beacon.gif"><img src="imgs/beacon.gif" height=192px title="beacon"></a>

## 运行方式

```shell
python game_of_life.py
```

## 参考资料

1. [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
2. [Lab 1: Game of Life (mit.edu)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/labs/MIT6_087IAP10_lab01.pdf)
3. [Conway's Game of Life: Mathematics and Construction (conwaylife.com)](https://conwaylife.com/book/)
4. [Golly Game of Life Home Page (sourceforge.net)](http://golly.sourceforge.net/)
