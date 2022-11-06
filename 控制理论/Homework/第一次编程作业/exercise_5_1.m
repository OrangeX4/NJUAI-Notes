t = 0:0.005:5;
num = 15; den = [1 8 15]; sys = tf(num,den);

% y(t) = \frac{15}{2}e^{-3t} - \frac{15}{2}e^{-5t}
y1 = (15 / 2) * exp(-3 * t) - (15 / 2) * exp(-5 * t);
plot(t, y1), grid
xlabel('Analysis Method')

y2 = impulse(sys, t);
plot(t, y2), grid
xlabel('Impulse Function')