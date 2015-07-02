% This function is a hack around the new R2014b+ graphics system that removed
% the ability to manipulate the children of contour(), contourf().
% It flattens a contour and pcolor, with a bit of sharpness loss due to imresize
% operation. 
% Certainly not optimal but "it works" to put a contour on an image in 3-D.
% Michael Hirsch

function contourImage2()
    z0=150;
    [x,y,z,Ne] = fakedata();
%% 2-D contour with ONE color over grayscale image
    [ax,himg] = baseplot(x,y); %plots pcolor image
    colormap(ax,'gray')
    contour(x,y,Ne(:,:,4),'b')
    
    
%% 3-D contour over image demo    
    %things that don't work
    %[ax,himg] = baseplot(x,y);
    %set(himg,'zdata',z0*ones(ny,nx)) %moves pcolor plot to 150km
    %contourhack(x,y,z0,Ne,ax)
    %hack that works
    flat = flattening(x,y,Ne);
    plot3Dflat(x,y,z0,flat)
end


function [x,y,z,Ne] = fakedata()
    Ne = load('wmri'); Ne = Ne.X;
    [ny,nx,nz]=size(Ne);

    x=linspace( -300,300,nx);
    y=linspace(-250,250,ny);
    z=linspace(100,500,nz);
end 

function [ax,himg] = baseplot(x,y)
    ny = length(y); nx = length(x);
    figure(1),clf()
    ax = axes('parent',1,'nextplot','add');
    himg = pcolor(x,y,rand(ny,nx)*30,'parent',ax);
end 

function contourhack(x,y,z0,Ne,ax)
% these hacks don't work in R2014b+ !
 
    % hacking contour, contourf
    [C,h2] = contour(x,y,Ne(:,:,4),'parent',ax); %stuck at z=0
    hh2 = get(h2,'children') % no children in the new R2014b+ graphics system
    % hacking contour3
    figure(10),clf()
    ax10=axes('parent',10);
    [C,h]= contour3(x,y,Ne(:,:,4),'parent',ax10); 
    set(h,'zdata',z0*ones(length(y),length(x)))
    hc = get(h,'Children') % contours disappear!
end
%% hack by imwrite/imread flattening image
% http://www.mathworks.com/matlabcentral/answers/101413-how-can-i-add-text-to-an-image-and-make-the-text-become-part-of-the-image-within-matlab
function flat = flattening(x,y,Ne)
    ny = length(y); nx = length(x);
    
    figure(20),clf()
    ax=axes('parent',20,'nextplot','add');
    pcolor(x,y,rand(ny,nx)*30,'parent',ax);
    contour(x,y,Ne(:,:,4),'parent',ax)
    %completely fill figure so that getframe() gets most possible resolution. Not strictly necesary.
    axis('off')
    set(ax,'pos',[0 0 1 1]) 
    % flatten contour to background in the form of an RGB image (as if you read
    % in a JPEG or something)
    img = getframe(ax);
    flat = rgb2gray(img.cdata);
    flat = imresize(flat,[ny,nx]); % hack
end

function plot3Dflat(x,y,z0,flat)
    ny = length(y); nx = length(x);

    figure(30),clf()
    ax = axes('parent',30);
    h = pcolor(x,y,flat,'parent',ax);
    set(h,'zdata',z0*ones(ny,nx)) %moves flattened pcolor, contour plot to 150km

end
