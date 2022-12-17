a=[0 1 0; 0 0 1; -3 -2 -5];
b=[0;0;1];
c=[1 0 0];
d=[0];
% (a)
sys_ss = ss(a,b,c,d)
sys_tf = tf(sys_ss)
% (b)
x0 = [0 -1 1];
t = [0:0.1:10];
u = 0*t;
[y,t,x] = lsim(sys_ss,u,t,x0);
plot(t,x(:,1),t,x(:,2),'--',t,x(:,3),':');
xlabel('time (s)'), ylabel('x(t)'), grid
title('x1 (solid); x2 (dashed); x3 (dotted)')
xf_sim = x(length(t),:)'
% (c)
t1 = 10;
Phi = expm(a*t1);
xf_phi = Phi*x0'