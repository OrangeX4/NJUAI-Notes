import matplotlib.pyplot as plt
from collections import Counter

values = [0.81, 0.74, 0.62, 0.55, 0.44, 0.35, 0.25, 0.21]
labels = [1, 1, 0, 1, 0, 1, 0, 0]

P = [1.0]
R = [0.0]
TPR = [0.0]
FPR = [0.0]

for i in range(1, len(values) + 1):
    P_counter = Counter(labels[:i])
    N_counter = Counter(labels[i:])
    TP = P_counter.get(1, 0)
    FP = P_counter.get(0, 0)
    FN = N_counter.get(1, 0)
    TN = N_counter.get(0, 0)
    P.append(TP / (TP + FP))
    R.append(TP / (TP + FN))
    TPR.append(TP / (TP + FN))
    FPR.append(FP / (TN + FP))

P.append(0.0)
R.append(1.0)
TPR.append(1.0)
FPR.append(1.0)

S = 0.5 * sum([(FPR[i] - FPR[i - 1]) * (TPR[i] + TPR[i - 1])  for i in range(1, len(TPR))])

print('P: ' + str(P))
print('R: ' + str(R))
print('TPR: ' + str(TPR))
print('FPR: ' + str(FPR))
print('S: ' + str(S))

# 绘图
plt.rcParams["font.sans-serif"] = ["simhei"]
plt.rcParams["axes.unicode_minus"] = False

plt.plot(R, P)
plt.xlabel('查全率')
plt.ylabel('查准率')
plt.show()

plt.plot(FPR, TPR)
plt.xlabel('假正例率')
plt.ylabel('真正例率')
plt.show()
