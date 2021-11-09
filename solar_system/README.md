# Solar System

## 背景介绍

宇宙中包含许多像太阳系这样的行星系统，行星围绕着恒星运行，太阳系位于银河系的外旋壁上。

参考知乎文章[用86行Python代码模拟太阳系](https://zhuanlan.zhihu.com/p/102375135)的作者**何崇崇**模拟太阳系使用的计算方法，使用Taichi的OOP和GGUI编写了3D的太阳系模拟。

在作者的代码仓库中`get_initial_condition.py`提供了获取天体数据的方式，但是对JPL实验室API `ssd.jpl.nasa.gov/api/horizons.api`的请求没有响应，目前使用了作者提供的2018-01-01这一天的天体数据。

### 功能介绍

水星、金星、地球、火星比例接近实际，为了能够清楚的看到这些行星，太阳大小并非真实比例。

木星的轨道半径非常大，会影响到地球的观测，暂时未加入更大轨道上的行星。

### TODO

- 加入地月系统。
- 加入太阳系的其它行星。
- 使用GUI支持2D渲染。

## 效果展示

<a href="gol.gif"><img src="imgs/ss.gif" height=600px title="random"></a>

## 运行方式

```shell
python main.py
```

## 参考资料

1. [taichiCourse01/--Galaxy (github.com)](https://github.com/taichiCourse01/--Galaxy)
2. [用86行Python代码模拟太阳系 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/102375135)
3. [chongchonghe/Python-solar-system (github.com)](https://github.com/chongchonghe/Python-solar-system)
4. [Horizon API (nasa.gov)](https://ssd-api.jpl.nasa.gov/doc/horizons.html)

## 附录

### 天体数据

附一些收集到的天文数据。（本来想用来设置天体的参数，比如质量，但并不确定如何设置初始位置。后来参考**何崇崇**的代码，直接使用真实天体数据就可以了，而且使用不同量纲进行计算，可以不使用质量作为参数。

#### Solar System

| Solar System |   Numbers |
| ------------ | --------: |
| Planets      |         8 |
| Moons        |      200+ |
| Asteroids    | 1,113,527 |
| Comets       |     3,743 |

#### Sun

| Name | Star-type           | Age     | Radius, KM | Distance from Galactic Center |
| ---- | ------------------- | ------- | ---------- | ----------------------------- |
| Sun  | 黄矮星 Yellow Dwarf | ~45亿年 | 695500.0   | 26000光年                     |

#### Planets

| Name           | Star-type            | Moons | Mean Radius, KM | Length of Year     | Distance from Sun, AU |
| -------------- | -------------------- | ----- | --------------- | ------------------ | --------------------- |
| 水星 Mecury    | 类地行星 Terrestrial | 0     | 2439.4          | 88 Earth Days      | 0.4                   |
| 金星 Venus     | 类地行星             | 0     | 6051.8          | 225 Earth Days     | 0.7                   |
| 地球 Earth     | 类地行星             | 1     | 6371.0          | 365.25 Days        | 1                     |
| 火星 Mars      | 类地行星             | 2     | 3389.5          | 1.88 Earth Years   | 1.5                   |
| 木星 Jupiter   | 气体巨星 Gas Giant   | 79    | 69911.0         | 11.86 Earth Years  | 5.2                   |
| 土星 Saturn    | 气体巨星             | 62    | 58232 .0        | 29.45 Earth Years  | 9.5                   |
| 天王星 Uranus  | 冰巨星 Ice Giant     | 27    | 25362.0         | 84 Earth Years     | 19.8                  |
| 海王星 Neptune | 冰巨星               | 14    | 24622.0         | 164.81 Earth Years | 30.1                  |
| 冥王星 Pluto   | 矮行星 Dwarf Planet  | 5     | 1188.3          | 248.89 Earth Years | 39                    |

**PS：**

1. AU：天文单位（Astronomical Unit），地球与太阳间的平均距离，约为1.496亿千米。

#### Moons

| Name              | Star-type            | Mean Radius, KM | Length of Year | Distance from Earth, KM |
| ----------------- | -------------------- | --------------- | -------------- | ----------------------- |
| 月球 Earth's Moon | 类地行星 Terrestrial | 1737.5          | 27 Earth Days  | 385000                  |

#### 参考资料

1. [Home – NASA Solar System Exploration](https://solarsystem.nasa.gov/)
2. [Planetary Physical Parameters (nasa.gov)](https://ssd.jpl.nasa.gov/planets/phys_par.html)

### 其它的太阳系仿真系统

#### [NASA's Eyes](https://eyes.nasa.gov/)

> Powered by NASA's Eyes

支持交互的实时3D的真实数据可视化太阳系。

还有地球、火星、外太空的数据可视化系统。NASA's Eyes也提供了PC、移动端的软件。

NASA的图像纹理[资源](https://nasa3d.arc.nasa.gov/images)。

#### [SOLAR SYSTEM](https://www.solarsystemscope.com/)

> by SOLAR SYSTEM SCOPE (GER)

很漂亮，功能强大的3D仿真系统，交互很棒。

网站上有很丰富的内容。

- [“实验室”](https://www.solarsystemscope.com/lab)，关于特性的开发，能够对一些好的想法进行讨论和投票。
- [日志](https://www.solarsystemscope.com/skydiary/)，即将到来的天文事件、有趣的观测信息，为北半球的观星者提供资讯。
- 好玩的[星球折纸素材](https://www.solarsystemscope.com/paper/)，提供15面/26面/60面的不同纸模。
- 为Web系统提供了可嵌入页面的[组件](https://www.solarsystemscope.com/embed)。
- [百科](https://www.solarsystemscope.com/spacepedia/)
- [纹理素材](https://www.solarsystemscope.com/textures/)
- [周边商店](https://solarsystemscope.myspreadshop.com/)

#### [Harmony of the Spheres](https://github.com/TheHappyKoala/Harmony-of-the-Spheres)

> by Darrell A. Huffman, Hugo Granström, Paul West, John Van Vliet

这是一个牛顿n体[重力模拟器](https://gravitysimulator.org/)，不仅仅能够仿真太阳系，可以做很多东西，提供了丰富的示例程序。

#### [3D Solar System Simulator](https://theskylive.com/3dsolarsystem)

> by TheSkyLive.com

3D的实时太阳系仿真系统，简单漂亮。

#### [Solar system orrery (Atlas Digital)](https://atlas-digital.nl/live/solar/)

> by Jeroen Gommers (NED)
>
> [Planetarium zonnestelsel | Atlas Digital (atlas-digital.nl)](https://atlas-digital.nl/en/werk/solarsystem/)

具有设计感的2D太阳系，干净漂亮。有创意的月份网格和天文事件交互按钮。

该作品被用于位于荷兰 Franeker 的 Koninklijk Eise Eisinga 天文馆。

Atlas Digital 是一个交互式设计工作室，服务内容包括网页、信息图&数据可视化、地图、报道&杂志、仪表板&界面、动画。

两位创始人于2019年春天合作之前，Cas Mathijsen 是一位前端工程师，Jeroen Gommers 是一位设计师。

#### [If the Moon Were Only 1 Pixel](https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html)

> by Josh Worth

这不是一个太阳系仿真，这是一个比较有趣的创意动画，比较真实距离下太阳系行星的大小。支持多语言。

#### [\- solar system - (Shadertoy)](https://www.shadertoy.com/view/3dyfzm)

>  by anahit_movsesyan

一个效果不错的3D太阳系仿真系统，有八大行星、地月系统，颜色不错。

#### [Solar System (JavaLab)](https://javalab.org/en/solar_system_en/)

> by DongJoon

包含可简单交互的3D轨道系统和天体相关的数据条形图。主要是仿真轨道，天体质感比较一般。

DongJoon Lee 是一位韩国中学的科学教师，在 [JavaLab](https://javalab.org/en/about_javalab/)上完成了非常多的仿真动画，关于物理、化学、地球、天文、生物、数学等主题。

JavaLab历史：

- 1996，开始使用 Java applet 开发
- 2014，提供了超过500个科学仿真程序
- 2015，使用 JavaScript 重写了 Java 代码
- 2017，日文支持
- 2018，英文支持

DongJoon Lee 在2021年的韩国教师节（2021.5.15），荣获了韩国总统文在寅的嘉奖和奖章。

#### [Build Your Solar System (SimPop)](https://simpop.org/solar-system/solar-system.htm)

> by Animan Naskar
>
> Developed by students, for students!

一个有趣的2D交互小游戏。

屏幕中间是太阳，可以拖动任意的行星及一颗彗星到屏幕中，每个天体将有自己的运行轨道。

如果天体相遇，质量较小的天体将会爆炸。

Animan 和 Ankush，两名高中生，SimPop的维护者。制作了一些科学相关的仿真和游戏，主要是物理学科中的仿真，化学和生物仅有学科相关的小游戏。

#### [The Planets Today](https://www.theplanetstoday.com/) 

> by Hayling Graphics

表示行星位置的2D动画，交互较少，主要关注当前时间下的星球。

