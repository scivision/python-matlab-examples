% Matlab >= R2014b -- independent colormap on subaxes of same figure

f = figure(1); clf()
a1 = subplot(1,2,1,'parent',f);
a2 = subplot(1,2,2,'parent',f);

p = peaks();

imagesc(p,'parent',a1)
colormap(a1,'jet')
colorbar('peer',a1)

imagesc(p,'parent',a2)
colormap(a2,'copper')
colorbar('peer',a2)
