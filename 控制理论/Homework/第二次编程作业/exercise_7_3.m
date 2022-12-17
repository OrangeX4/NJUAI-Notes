ng = 10; dg = conv([1 10 0], [1 5]); sysg = tf(ng, dg);
nh = conv([1 0.01], [1 5.5]);
dh = conv([1 6.5], [1 0.0001]); 
sysh = tf(nh, dh);
rlocus(sysg * sysh)
K = 8.58; sysh = tf(K * nh, dh);
sys = series(sysg, sysh);syscl = feedback(sys, 1)
stepinfo(syscl)
step(syscl);
Kv = 10 * 8.58 * 0.01 * 5.5 / 10 / 6.5 / 0.0001 / 5
systd = feedback(sysg, sysh);
step(systd)