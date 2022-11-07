num1 = [0.5 2]; den1 = [1 0]; sys1 = tf(num1,den1);
num2 = [1]; den2 = [1 2 0]; sys2 = tf(num2,den2);
sys = series(sys1, sys2);
sys_cl = feedback(sys, 1);
sys_cl

t = 0:0.01:20;
u = t;
y1 = impulse(sys_cl, t);
y2 = step(sys_cl, t);
y3 = lsim(sys_cl, u, t);
subplot(3,1,1), plot(t, y1), grid, title('Impulse Response')
subplot(3,1,2), plot(t, y2), grid, title('Step Response')
subplot(3,1,3), plot(t, y3, t, u), grid, title('Ramp Response')
