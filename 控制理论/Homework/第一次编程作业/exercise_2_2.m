% basic sys
num1 = 4; den1 = 1; sys1 = tf(num1, den1);
num2 = 1; den2 = [1 1]; sys2 = tf(num2, den2);
num3 = [1 0]; den3 = [1 0 2]; sys3 = tf(num3, den3);
num4 = 1; den4 = [1 0 0]; sys4 = tf(num4, den4);
num5 = [4 2]; den5 = [1 2 1]; sys5 = tf(num5, den5);
num6 = 50; den6 = 1; sys6 = tf(num6, den6);
num7 = [1 0 2]; den7 = [1 0 0 14]; sys7 = tf(num7, den7);


% 1. compose sys
sysc1 = series(sys2, sys3);
sysc2 = feedback(sysc1, sys5);
sysc3 = feedback(sys4, sys6, 1);
sysc4 = series(sysc2, sysc3);
sysc5 = feedback(sysc4, sys7);
sys = series(sys1, sysc5);
sys


% 2. pzmap
pzmap(sys)


% 3. pole and zero
p = pole(sys);
z = zero(sys);
p
z