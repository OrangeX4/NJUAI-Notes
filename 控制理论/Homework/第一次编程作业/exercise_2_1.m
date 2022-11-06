% define parameters
J = 10.8E8;
k = 10.8E8;
a = 1;
b = 8;


% 3. 100%, 80% and 50% J
sys = get_sys_2_1(J, k, a, b)
t = 0:0.1:100;
y1 = get_y_2_1(get_sys_2_1(J, k, a, b), t);
y2 = get_y_2_1(get_sys_2_1(0.8 * J, k, a, b), t);
y3 = get_y_2_1(get_sys_2_1(0.5 * J, k, a, b), t);
plot(t, y1, t, y2, ':', t, y3, '--'), grid
xlabel('Time (s)')
ylabel('theta (deg)')


% 1. calculate transfer function
function sys = get_sys_2_1(J, k, a, b)
    num1 = [k, k * a];
    den1 = [1, b];
    num2 = 1;
    den2 = [J, 0, 0];

    [num, den] = series(num1, den1, num2, den2);
    [num, den] = feedback(num, den, 1, 1, -1);
    sys = tf(num, den);
end


% 2. draw the curve with step sinal A = 10
function y = get_y_2_1(sys, t)
    opt = stepDataOptions('StepAmplitude', 10);
    [y, ~] = step(sys, t, opt);
end

