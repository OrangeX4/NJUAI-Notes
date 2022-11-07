K = 0:0.1:5;
n = length(K);
for i = 1:n
    num = [1]; den = [1 5 K(i)-3 K(i)]; sys = tf(num, den);
    sys_cl = feedback(sys, 1);
    p(:, i) = pole(sys_cl);
end
plot(real(p), imag(p), 'x'), grid

for i = 1:n
    if max(real(p(:, i))) >= 0
        break
    end
end
K(i)

K = K(i)
num = [1]; den = [1 5 K(i)-3 K(i)]; sys = tf(num, den);
sys_cl = feedback(sys, 1);
p = pole(sys_cl)