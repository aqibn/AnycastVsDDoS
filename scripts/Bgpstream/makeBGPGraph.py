
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
# import numpy as np

fig = pyplot.figure()

letters = ["A","B","C","E","F","G","H","I","J","K","L","M"]
# colors = ["blue","green","red","cyan","magenta","yellow","black","darkgreen","dodgerblue","indianred","mediumseagreen","orange","royalblue","yellowgreen"]
markers = ["o","v","^","<",">","1","2","3","4","s","p","h","d"]
# -                solid line style
#    --               dashed line style
#    -.               dash-dot line style
#    :                dotted line style
#    .                point marker
#    ,                pixel marker
#    o                circle marker
#    v                triangle_down marker
#    ^                triangle_up marker
#    <                triangle_left marker
#    >                triangle_right marker
#    1                tri_down marker
#    2                tri_up marker
#    3                tri_left marker
#    4                tri_right marker
#    s                square marker
#    p                pentagon marker
#    *                star marker
#    h                hexagon1 marker
#    H                hexagon2 marker
#    +                plus marker
#    x                x marker
#    D                diamond marker
#    d                thin_diamond marker
#    |                vline marker
#    _                hline marker
index = 1
timePeriod = []
xAxis = []
# with open("G_bgpAnnoucements_route-views2.csv", "rt") as f:
# 		for line in f:
# 			x = line.split(',')
# 			timePeriod.append(x[1])
# 			xAxis.append(int(x[0])/60)


# plt.xlabel('Hours after 06/25/2016 6:00pm (UTC)', fontsize=18)
# plt.ylabel('BGP Annoucments', fontsize=18)
# plt.plot(xAxis, timePeriod,'ro')
# plt.axis([0, 45, 1, 50])
# plt.legend(loc='upper right')
# plt.savefig("G.png")
# plt.show()
for letter in letters:

	timePeriod = []
	xAxis = []
	# color = colors[index]
	with open(str(letter)+"$_bgpupdates_route-views2_June25th.csv", "rt") as f:
			for line in f:
				x = line.split(',')
				timePeriod.append(x[1])
				xAxis.append(float(x[0])/60)


	
	# subplot = "43"+str(index)
	# print subplot
	# pyplot.subplot(4,3,index)
	pyplot.plot(xAxis,timePeriod,label=letter,marker=markers[index],linewidth="0")
	index =index + 1

	# plt.plot(xAxis, timePeriod,color=color,label=letter,linewidth="3")
	pyplot.axis([0, 10, 1, 150])
	pyplot.legend(loc='upper left')

	# plt.show()
# pyplot.xlabel('Hours after 06/25/2016 6:00pm (UTC)')
# pyplot.ylabel('Number of VPs performing successful queries')	
# pyplot.tight_layout()
pyplot.xlabel('Hours after 06/25/2016 6:00pm (UTC)', fontsize=18)
pyplot.ylabel('BGP Annoucments', fontsize=18)
pyplot.savefig("BGP.png")

# pyplot.show()