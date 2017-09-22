function [mn, mx, ave]= mnmxave(x,y)

mn=min(x,y);
mx=max(x,y);
ave=mean([x y]);