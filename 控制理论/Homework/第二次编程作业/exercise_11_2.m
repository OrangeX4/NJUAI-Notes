a = [0 0 0 1 0 0; 0 0 0 0 1 0; 0 0 0 0 0 1; 7.3809 0 0 0 2 0; 0 -2.1904 0 -2 0 0; 0 0 -3.1904 0 0 0];
c = [0 1 0 0 0 0];
d = [0];
b1 = [0; 0; 0; 1; 0; 0];
b2 = [0; 0; 0; 0; 1; 0];
b3 = [0; 0; 0; 0; 0; 1];
sys_ss_1 = ss(a,b1,c,d);
sys_ss_2 = ss(a,b2,c,d);
sys_ss_3 = ss(a,b3,c,d);
% (a)
evalues = eig(a)
% (b)
Pc1 = ctrb(sys_ss_1); dt1 = det(Pc1)
% (c)
Pc2 = ctrb(sys_ss_2); dt2 = det(Pc2)
% (d)
Pc3 = ctrb(sys_ss_3); dt3 = det(Pc3)
% (e)
sys_tf = tf(sys_ss_2);
sys_tf = minreal(sys_tf)
% (f)
sys_ss = ss(sys_tf );
Pc = ctrb(sys_ss); dt_Pc = det(Pc)
% (g)
P = [-1+i; -1-i;-10;-10];
[a, b] = ssdata(sys_ss);
K = acker(a,b,P)