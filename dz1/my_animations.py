import matplotlib.pyplot as plt
import matplotlib.animation as animation

def anim_initial(function,rule,value):
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_frame_on(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    ax.set_xlim([0,8])
    ax.set_ylim([0,2])

    funpos = (3,0)
    datapos = (1,1)
    radius = 1

    funrect = plt.Rectangle(funpos, 2*radius,2*radius, fc='b', zorder=2)
    funname = ax.annotate(function, xy=(funpos[0]+radius,funpos[1]+radius), color='w', weight='bold', fontsize=24, ha='center', va='center')

    data = plt.Circle(datapos, 0.8*radius, fc='r', zorder=0)
    dataval = ax.annotate(value, xy=data.center, color='w', fontsize=18, ha='center', va='center', zorder=1)

    ax.add_patch(data)
    ax.add_patch(funrect)

    def update(i):
        x,y = data.center
        x = datapos[0] + 0.05*i
        if x==1:
            data.set_color('r')
            dataval.set_text(value)
        data.center = (x, y)
        dataval.set_position((x,y))
        dataval.xy = (x,y)
        if x>funpos[0]+radius:
            data.set_color('g')
            if isinstance(value,list):
                dataval.set_text(rule(*value))
            else:
                dataval.set_text(rule(value))
        return data, dataval

    plt.show()
    return animation.FuncAnimation(fig, update, frames=120, interval=60, blit=True)

def anim_composition():
	fig, ax = plt.subplots(figsize=(9, 5))
	ax.set_frame_on(False)
	ax.axes.get_yaxis().set_visible(False)
	ax.axes.get_xaxis().set_visible(False)
	ax.set_xlim([0,9])
	ax.set_ylim([0,5])

	h1pos = (2,4)
	h2pos = (2,2)
	h3pos = (2,0)
	gpos = (4,0)
	data1pos = (0.5,2.5)
	data2pos = (0.5,2.5)
	data3pos = (0.5,2.5)
	radius = 0.5

	h1rect = plt.Rectangle(h1pos, 2*radius,2*radius, fc='b', zorder=2)
	h1name = ax.annotate("$h_1$", xy=(h1pos[0]+radius,h1pos[1]+radius), color='w', weight='bold', fontsize=24, ha='center', va='center')
	h2rect = plt.Rectangle(h2pos, 2*radius,2*radius, fc='b', zorder=2)
	h2name = ax.annotate("$h_2$", xy=(h2pos[0]+radius,h2pos[1]+radius), color='w', weight='bold', fontsize=24, ha='center', va='center')
	h3rect = plt.Rectangle(h3pos, 2*radius,2*radius, fc='b', zorder=2)
	h3name = ax.annotate("$h_3$", xy=(h3pos[0]+radius,h3pos[1]+radius), color='w', weight='bold', fontsize=24, ha='center', va='center')
	grect = plt.Rectangle(gpos, 4*radius,10*radius, fc='b', zorder=2)
	gname = ax.annotate("$g^3$", xy=(gpos[0]+2*radius,gpos[1]+5*radius), color='w', weight='bold', fontsize=24, ha='center', va='center')

	data1 = plt.Circle(data1pos, 0.8*radius, fc='r', zorder=0)
	data1val = ax.annotate('x', xy=data1.center, color='w', fontsize=12, ha='center', va='center', zorder=1)
	data2 = plt.Circle(data2pos, 0.8*radius, fc='r', zorder=0)
	data2val = ax.annotate('x', xy=data1.center, color='w', fontsize=12, ha='center', va='center', zorder=1)
	data3 = plt.Circle(data3pos, 0.8*radius, fc='r', zorder=0)
	data3val = ax.annotate('x', xy=data1.center, color='w', fontsize=12, ha='center', va='center', zorder=1)

	ax.add_patch(data1)
	ax.add_patch(data2)
	ax.add_patch(data3)
	ax.add_patch(h1rect)
	ax.add_patch(h2rect)
	ax.add_patch(h3rect)
	ax.add_patch(grect)

	def update(i):
		x1,y1 = data1.center
		x2,y2 = data2.center
		x3,y3 = data3.center
		if x1==0.5:
		    data1.set_visible(True)
		    data1.set_color('r')
		    data1val.set_text('x')
		    data2.set_radius(0.8*radius)
		    data2.set_color('r')
		    data2val.set_text('x')
		    data2val.set_fontsize(12)
		    data3.set_visible(True)
		    data3.set_color('r')
		    data3val.set_text('x')
		x1 = data1pos[0] + 0.05*i
		x2 = data2pos[0] + 0.05*i
		x3 = data3pos[0] + 0.05*i
		if x1<h1pos[0]+radius:
		    y1 = data1pos[1] + 0.05*i
		    y3 = data3pos[1] - 0.05*i
		    
		data1.center = (x1, y1)
		data2.center = (x2, y2)
		data3.center = (x3, y3)
		data1val.set_position((x1,y1))
		data1val.xy = (x1,y1)
		data2val.set_position((x2,y2))
		data2val.xy = (x2,y2)
		data3val.set_position((x3,y3))
		data3val.xy = (x3,y3)
		
		if x1>h1pos[0]+radius:
		    data1.set_color('y')
		    data1val.set_text("$h_1(x)$")
		    data2.set_color('y')
		    data2val.set_text("$h_2(x)$")
		    data3.set_color('y')
		    data3val.set_text("$h_3(x)$")
		if x1>gpos[0]+2*radius:
		    data1.set_visible(False)
		    data2.set_color('g')
		    data2.set_radius(1.8*radius)
		    data2val.set_text("$g(h_1(x),h_2(x),h_3(x))$")
		    data2val.set_fontsize(10)
		    data3.set_visible(False)
		    
		return data1, data1val, data2, data2val, data3, data3val

	plt.show()
	return animation.FuncAnimation(fig, update, frames=150, interval=60, blit=True)
