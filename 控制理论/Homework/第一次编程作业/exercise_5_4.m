num1 = [21]; den = [1 0]; sys1 = tf(num1,den);
num2 = [1]; den = [1 2]; sys2 = tf(num2,den);
sys = series(sys1, sys2);
sys_cl = feedback(sys, 1);
sys_cl

t = 0:0.01:10;
y = step(sys_cl, t);
plot(t, y), grid