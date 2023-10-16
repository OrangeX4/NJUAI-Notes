# 软件工程作业 1

## 201300035 方盛俊

## (1)

系统整体架构使用 UML 图中的 **类图** 表示如下：

![](./images/uml.png)

其中关系有 Is-A 和 Has-A 关系。

Is-A 关系的一个实例有：CppCompare 是 AutoCompare 的一个实现或继承。

Has-A 关系的一个实例有：Cluster 类里包含了 Compare 类。

## (2)

Is-A 关系共有 2 个。

Has-A 关系共有 6 个。

## (3)

Is-A 关系的一个实例有：CppCompare 是 AutoCompare 的一个实现或继承。

该关系可以实现为 Has-A。

我们可以 CppCompare 不实现为 AutoCompare 的一个实现或继承，而是作为 AutoCompare 里包含的一个子类。这种子类可以动态地加以注册。

## (4)

Has-A 关系有 Cluster 类里包含了 Compare 类等。

这种关系很难实现为 Is-A。因为 Compare 包含的信息要少于 Cluster 的信息，很难且也没必要将其变为 Is-A 关系，对于其他该图中的 Has-A 关系也同理。
