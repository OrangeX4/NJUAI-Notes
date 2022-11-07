t = 0:0.01:50;
u = t;
num = [1 10]; den = [1 15 0 0]; sys = tf(num,den);
sys_cl = feedback(sys, 1);

y = lsim(sys_cl, u, t);
plot(t, y), grid