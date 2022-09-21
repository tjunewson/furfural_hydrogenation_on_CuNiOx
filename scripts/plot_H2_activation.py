##H2 activation 
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy import interpolate

surfaces = ['Cu(111)','Ni(111)','Cu$_1$Ni$_3$','Cu$_2$Ni$_2$','Cu$_3$Ni$_1$','Cu$_2$O(111)']
IS = list([0]*6)
TS = [0.61,0.19,0.26,0.30,0.39,0.07]
FS = [-0.61,-1.94,-1.51,-1.42,-1.16,-2.00]
energies = np.array([IS,[ts+0.1 for ts in TS],FS]).transpose()

print(energies)


steps= ['H$_2$ (g)','H-H$^{TS}$','2H*']
ns = np.arange(0,3,1)
print(ns)
xx = np.linspace(ns[0],ns[-1],100)
fig, ax = plt.subplots(figsize=(8,6))
colors = cm.Accent(np.linspace(0,1,7))


for i, surf in enumerate(surfaces):
    e = energies[i]
    y = interpolate.pchip_interpolate(ns, e, xx)
    ax.plot(xx, y, label=surfaces[i],color=colors[i])
    ax.plot(ns, e,'o',color=colors[i],markersize=10)

ax.set_xticks(ns)
ax.set_xticklabels(steps)
ax.set_ylim(-2.2,1)
ax.set_ylabel('$\Delta E$ (eV)',fontsize=20)


ax.legend(loc=0,fontsize=20,frameon=False)
ax.tick_params(labelsize=20)
fig.tight_layout()
