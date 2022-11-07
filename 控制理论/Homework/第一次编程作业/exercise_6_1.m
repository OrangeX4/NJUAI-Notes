% (b)
num = 1; den = [1 2 2 4 1 2]; sys = tf(num, den);
pole(sys)
pzmap(sys)

% (c)
t = 0:0.01:50;
y = step(sys, t);
plot(t, y), grid