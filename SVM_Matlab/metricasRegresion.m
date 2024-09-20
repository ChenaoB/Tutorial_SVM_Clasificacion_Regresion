function [ro, ERMS] = metricasRegresion(yz, y)
r = length(yz); 
ro = (1/r)*((yz-mean(yz))'*(y -mean(y)))/sqrt(var(yz,1)*var(y,1));
ERMS = sqrt((yz-y)'*(yz - y)/r);
end

