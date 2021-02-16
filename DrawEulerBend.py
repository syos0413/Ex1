import pya
import numpy as np
layout = pya.Layout()
# database unit 1nm:
layout.dbu = 0.001

# Create Cell obj
layout1 = layout.create_cell("Euler90Bend")


# Create layer #'s
setLayer1= layout.layer(1, 0) 

# draw Euler bend 
wgw=1 # waveguide width in um
Rmin=10 # minimum radius in um

#Number of points
N=int(1/0.001)
T=np.sqrt(np.pi/2)
dt=T/N
dx=0
dy=0
bendPath=[]
prev_x=0
prev_y=0
t=0
for ii in range(0,N):
    dx=np.cos(t*t)*dt
    dy=np.sin(t*t)*dt
    t=t+dt
    x=prev_x+dx
    y=prev_y+dy
    bendPath.append(pya.DPoint(x,y))
    prev_x=x
    prev_y=y

scale=Rmin/y # scale for minimum radius
bendPath=[item*scale for item in bendPath] # update path points             

dpath = pya.DPath(bendPath, wgw) # create path of width 
outline = layout1.shapes(setLayer1).insert(dpath) # generate layout


# Export GDS
layout.write("EulerBend.gds") 

print("Done.")


