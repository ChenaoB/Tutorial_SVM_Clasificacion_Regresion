function [K] = kernel(X1,X2, lengthScale)
K = zeros(length(X1), length(X2));
for d=1:length(X1)
    for e=1:length(X2)
        K(d,e) = exp(-lengthScale*((X1(d,:)-X2(e,:))*(X1(d,:)-X2(e,:))'));
    end
end
end

