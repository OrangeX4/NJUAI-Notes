numg = [1]; deng = [1 5 6]; sysg = tf(numg,deng);
t = [0:0.1:15];
% (a)
sys1 = sysg;
rlocus(sys1), grid
hold on
plot([-0.4 -0.4],[-6 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 -6],'--')
hold off
[kp,poles] = rlocfind(sys1)
% (b)
numc = [1]; denc = [1 0]; sysc = tf(numc,denc);
sys2 = series(sysc,sysg); 
figure
rlocus(sys2), grid
hold on
plot([-0.4 -0.4],[-6 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 -6],'--')
hold off
[ki,poles] = rlocfind(sys2)
% (c)
figure
numc = [1 1]; denc = [1 0]; sysc = tf(numc,denc);
sys3 = series(sysc,sysg); 
rlocus(sys3), grid
hold on
plot([-0.4 -0.4],[-6 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 6],'--',...
[0 -6*tan(36.2*pi/180)],[0 -6],'--')
hold off
[kpi,poles] = rlocfind(sys3)
% (d)
figure
sys1_o = kp*sys1; sys1_cl = feedback(sys1_o,[1]);
sys2_o = ki*sys2; sys2_cl = feedback(sys2_o,[1]);
sys3_o = kpi*sys3; sys3_cl = feedback(sys3_o,[1]);
[y1,t] = step(sys1_cl,t);
[y2,t] = step(sys2_cl,t);
[y3,t] = step(sys3_cl,t);
plot(t,y1,t,y2,'--',t,y3,':'),grid
xlabel('时间 [s]'),ylabel('y(t)')
title('Gc(s): 比例控制器 (solid), 积分控制器 (dashed) & PI 控制器 (dotted)')
