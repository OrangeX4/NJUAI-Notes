num = [25]; den = [1 5 0]; sys = tf(num,den);
sys_cl = feedback(sys, 1);

t = 0:0.01:2;
y = step(sys_cl, t);
plot(t, y), grid

[m_pt, m_pt_index] = max(y);
m_pt
t_p = t(m_pt_index)

% Find the time at which the step response is 0.98
t_s = interp1(y, t, 0.98)

