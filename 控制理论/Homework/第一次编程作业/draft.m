clear;
K = 1;
num1 = K * [1 1]; den1 = [1]; sys1 = tf(num1, den1);
num2 = [2]; den2 = [1 4 0]; sys2 = tf(num2, den2);
num3 = [3]; den3 = [1 2 5]; sys3 = tf(num3, den3);
sys = sys1 * sys2;
sys_cl = feedback(sys, sys3);

t = 0:0.01:5;
[y, ~] = step(sys_cl, t);
plot(t, y), grid;