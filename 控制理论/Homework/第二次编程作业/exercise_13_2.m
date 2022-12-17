% (a)
num1 = [1]; den1 = [1 0]; T1 = 1;
sys1 = tf(num1,den1);
sys_d1 = c2d(sys1,T1,'zoh')
% (b)
num2 = [1 0]; den2 = [1 0 2]; T2 = 1;
sys2 = tf(num2,den2);
sys_d2 = c2d(sys2,T2,'zoh')
% (c)
num3 = [1 4]; den3 = [1 3]; T3 = 1;
sys3 = tf(num3,den3);
sys_d3 = c2d(sys3,T3,'zoh')
% (d)
num4 = [1]; den4 = [1 8 0]; T4 = 1;
sys4 = tf(num4,den4);
sys_d4 = c2d(sys4,T4,'zoh')