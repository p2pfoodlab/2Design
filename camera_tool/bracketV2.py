import svgwrite
import numpy as np

def mkArc(dwg, p0, p1, radius):
   args = {'x0':p0[0], 
        'y0':p0[1], 
        'xradius':radius, 
        'yradius':radius, 
        'ellipseRotation':0, #has no effect for circles
        'x1':(p1[0]-p0[0]), 
        'y1':(p1[1]-p0[1])}

   p=dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,0 %(x1)f,%(y1)f"%args,
             fill="none", 
             stroke='red', stroke_width=lw
            )
   dwg.add(p)
   return p

big=1
sk_col="black"
Ri=17.8
Re=26
Mvisx=21
r=.3*Ri
L=280+big*20
W=55
lw=.02
M3=1.5
M4=2

y_center=W/2.
C1_x=Re+r

B_x=60+big*10
B_s=[47,51]

dwg = svgwrite.Drawing(filename='br_big.svg', profile="full", size=('%dmm'%(L), '%dmm'%(2*W)), viewBox=('0 0 %d %d'%(L, 2*W)))


rects=[[(0,y_center-Ri), (L,2*Ri)],
       [(B_x,y_center-B_s[1]/2.),B_s], [(L-B_x-B_s[0],y_center-B_s[1]/2.), B_s]]

circles_sk=[[(Re+r,y_center), Re], [(L-(Re+r),y_center), Re], 
            [(C1_x,y_center), Ri], [(L-C1_x,y_center), Ri] , 
            [(r,y_center), r], [(L-r,y_center), r]]

circles_holes=[[(Re+r-Mvisx,y_center), M3], [(L-(Re+r-Mvisx), y_center), M3], 
               [(Re+r+Mvisx,y_center), M3], [(L-(Re+r+Mvisx), y_center), M3],
               [(Re+r,y_center-Ri), M4], [(L-(Re+r),y_center-Ri), M4],
               [(rects[1][0][0]+2.5, rects[2][0][1]+2.5), M3], 
               [(rects[1][0][0]+rects[2][1][0]-2.5, rects[2][0][1]+2.5), M3],
               [(rects[1][0][0]+.5*rects[2][1][0]-2.5, rects[2][0][1]+2.5), M3],
               [(rects[1][0][0]+.5*rects[2][1][0]+2.5, rects[2][0][1]+2.5), M3],
               
               [(rects[1][0][0]+2.5, rects[1][0][1]+rects[2][1][1]-2.5), M3], 
               [(rects[1][0][0]+rects[2][1][0]-2.5, rects[2][0][1]+rects[1][1][1]-2.5), M3],
               [(rects[1][0][0]+.5*rects[2][1][0]-2.5, rects[2][0][1]+rects[1][1][1]-2.5), M3],
               [(rects[1][0][0]+.5*rects[2][1][0]+2.5, rects[2][0][1]+rects[1][1][1]-2.5), M3],

               [(rects[2][0][0]+2.5, rects[2][0][1]+2.5), M3], 
               [(rects[2][0][0]+rects[2][1][0]-2.5, rects[2][0][1]+2.5), M3],
               [(rects[2][0][0]+.5*rects[2][1][0]-2.5, rects[2][0][1]+2.5), M3],
               [(rects[2][0][0]+.5*rects[2][1][0]+2.5, rects[2][0][1]+2.5), M3],

               [(rects[2][0][0]+2.5, rects[2][0][1]+rects[2][1][1]-2.5), M3], 
               [(rects[2][0][0]+rects[2][1][0]-2.5, rects[2][0][1]+rects[2][1][1]-2.5), M3],
               [(rects[2][0][0]+.5*rects[2][1][0]-2.5, rects[2][0][1]+rects[2][1][1]-2.5), M3],
               [(rects[2][0][0]+.5*rects[2][1][0]+2.5, rects[2][0][1]+rects[2][1][1]-2.5), M3],
               

               [(L/2., W/2.), Ri],
               [(L/2.-16, W/2.-14), M3],
               [(L/2.+16, W/2.+14), M3],
               [(L/2.-18.5, W/2.+14), M4],
               [(L/2.+18.5, W/2.-14), M4]
              ]

"""
               [(.5*(rects[1][0][0]+rects[1][0][0])-2.5), rects[2][0][1]+2.5), M3], 
               [(.5*(rects[1][0][0]+rects[1][0][0])+2.5), rects[2][0][1]+2.5), M3], 
               [(L-.5*(rects[1][0][0]+rects[1][0][0])-2.5), rects[2][0][1]+2.5), M3], 
               [(L-.5*(rects[1][0][0]+rects[1][0][0])+2.5), rects[2][0][1]+2.5), M3], 

               [(.5*(rects[1][0][0]+rects[1][0][0])-2.5), rects[2][1][1]-2.5), M3], 
               [(.5*(rects[1][0][0]+rects[1][0][0])+2.5), rects[2][1][1]-2.5), M3], 
               [(L-.5*(rects[1][0][0]+rects[1][0][0])-2.5), rects[2][1][1]-2.5), M3], 
               [(L-.5*(rects[1][0][0]+rects[1][0][0])+2.5), rects[2][1][1]-2.5), M3], 
"""


l1=dwg.line(start=(B_x,W/2.-Ri),end=(B_x,W/2.+Ri)).stroke(color="black",width=lw)
l2=dwg.line(start=(L-B_x,W/2.-Ri),end=(L-B_x,W/2.+Ri)).stroke(color="black",width=lw)

dwg.add(l1)
dwg.add(l2)

#Im=svgwrite.image.Image(href="salade.png",insert=(B_x+5,y_center-20) )
#dwg.add(Im)
"""
for ri in rects:
   B=dwg.rect(insert=ri[0],size=ri[1]).fill(color=None,opacity=0).stroke(color=sk_col,width=lw)
   dwg.add(B)

for c in circles_sk:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color=sk_col,width=lw)
   dwg.add(cir)
"""

for c in circles_holes:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color="red",width=lw)
   dwg.add(cir)

for c in circles_sk[2:4]:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color="red",width=lw)
   dwg.add(cir)


p0=[0,W/2.]
radius=r
#mkArc(dwg, p0, p1, radius)

start=p0
s1 = 'M {0[0]} {0[1]}'.format(start)
p1 = dwg.path(d=s1, stroke_width=lw, stroke='blue', fill='none')
p1.push_arc([r,W/2.+r], 0, r, large_arc=False, angle_dir='-',absolute=True)
p1.push('C', [2*r, W/2.+r, r, W/2.+Re, Re+r, W/2.+Re])
p1.push('C', [2*Re+r, W/2.+Re, r+Ri+Re, W/2.+Ri, 2*Re+r, W/2.+Ri])
p1.push('C', [B_x, W/2.+Ri, B_x, W/2.+Ri, B_x, y_center+B_s[1]/2.-2.5])
p1.push('C', [B_x, y_center+B_s[1]/2., B_x, y_center+B_s[1]/2., B_x+2.5, y_center+B_s[1]/2.])
p1.push('L', [B_x+B_s[0]-2.5, y_center+B_s[1]/2.])
p1.push('C', [B_x+B_s[0], y_center+B_s[1]/2., B_x+B_s[0], y_center+B_s[1]/2., B_x+B_s[0], y_center+B_s[1]/2.-2.5])
p1.push('C', [B_x+B_s[0], W/2.+Ri, B_x+B_s[0], W/2.+Re, L/2., W/2.+Re])
dwg.add(p1)

dwg.add(dwg.image(href="salade.png", insert=(B_x+B_s[0]/4., W/2.-Ri), size=("%dmm"%(Ri/2.), "%dmm"%(Ri/2.)))) 
dwg.add(dwg.image(href="salade.png", insert=(L-(B_x+3*B_s[0]/4.), W/2.-Ri), size=("%dmm"%(Ri/2.), "%dmm"%(Ri/2.)))) 


p2=p1.copy()
p2.scale(1,-1)
p2.translate(0,-W)
dwg.add(p2)

p3=p1.copy()
p3.scale(-1,1)
p3.translate(-L,0)
dwg.add(p3)

p4=p1.copy()
p4.scale(-1,-1)
p4.translate(-L,-W)
dwg.add(p4)

######################
L2=210
xLs=45
cx=23
d=7.5
W2=30.

B=dwg.rect(insert=(0,W),size=[L2,W2],rx=10,ry=10).fill(color=None,opacity=0).stroke(color="blue",width=lw)
dwg.add(B)
l1=dwg.line(start=(xLs,W),end=(xLs,W2+W)).stroke(color="black",width=lw)
l2=dwg.line(start=(L2-xLs,W),end=(L2-xLs,W2+W)).stroke(color="black",width=lw)

dwg.add(l1)
dwg.add(l2)

circles_holes=[[(cx,W+W2/2), M4], [(L2-cx,W+W2/2), M4], 
               [(cx-d,W+W2/2), M3], [(cx+d,W+W2/2), M3], 
               [(L2-cx-d,W+W2/2), M3], [(L2-cx+d,W+W2/2), M3],
               [(L2/2.,W+W2/2), 5]
              ]     

for c in circles_holes:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color="red",width=lw)
   dwg.add(cir)


#dwg.add(Ra)
dwg.save()
