% 1.
num_g = [1 1]; den_g = [1 2]; sys_g = tf(num_g, den_g);
num_h = 1; den_h = [1 1]; sys_h = tf(num_h, den_h);
sys = feedback(sys_g, sys_h);
sys


% 2.
pzmap(sys);
p = pole(sys);
z = zero(sys);
p
z


% 3.
sysm = minreal(sys);
sysm
