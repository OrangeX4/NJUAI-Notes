num = [1 5]; den = [1 0 0]; sys = tf(num,den);
rlocus(sys), grid
hold on
plot([-1.0 -1.0],[-6 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 -6],'--')
hold off
[kpi,poles] = rlocfind(sys)

