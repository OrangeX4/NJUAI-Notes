A = 'ARTISTOIL'
n = len(A)

def IsWord(s):
    return s == 'ART' or s == 'IS' or s == 'TOIL' or s == 'ARTIST' or s == 'OIL'

# 用于动态规划的数组
p = [0 for _ in range(n + 1)]

# 初始化 p[0]
p[0] = 1

# 主循环
for k in range(1, n + 1):
    sum = 0
    for i in range(0, k):
       if IsWord(A[i : k]):
           sum += p[i]
    p[k] = sum

# 输出最后结果
print(p[n])