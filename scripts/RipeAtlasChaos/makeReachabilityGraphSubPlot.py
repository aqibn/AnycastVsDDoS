from matplotlib import pyplot
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('reachability.pdf')

fig = pyplot.figure()

letters = ["A","B","C","E","F","G","H","I","J","K","L","M"]
colors = ["blue","green","red","cyan","magenta","yellow","black","darkgreen","dodgerblue","indianred","mediumseagreen","orange","royalblue","yellowgreen"]
index = 1



ax = pyplot.subplot(1,1,1)
	
for letter in letters:

	timePeriod = []
	xAxis = []
	color = colors[index]
	with open(str(letter)+"reachability.csv", "rt") as f:
			for line in f:
				x = line.split(',')
				timePeriod.append(x[1])
				xAxis.append(int(x[0])/60)


	
	# subplot = "43"+str(index)
	# print subplot
	ax1 = pyplot.subplot(4,3,index)
	index =index + 1
	ax1.plot(xAxis,timePeriod,color=color,label=letter,linewidth="2")
	# plt.plot(xAxis, timePeriod,color=color,label=letter,linewidth="3")
	ax1.axis([0, 7, 0, 10000])
	ax1.legend(loc='lower left')
	pyplot.tight_layout()

	# ax1.savefig(str(letter)+".png")

	# plt.show()
ax.text(0.5, 0.04, 'common xlabel', ha='center', va='center')
ax.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical')
# pyplot.show()
pp.savefig()
pp.close()


# fig = pyplot.figure()
# xData = np.linspace(0, 4*np.pi)
# yData = np.sin(xData)

# # 3 rows, 2 columns, subplot 2 -> 321
# pyplot.subplot("431")
# pyplot.plot(xData, yData)

# # 3 rows, 2 columns, subplot 2 -> 322
# pyplot.subplot("432")
# pyplot.plot(xData, yData)

# # 3 rows, 2 columns, subplot 3 -> 323
# pyplot.subplot("433")
# pyplot.plot(xData, yData)

# etc ...

