import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import pandas as pd

# get data from csv file.
df = pd.read_csv(r'C:\Users\Admin\Desktop\pytools\kyeongsunkim.github.io\saved\saved.csv')
###########################################################################
# data to plot
x = df["Ux"].to_numpy()
y = df["Fx"].to_numpy()
x2 = df["Uy"].to_numpy()
y2 = df["Fy"].to_numpy()
x3 = df["Uz"].to_numpy()
y3 = df["Fz"].to_numpy()
###########################################################################
# set plot style
fig = plt.figure(figsize=(8, 5))
ax = plt.axes()
plt.style.use(['science', 'notebook', 'grid'])
###########################################################################
# plot [1]
ax.plot(x, y, '-o', color='black', lw=0.7, ms=5, label='x-dir')
ax.plot(x2, y2, '--^', color='red', lw=0.7, ms=5, label='y-dir')
ax.plot(x3, y3, '--s', color='blue', lw=0.7, ms=5, label='z-dir')
# labels
fntsz = 16
ax.set_xlabel('Displacement [m]', fontsize=fntsz)
ax.set_ylabel('Reaction force [kN]', fontsize=fntsz)
ax.set_title('Load-displacement curve', fontsize=fntsz)
# legend
ax.legend(loc='lower right', fancybox=False, edgecolor='black', fontsize=fntsz)
# tick params
ax.tick_params(axis='both', which='both', labelsize=12)
# text
#ax.text(0.1, 0.1, 'text', transform=ax.transAxes, ha='center', fontsize=fntsz)
###########################################################################
plt.show()

filename = r'C:\Users\Admin\Desktop\pytools\kyeongsunkim.github.io\saved\single_fig.png'
plt.savefig(filename, dpi=450, bbox_inches='tight')
plt.show()
plt.close()