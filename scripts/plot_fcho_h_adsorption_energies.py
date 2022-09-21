import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(figsize=(8,6))
surfaces = ['Cu(111)','Ni(111)','Cu$_3$Ni$_1$','Cu$_2$Ni$_2$','Cu$_1$Ni$_3$','Cu$_2$O(111)']
efur = [-0.91,-1.88,-1.18,-1.81,-1.99,-1.65]
eh = [-0.31,-0.97,-0.58,-0.71,-0.75,-1.00]

xx = np.arange(0,6)
ax.scatter(xx, efur, s=200, marker = 'x',color='blue',label='FCHO*')
ax.scatter(xx, eh, s=200, marker = 'x',color='red',label='H*')

#ax.set_xlim(-0.4,1.2)
ax.set_ylim(-3,0)
ax.set_xticks(xx)
ax.set_xticklabels(surfaces)
ax.set_ylabel('$\Delta E$ (eV)',fontsize=16)
ax.legend(loc=0,fontsize=16)
ax.tick_params(labelsize=16)
fig.tight_layout()
