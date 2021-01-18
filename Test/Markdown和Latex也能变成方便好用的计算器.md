# Markdown和Latex也能变成方便好用的计算器

很多人都用过 VSCode 来写 Markdown 和 Latex，或许还会用它来记笔记、写作业和写论文。

相信有人也碰到过这样的麻烦：用 Latex 输入了一个分式 \frac{1}{2}，想要计算还得手动将它改成 1/2，再打开其他软件进行计算；又或是用 Latex 写了一个矩阵，想要计算它的行列式，还得打开 Matlab 重新输入一遍整个矩阵，得到结果还要重新改写成 Latex。

有没有办法简化这一整个流程呢？当然是有的！

我写的 VSCode 插件 Better Markdown & Latex Shortcuts 迎来了重大的升级，加入了计算器功能。以后用 VSCode 写 Markdown 或者 Latex 的时候，便可以随手进行一些四则运算或矩阵运算之类的运算了。

# Better Markdown & Latex Shortcuts 插件安装

在这里，默认你已经安装了 VSCode 和相关的 Markdown 数学公式支持插件或是 Latex 编译环境。

要使用这个插件，你只需要在vscode的插件市场搜索 “Better Markdown & Latex Shortcuts” 或 “Orangex4”，并安装名为 "Better Markdown&Latex Shortcuts" 的插件.

![img](https://s3.ax1x.com/2020/12/02/DIW5mF.png)

### Github地址

[Github](https://github.com/OrangeX4/Better-Markdown-Latex-Shortcuts)

# 用法

## 行内复制与移动

### 复制

使用快捷键 "Shift + Alt + ←" 将选中内容在行内向左复制。

使用快捷键 "Shift + Alt + →" 将选中内容在行内向右复制。

![copy](https://s3.ax1x.com/2020/12/02/DIg8ds.gif)

### 多行复制

![multicopy](https://s3.ax1x.com/2020/12/02/DIgGon.gif)

### 移动

使用快捷键 "Alt + ←" 将选中内容在行内向左移动。

使用快捷键 "Alt + →" 将选中内容在行内向右移动。

![move](https://s3.ax1x.com/2020/12/02/DIgYiq.gif)

### 单选

使用快捷键 "Ctrl + Alt + U" 将光标变为一个。

![single](https://s3.ax1x.com/2020/12/02/DIgtJ0.gif)


## 计算器功能

计算器功能一共有三个快捷键，分别是：

1. 定义（Define）："Shift + Ctrl + Alt + D"
2. 等于（Equal）："Shift + Ctrl + Alt + E"
3. 替换（Replace）："Shift + Ctrl + Alt + R"

这三个命令实际上效果相同，唯一区别是输出的内容。

“定义”什么都不会输出，通常用来定义变量，如 “x=3”。

“等于”会将计算结果加上等于号并接在当前选中区域之后，如 “1+2” 会变成 “1+2=3”。

“等于”会用计算结果替换选中区域，如 “1+2” 会变成 “3”。

目前计算器支持数值运算，函数运算，多项式运算，矩阵运算等诸多运算，并且是用 Latex 表达式直接计算，输出结果也会自动转换为 Latex 形式。

![Calculator](https://ae01.alicdn.com/kf/U775488c7dd0a4fa682ffed6b36ef12ab1.jpg)

PS：运算相关支持使用的是 “Mathjs” 库，一切 Mathjs 表达式均可以正常使用。


## 常用 Snippets 

插件还内置了许多的 Snippets，让你写 Latex 数学公式更为简单快捷。

详细的 Snippets 请参考我的博客或者插件的介绍页面。

![](https://ae01.alicdn.com/kf/U649466346e7a45368747001600b89921s.jpg)


# 最后

欢迎来我的博客，orangex4.cool，我的github，抑或是邮箱 318483724@qq.com 提交反馈！

感谢！