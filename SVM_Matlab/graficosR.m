function [SPARS] = graficosR(x,t,z,y,yz,apuntos)
Nx = length(x);  
an = apuntos(1:Nx);
am = apuntos(Nx+1:end); 
SPARS = find(an-am~=0);
plot(z, yz, '.g')
hold on
plot(z, y, '.b')
hold on
plot(x(SPARS), t(SPARS), 'ok')
hold on
xlabel('x')
ylabel('y')
legend('y(z)', 'y', 'Vectores de soporte')
figure(2)
plot(y,y, 'b')
hold on
plot(y,yz, '.k')
xlabel('y')
ylabel('y(z)')
legend('y vs y', 'y vs y(z)')
end

