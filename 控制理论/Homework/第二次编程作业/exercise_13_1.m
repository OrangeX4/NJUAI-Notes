num =[ 0.2145 0.1609]; den = [1 -0.75 0.125];
t = 0:1:50;
T = 1;
sysd = tf(num,den,T);
step(sysd,t)
stepinfo(sysd)