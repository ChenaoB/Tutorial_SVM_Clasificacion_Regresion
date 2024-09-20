function [x,t,z,y] = dividir_datos_entrenamiento_validacion(X1,X2)
 n1 = size(X1,2);
 nc = n1 - 1;
 x = X1(:,1:nc);
 t = X1(:,n1);
 z = X2(:,1:nc);
 y = X2(:,n1);
end

