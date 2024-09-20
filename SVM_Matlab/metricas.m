function [TRN,  TPR, PVV,  Acc] = metricas(yz,y)
  VP = 0;
  VN = 0;
  FP = 0;
  FN = 0;
  for j=1:length(y)
    if(y(j)==1)   
      if(y(j)== yz(j))
        VP = VP + 1;
      else
        FN = FN + 1;
      end
    else
      if(y(j)==yz(j))
        VN = VN + 1;
      else
        FP = FP + 1;
      end
    end
  end
  TRN = VN/(VN+FP);
  TPR = VP/(VP+FN);
  PVV = VP/(VP+FP);
  Acc = (VP+VN)/(VP+VN+FP+FN);
end

