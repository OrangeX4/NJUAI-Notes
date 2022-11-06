% z = 5, 10, 15
t = 0:0.005:5;
y1 = get_y_2_3(get_sys_2_3(5), t);
y2 = get_y_2_3(get_sys_2_3(10), t);
y3 = get_y_2_3(get_sys_2_3(15), t);
plot(t, y1, t, y2, ':', t, y3, '--'), grid


% 1. calculate transfer function
function sys = get_sys_2_3(z)
    num = [20 / z, 20];
    den = [1, 3, 20];
    sys = tf(num, den);
end


% 2. draw the curve with step sinal
function y = get_y_2_3(sys, t)
    [y, ~] = step(sys, t);
end

