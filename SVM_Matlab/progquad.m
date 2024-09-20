function [a] = progquad(P,qt, g,h, A, B, lb, ub)
a = quadprog(P,qt, g,h, A, B, lb, ub);
Spars = find(abs(a)<0.00001);
a(Spars) = 0;
a;
%% Se umbralizan los vectores de soporte
end

