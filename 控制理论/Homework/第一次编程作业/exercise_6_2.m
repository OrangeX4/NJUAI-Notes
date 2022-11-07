sys_fast = get_sys_6_2(0.1)
pole(sys_fast)
pzmap(sys)
sys_slow = get_sys_6_2(0.6)
pole(sys_slow)
pzmap(sys_slow)

% find maximum pilot time delay
for tau = 0.1:0.0001:0.6
    sys = get_sys_6_2(tau);
    if max(real(pole(sys))) >= 0
        break
    end
end
tau
sys
pole(sys)
pzmap(sys)

function sys = get_sys_6_2(tau)
    K = 1; tau1 = 2; tau2 = 0.5;
    num1 = -K * [tau1*tau tau-2*tau1 -2];
    den1 = [tau2*tau tau+2*tau2 2];
    sys1 = tf(num1, den1);
    num2 = [-10]; den2 = [1 10]; sys2 = tf(num2, den2);
    num3 = [-1 -6]; den3 = [1 3 6 0]; sys3 = tf(num3, den3);
    sys = sys1 * sys2 * sys3;
    sys_cl = feedback(sys, 1);

    sys = sys_cl;
end