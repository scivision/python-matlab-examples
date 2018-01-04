clear
try
  pkg load image
end

N = 256;
Nairy = 15;

airykern = airy_disc_kernel(Nairy);

I = zeros(N,N);
I = imnoise(I, 'salt & pepper', 0.0001);
I = imfilter(I, airykern);

figure(1)
imagesc(I)
axis('xy')
title('simulated star field')
%https://www.mrao.cam.ac.uk/~dag/CUBEHELIX/CubeHelix.m
colormap(flipud(cubehelix))

colorbar()

%figure(2)
%pcolor(log10(airykern))
%title('Airy disc kernel')