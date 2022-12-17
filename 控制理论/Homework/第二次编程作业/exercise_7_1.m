num1 = [10]; den1 = [1 14 43 30]; sys1 = tf(num1, den1);
rlocus(sys1);
num2 = [1 20]; den2 = [1 4 20]; sys2 = tf(num2, den2);
rlocus(sys2);
num3 = [1 1 2]; den3 = [1 6 10 0]; sys3 = tf(num3, den3);
rlocus(sys3);
num4 = [1 4 6 10 6 4]; den4 = [1 4 4 1 1 10 1]; sys4 = tf(num4, den4);
rlocus(sys4);