clf

w1 = 2; z1 = 0;
w2 = 2; z2 = 0.1;
w3 = 1; z3 = 0;
w4 = 1; z4 = 0.2;
t = [0:0.01:25];

num1 = [w1^2]; den1 = [1 2*z1*w1 w1^2];
sys1 = tf(num1, den1);
[y1, x1] = impulse(sys1, t);

num2 = [w2^2]; den2 = [1 2*z2*w2 w2^2];
sys2 = tf(num2, den2);
[y2, x2] = impulse(sys2, t);

num3 = [w3^2]; den3 = [1 2*z3*w3 w3^2];
sys3 = tf(num3, den3);
[y3, x3] = impulse(sys3, t);

num4 = [w4^2]; den4 = [1 2*z4*w4 w4^2];
sys4 = tf(num4, den4);
[y4, x4] = impulse(sys4, t);

subplot(221), plot(t, y1), title('wn=2, zeta=0')
subplot(222), plot(t, y2), title('wn=2, zeta=0.1')
subplot(223), plot(t, y3), title('wn=1, zeta=0')
subplot(224), plot(t, y4), title('wn=1, zeta=0.2')
clf