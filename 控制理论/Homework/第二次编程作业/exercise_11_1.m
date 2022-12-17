a=[0 1 0 0 0;-0.1 -0.5 0 0 0;0.5 0 0 0 0;0 0 10 0 0;0.5 1 0 0 0];
b=[0;1;0;0;0];
c=[0 0 0 1 0];
d=[0];
sys_ss = ss(a,b,c,d);
% (a)
Pc = ctrb(sys_ss);
dt_Pc = det(Pc)
% (b)
sys_tf = tf(sys_ss)
sys_new = minreal(sys_tf);
sys_new_ss = ss(sys_new)
% (c)
Pc_new = ctrb(sys_new_ss);
dt_Pc_new = det(Pc_new)