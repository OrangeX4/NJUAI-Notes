#import "@local/mytemplate:0.1.0": *


#set heading(numbering: Numbering.with(first-level: "一、", "1.1"))

// apply the template
#show: report.with(
    media: "screen",
    // theme: "dark",
    // date: "2023 年春季", 
    // subject: "课程", 
    // title: "标题", 
    par-indent: false,
    show-outline: false,
)