K = 0:0.1:30;
n = length(K);
for i = 1:n
    num1 = [5]; den1 = [1 10 0]; sys1 = tf(num1, den1);
    num2 = [2 K(i)]; den2 = [1 0]; sys2 = tf(num2, den2);
    sys_cl = feedback(sys1, sys2);
    p(:, i) = pole(sys_cl);
end
plot(real(p), imag(p), 'x'), grid

K = 20;
num1 = [5]; den1 = [1 10 0]; sys1 = tf(num1, den1);
num2 = [2 K]; den2 = [1 0]; sys2 = tf(num2, den2);
sys_cl = feedback(sys1, sys2);
pole(sys_cl)