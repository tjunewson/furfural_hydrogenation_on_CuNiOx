import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(figsize=(8,6))
surfaces = ['Cu(111)','Ni(111)','Cu$_1$Ni$_3$','Cu$_2$Ni$_2$','Cu$_3$Ni$_1$','Cu$_2$O(111)']
c_surf = [3.03,2.07,2.04,2.21,2.38,2.20]
o_surf = [2.34,1.91,1.91,1.91,2.07,1.91]

xx = np.arange(0,6)
ax.scatter(xx, o_surf, s=200, marker = 'x',color='blue',label='O in -CHO')
ax.scatter(xx, c_surf, s=200, marker = 'x',color='red',label='C in furan')

#ax.set_xlim(-0.4,1.2)
ax.set_ylim(1,3.5)
ax.set_xticks(xx)
ax.set_xticklabels(surfaces)
ax.set_ylabel('Bond length $\AA$',fontsize=16)
ax.legend(loc=0,fontsize=16)
ax.tick_params(labelsize=16)
fig.tight_layout()
