A=[0 1 0;0 0 1;-4.3 -1.7 -6.7]; B=[0;0;0.35]; C=[0 1 0]; D=[0];
% (a)
% 反馈增益矩阵
p=[-1.4+1.4*j;-1.4-1.4*j;-2];
K=acker(A,B,p)
% 观测器增益矩阵
q=[-18+5*j;-18-5*j;-20];
L = acker(A',C',q); L=L'
% (b)
Ac=[A -B*K;L*C A-B*K-L*C]; 
Bc=[zeros(6,1)];
Cc=eye(6); 
Dc=zeros(6,1);
sys=ss(Ac,Bc,Cc,Dc); 
% (c)
x0=[1;0;0;0.5;0.1;0.1]; t=[0:0.001:3.5];
[y,t]=initial(sys,x0,t);
subplot(311)
plot(t,y(:,1),t,y(:,4),'--'), grid
subplot(312)
plot(t,y(:,2),t,y(:,5),'--'), grid
subplot(313)
plot(t,y(:,3),t,y(:,6),'--'), grid