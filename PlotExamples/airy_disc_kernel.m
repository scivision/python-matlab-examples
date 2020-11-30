% https://github.com/astropy/astropy/blob/astropy/modeling/functional_models.py
function z = airy_disc_kernel(N, radius)
arguments
  N (1,1) {mustBePositive}
  radius (1,1) {mustBePositive} = 3
end

x_0=0;
y_0=0;
%%
x = -N/2:N/2;
y = x;

[x,y] = meshgrid(x,y);

j1zero = 3.8317059702075125; % scipy.special.jn_zeros(1, 1)[0]

rz = j1zero / pi;
r = sqrt((x - x_0) .^ 2 + (y - y_0) .^ 2) ./ (radius ./ rz);

z = ones(size(r));

rt = pi * r(r > 0);
z(r > 0) = (2 * besselj(1,rt) ./ rt) .^ 2;

end % function
