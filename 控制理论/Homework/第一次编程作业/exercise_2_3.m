% z = 5, 10, 15
t = 0:0.005:5;
y1 = get_y(get_sys(5), t);
y2 = get_y(get_sys(10), t);
y3 = get_y(get_sys(15), t);
plot(t, y1, t, y2, ':', t, y3, '--'), grid


% 1. calculate transfer function
function sys = get_sys(z)
    num = [20 / z, 20];
    den = [1, 3, 20];
    sys = tf(num, den);
end


% 2. draw the curve with step sinal
function y = get_y(sys, t)
    [y, ~] = step(sys, t);
end

