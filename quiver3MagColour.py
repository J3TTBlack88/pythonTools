from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math as m

fig = plt.figure()
ax = fig.gca(projection='3d')

# Data is a list of lists with the entries [x,y,z,theta,beta,gamma,velocity]. Omega is angle to x-axis etc.
data=[[0.5,0.1,0.04,0,90,90,0.15],[0.75,0.1,0.04,0,90,90,0.08],[0.95,0.1,0.04,5,85,30,0.02],
[0.5,0.285,0.04,0,90,90,0.12],[0.75,0.285,0.04,0,90,90,0.06],[0.95,0.285,0.04,0,90,30,0.02],
[0.5,0.52,0.04,0,90,90,0.1],[0.75,0.52,0.04,0,90,90,0.04],[0.95,0.52,0.04,-5,85,30,0.02],
[0.5,0.1,0.3,0,90,85,0.25],[0.75,0.1,0.3,3,87,85,0.15],[0.95,0.1,0.3,7,83,0,0.05],
[0.5,0.285,0.3,0,90,85,0.15],[0.75,0.285,0.3,0,90,85,0.08],[0.95,0.285,0.3,0,90,0,0.04],
[0.5,0.52,0.3,0,90,85,0.1],[0.75,0.52,0.3,-3,87,85,0.06],[0.95,0.52,0.3,-7,83,0,0.06],
[0.5,0.1,0.7,0,90,85,0.08],[0.75,0.1,0.7,5,85,85,0.06],[0.95,0.1,0.7,10,80,-5,0.03],
[0.5,0.285,0.7,0,90,60,0.15],[0.75,0.285,0.7,0,90,60,0.1],[0.95,0.285,0.7,0,90,-5,0.05],
[0.5,0.52,0.7,0,90,60,0.07],[0.75,0.52,0.7,5,85,60,0.05],[0.95,0.52,0.7,-10,80,-5,0.04],
[0.5,0.1,1.1,0,90,85,0.08],[0.75,0.1,1.1,10,80,85,0.06],[0.95,0.1,1.1,30,60,-15,0.03],
[0.5,0.285,1.1,0,90,60,0.06],[0.75,0.285,1.1,0,90,60,0.04],[0.95,0.285,1.1,0,90,-15,0.02],
[0.5,0.52,1.1,0,90,60,0.12],[0.75,0.52,1.1,-10,80,60,0.09],[0.95,0.52,1.1,-30,60,-15,0.04],
[0.5,0.1,1.36,0,90,85,0.08],[0.75,0.1,1.36,15,75,85,0.1],[0.95,0.1,1.36,30,60,-45,0.18],
[0.5,0.285,1.36,0,90,85,0.12],[0.75,0.285,1.36,0,90,85,0.15],[0.95,0.285,1.36,0,90,-45,0.1],
[0.5,0.52,1.36,0,90,85,0.05],[0.75,0.52,1.36,-15,75,85,0.1],[0.95,0.52,1.36,-30,60,-45,0.18],
[0.65,0.285,1.4,90,90,0,0.57],[0.8,0.285,1.4,90,90,0,0.53],[0.95,0.285,1.4,90,90,0,0.57],
[0.8,0.135,1.4,90,90,0,0.6],[0.8,0.435,1.4,90,90,0,0.12],[0.3,0.1,0.1,0,90,90,0.1],
[0.3,0.285,0.1,0,90,90,0.06],[0.3,0.52,0.1,0,90,90,0.05],[0.45,0.1,0.1,0,90,85,0.09],
[0.45,0.285,0.1,0,90,85,0.1],[0.45,0.52,0.1,0,90,85,0.06],[0.6,0.1,0.1,2,88,70,0.13],
[0.6,0.285,0.1,0,90,70,0.15],[0.6,0.52,0.1,-2,88,70,0.11],[0.75,0.1,0.1,5,85,60,0.16],
[0.75,0.285,0.1,0,90,60,0.18],[0.75,0.52,0.1,-5,85,60,0.1],[0.85,0.1,0.7,4,86,60,0.09],
[0.85,0.285,0.7,0,90,60,0.06],[0.85,0.52,0.7,-4,86,60,0.05],[0.55,0.1,0.7,1,89,70,0.07],
[0.55,0.285,0.7,0,90,70,0.05],[0.55,0.52,0.7,-1,89,70,0.04]]

#This colour map suits my needs, it's a cubic progression according to velocity magnitude so that lower steps 
#are differentiated more. My Plot is 0=Green100% and 0.7=Red100%
colors=["#FF0000","#EC1200","#DA2400","#C83600","#B64800",
"#A35B00","#916D00","#7F7F00","#6D9100","#5BA300",
"#48B600","#36C800","#24DA00","#12EC00","#00FF00"]

#Quiver3 doesn't allow a list type colour map, hence the points are plotted individually:
for i in range(0,len(data)):
    #The nest few lines are my 4am direction considerations
    xdir=1
    ydir=1
    zdir=1
    if data[i][3]<0:
        ydir=-1
    elif data[i][4]<0:
        ydir=-1
    elif data[i][5]<0:
        xdir=-1
    u=data[i][6]*np.cos(np.radians(data[i][3]))*xdir
    v=data[i][6]*np.cos(np.radians(data[i][4]))*ydir
    w=data[i][6]*np.cos(np.radians(data[i][5]))*zdir

    #Assignment of colours according to magnitude, according to cubic steps discussed above
    if data[i][6] >= 0.59 and data[i][6] < 0.7 : 
     tone=colors[ 0 ]
    elif data[i][6] >= 0.5 and data[i][6] < 0.59 : 
     tone=colors[ 1 ]
    elif data[i][6] >= 0.42 and data[i][6] < 0.5 : 
     tone=colors[ 2 ]
    elif data[i][6] >= 0.34 and data[i][6] < 0.42 : 
     tone=colors[ 3 ]
    elif data[i][6] >= 0.28 and data[i][6] < 0.34 : 
     tone=colors[ 4 ]
    elif data[i][6] >= 0.23 and data[i][6] < 0.28 : 
     tone=colors[ 5 ]
    elif data[i][6] >= 0.18 and data[i][6] < 0.23 : 
     tone=colors[ 6 ]
    elif data[i][6] >= 0.15 and data[i][6] < 0.18 : 
     tone=colors[ 7 ]
    elif data[i][6] >= 0.11 and data[i][6] < 0.15 : 
     tone=colors[ 8 ]
    elif data[i][6] >= 0.09 and data[i][6] < 0.11 : 
     tone=colors[ 9 ]
    elif data[i][6] >= 0.06 and data[i][6] < 0.09 : 
     tone=colors[ 10 ]
    elif data[i][6] >= 0.04 and data[i][6] < 0.06 : 
     tone=colors[ 11 ]
    elif data[i][6] >= 0.03 and data[i][6] < 0.04 : 
     tone=colors[ 12 ]
    elif data[i][6] >= 0.01 and data[i][6] < 0.03 : 
     tone=colors[ 13 ]
    elif data[i][6] >= 0 and data[i][6] < 0.01 : 
     tone=colors[ 14 ]
    else:
        #Outliers plotted in Blue100% for defference
        tone='#0000FF'
    
    #Actual plotting of coloured arrows
    ax.quiver(data[i][0], data[i][1], data[i][2], u, v, w, length=0.1, color=tone)

#ax.colorbar() TODO - Not supported
ax.set_xlim3d(0,1)
ax.set_ylim3d(0,0.6)
ax.set_zlim3d(0,1.5)
ax.set_xlabel('Front face (m)')
ax.set_ylabel('Side face (m)')
ax.set_zlabel('Height (m)')
plt.show()
