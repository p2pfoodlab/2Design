import svgwrite
import numpy as np


H=100
W=90
D1=7.137/2
D2=5.5/2
x1=12.7
x2=35
x3=55
x4=77.3
lw=0.02

dwg = svgwrite.Drawing(filename='XCplate.svg', profile="full", size=('%dmm'%(W), '%dmm'%(H)), viewBox=('0 0 %d %d'%(W, H)))


circles_big=[[(x1,90), D1], [(x1,50), D1], [(x1,10), D1]]

circles_small=[[(x2,25), D2], [(x2, 50), D2], [(x2, 75), D2], 
                [(x3,25), D2], [(x3, 50), D2], [(x3, 75), D2], 
                [(x4,10), D2], [(x4, 50), D2], [(x4, 90), D2] 
              ]


for c in circles_small:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color="red",width=lw)
   dwg.add(cir)

for c in circles_big:
   cir = dwg.circle(center=c[0], r=c[1]).fill(color=None,opacity=0).stroke(color="red",width=lw)
   dwg.add(cir)

B=dwg.rect(insert=(0,0),size=[W,H],rx=10,ry=10).fill(color=None,opacity=0).stroke(color="blue",width=lw)
dwg.add(B)

dwg.save()
