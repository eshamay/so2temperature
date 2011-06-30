import sys
import matplotlib.pyplot as plt
from pylab import *
import numpy
import operator
import PlotUtility


new_bins = []
num_bins = 4
for i in range(num_bins):
  for j in range(num_bins):
			new_bins.append(i + 10*j)
new_bins.sort()
print new_bins
width = 0.35

#x_bins = ['Single', 'Double', 'Triple I', 'Triple II', 'Triple']
#cold = [0.12, 8.5, 28.2, 16.4, 44.9]
#hot = [0.2, 4.7, 31, 33.2, 64.3]
x_bins = ['Acyclic', 'Single', 'Double', 'Triple I', 'Triple II']
cold = [46.48, 0.12, 8.5, 28.2, 16.4]
hot = [30.85, 0.2, 4.7, 31, 33.2]


fig = plt.figure(num=1, facecolor='w', edgecolor='w', frameon=True)

plt.bar([i-width/2.0 for i in range(len(x_bins))], cold, width, color='b', align='center')

plt.bar([i+width/2.0 for i in range(len(x_bins))], hot, width, color='r', align='center')

xticks(arange(len(x_bins)), x_bins, fontsize=36)
yticks(fontsize=36)
xlabel('Cyclic Structure Type', fontsize=42)
ylabel('% SO Structure Types', fontsize=42)

plt.show()
