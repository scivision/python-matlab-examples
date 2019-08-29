% Shows different font use in GNU Octave (or Matlab).
% you can put these font settings into either:
% ~/.octaverc (Octave only)
% ~/Documents/startup.m (Matlab and Octave)
%
% Because Octave can use 3 different graphical backends, the defaults are not always
% optimal, particularly for HiDPI screens or publication plotting.
%
% NOTE: GNUPLOT IGNORES FONT SIZE SETTINGS!
% You must be using "ftlk" or "qt" backends.
% The 'qt' backend is ONLY available if you use "octave" not "octave-cli"
% QT is the preferred backend, FLTK and GNUplot are soft-deprecated.
%
% Further details:
% https://www.scivision.dev/gnu-octave-octaverc-default-suggested/
% https://octave.org/doc/v4.4.0/Text-Properties.html

try % Octave only
  backends = available_graphics_toolkits();
  disp('available backends: ')
  disp(backends)

  % graphics_toolkit('qt')  % force graphics backend like this, normally not needed.

  backend = graphics_toolkit();
  disp(['backend in use: ',backend])
end

%% pick a font
mult=1; % most fonts
font = "Courier";
font = "eufm10";
font = "FreeMono";
font = "Ani";
font = "Karumbi"; mult = 3;


%% bigger default font
set(0, "defaulttextfontsize", 24*mult)
set(0, "defaultaxesfontsize", 16*mult)

%% Thicker default lines
set(0, "defaultlinelinewidth", 2)

%% default font (falls back to sans serif if not found)

set(0, "defaulttextfontname", font)
set(0, "defaultaxesfontname", font)
%% Test plot
addpath([cwd,filesep,'tests'])

test_plot()

