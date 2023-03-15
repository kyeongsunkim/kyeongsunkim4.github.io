import os, time, sys, math, random, json, requests, csv, subprocess
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scienceplots
import multiprocessing as mp
from scipy import stats
from plotnine import *
from plotnine.data import diamonds
from IPython.display import display
import xlsxwriter
import xmltodict
from plxscripting.easy import*
import plxscripting.easy
from collections import defaultdict
from collections import Mapping
from bs4 import BeautifulSoup
from lxml import objectify
###########################################################################
# data to plot
x = np.linspace(0, 15, 30)
y = np.sin(x) + 0.1*np.random.rand(len(x))
x2 = np.linspace(0, 15, 60)
y2 = np.sin(x2)
###########################################################################
# set plot style
fig = plt.figure(figsize=(8, 5))
ax = plt.axes()
plt.style.use(['science', 'notebook', 'grid'])
###########################################################################
# plot [1]
ax.plot(x, y, '-o', color='black', lw=0.7, ms=5, label='Bucket 1')
ax.plot(x2, y2, '--^', color='red', lw=0.7, ms=5, label='Bucket 2')
# labels
fntsz = 16
ax.set_xlabel('Displacement [m]', fontsize=fntsz)
ax.set_ylabel('Reaction force [kN]', fontsize=fntsz)
ax.set_title('Plot 1', fontsize=fntsz)
# legend
ax.legend(loc='upper right', fancybox=False, edgecolor='black', fontsize=fntsz)
# tick params
ax.tick_params(axis='both', which='both', labelsize=12)
# text
ax.text(0.1, 0.1, 'text', transform=ax.transAxes, ha='center', fontsize=fntsz)
###########################################################################
plt.show()