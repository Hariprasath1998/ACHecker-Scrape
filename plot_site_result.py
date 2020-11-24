#Script to plot graph

import matplotlib.pyplot as plt
import pandas as pd

column_names = ['Sites','Tested','Known','Likely','Potential']
df = pd.read_csv("Last.csv", names=column_names)
filt=(df['Tested']=='Y')

Sites=df[filt].Sites.to_list()
Known=df[filt].Known.astype(int).to_list()
Likely=df[filt].Likely.astype(int).to_list()
Potential=df[filt].Potential.astype(int).to_list()
width= 0.45

fig, ax = plt.subplots()

ax.bar(Sites, Known, width, bottom=Potential, label='Known')
ax.bar(Sites, Likely, width, bottom=Known, label='Likely')
ax.bar(Sites, Potential, width, label='Potential')

ax.set_xlabel('Sites')
ax.set_ylabel('Number of errors')
ax.set_title('Graph')
ax.legend()
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) #

plt.savefig('Site_Graph.svg')
plt.show()
