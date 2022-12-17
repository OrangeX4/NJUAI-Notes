num = [1]; den = [1 8 10 1]; sys = tf(num, den);
rlocus(sys), grid
hold on
plot([0 -6*tan(45*pi/180)],[0 6],'--',...
[0 -6*tan(45*pi/180)],[0 -6],'--')
hold off
[kpi,poles] = rlocfind(sys)
