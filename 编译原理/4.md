# 编译原理

## 4. 语法分析

- LR 语法
    - LR 语法分析器
        - 状态栈
        - 输入
        - 语法分析表
            - ACTION
            - GOTO
    - ACTION 是面对某个格局 $(s_0\cdots s_m, a_i\cdots a_n)$ 时的行为, 查询表 ACTION[$s_{m}, a_{i}$]
        - 移入 $s$: 格局变为 $(s_0\cdots s_ms, a_{i+1}\cdots a_n)$
        - 规约 $A \to \beta$: 格局变为 $(s_0\cdots s_{m-r}s, a_{i}\cdots a_n)$, $r$ 是 $\beta$ 的长度, $s=\text{GOTO}[s_{m-r}, A]$
        - 接受
        - 报错
    - LR(0) 项族
    - SLR(1) 分析表
