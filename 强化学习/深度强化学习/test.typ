#import "@local/mytemplate:0.1.0": *

#set heading(numbering: Numbering.with(first-level: "一、", "1.1"))

// apply the template
#show: report.with(
    media: "screen",
    // theme: "dark",
    // date: "2023 年春季", 
    // subject: "课程", 
    // title: "标题", 
    // author: "201300035 方盛俊 人工智能学院",
    par-indent: false,
    show-outline: false,
)

// 数学公式
#show math.equation.where(block: false): it => [#math.equation(block: true, numbering: none, it)<inline-math-equation>]
#show <inline-math-equation>: it => box(it)

= 价值学习

你好测试

士大夫 $integral 1 + 2$

