function contourOverImage()
[X,Y,Z,V] = testdata();
plotimagecontour(X,Y,Z,V)
end

function [X,Y,Z,V] = testdata()
delta = 0.1;
V = 0.1*rand(61,61);
x = -3:delta:3;
y = -3:delta:3;
[X,Y] = meshgrid(x,y);
Z = reshape(mvnpdf([X(:),Y(:)]), size(X));
end

function plotimagecontour(x,y,Z,V)
%% 2-D
figure(1),clf(1)
% image
ax = axes('nextplot','add');
h2=pcolor(x,y,V,'parent',ax);
colorbar('peer',ax)
% contour
contour(x,y,Z,'parent',ax)
%% 3-D
altkm = 150; %arbitrary

figure(2),clf(2)
%image
a3 = axes('nextplot','add');
hi3 = pcolor(x,y,V,'parent',a3);
set(hi3,'zdata',0*V+altkm)

[C3,hc3] = contour(x,y,Z,'parent',a3);
%set(hc3,'zdata',0*V+altkm*1.1) %no, the zdata is what the noisy data is.
end
