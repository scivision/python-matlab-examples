% finds directory this .m file exists in

function path = cwd()

path = fileparts(mfilename('fullpath'));

end
