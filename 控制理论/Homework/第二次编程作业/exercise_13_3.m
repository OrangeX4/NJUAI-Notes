% (a)
num = 1.7 * [1 0.46]; den = [1 1 0.5];
T = 1;
t = 0:1:20;
sysd = tf(num,den,T);
step(sysd, t)
% (b)
num = 1.7 * [1 0.46]; den = [1 1 0.5];
T = 0.1;
t = 0:0.1:2;
sysd = tf(num,den,T);
sys = d2c(sysd)
% (c)
step(sys, t)