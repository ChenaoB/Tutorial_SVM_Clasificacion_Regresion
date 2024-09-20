function [Xc, Yc, Curva] = curva_decision(a, b, x, t, lengthScale)
xlevel = linspace(min(x(:,1)), max(x(:,1)), 100)';
ylevel = linspace(min(x(:,2)), max(x(:,2)), 100)';
[Xc, Yc] = meshgrid(xlevel, ylevel);
Curva = zeros(length(xlevel));
k = zeros(length(x), length(Xc));
for zz = 1:length(xlevel)   
 Xcountor = [Xc(:,zz), Yc(:,zz)];
 for i = 1: 1:length(Xcountor)
  for j = 1: 1: length(x)
   k(j,i) = exp(-lengthScale*(x(j,:) - Xcountor(i,:))*(x(j,:) - Xcountor(i,:))');
  end
 end
 Curva(:,zz) = (a.*t)'*k + b; 
end


