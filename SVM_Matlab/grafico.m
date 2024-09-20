function  grafico(Xcurva, Ycurva, Nivelcurva, x, t, z, y, a)
Xclasst1 = x(find(t==1),:);
Xclasst2 = x(find(t==-1),:);

Xclassy1 = z(find(y==1),:);
Xclassy2 = z(find(y==-1),:);

Xclass1 = [Xclasst1; Xclassy1];
Xclass2 = [Xclasst2; Xclassy2];

plot(Xclass1(:,1), Xclass1(:,2), '.r')
hold on
plot(Xclass2(:,1), Xclass2(:,2), '.b')
hold on
VectoresSoporte = x(find(abs(a)~=0),:);
length(VectoresSoporte)
plot(VectoresSoporte(:,1), VectoresSoporte(:,2), 'og')
hold on
contour(Xcurva, Ycurva, Nivelcurva, [0 0], 'Color', 'k')
legend('tn=1', 'tn=-1', 'Vectores de soporte', 'y(z)=0')
xlabel('x1')
ylabel('x2')

end

