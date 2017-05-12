def top_asym(l,circ=False,dy=6):
  res="line; 0,0;"
  g=[0,1,1,2]
  for k in range(0,2):
    i=2*k
    res+=" %s,%s;"%(l-5,dy*i) 
    res+=" %s,%s;"%(l-5,dy*(i+1)) 
    res+=" %s,%s;"%(l,dy*(i+1)) 
    res+=" %s,%s;"%(l,dy*(i+2)) 
  res+=" %s,%s;"%(l-5,dy*4) 
  res+=" %s,%s;"%(l-5,dy*5) 

  for k in range(2):
    i=2*k
    res+=" %s,%s;"%(0,dy*(5-i)) 
    res+=" %s,%s;"%(0,dy*(5-i-1)) 
    res+=" %s,%s;"%(5,dy*(5-i-1)) 
    res+=" %s,%s;"%(5,dy*(5-i-2)) 
  res+=" %s,%s;"%(0,dy*1) 
  res+=" %s,%s;"%(0,0) 
  res+=" close"
  if circ: res+="; circle; %s,%s; %s;"%(l/2,5*dy/2.,circ)
  return res
 
def top_sym(l,circ=False,dy=6):
  res="line; 5,0;"
  g=[0,1,1,2]
  for k in range(0,2):
    i=2*k
    res+=" %s,%s;"%(l-5,dy*i) 
    res+=" %s,%s;"%(l-5,dy*(i+1)) 
    res+=" %s,%s;"%(l,dy*(i+1)) 
    res+=" %s,%s;"%(l,dy*(i+2)) 
  res+=" %s,%s;"%(l-5,dy*4) 
  res+=" %s,%s;"%(l-5,dy*5) 

  for k in range(2):
    i=2*k
    res+=" %s,%s;"%(5,dy*(5-i)) 
    res+=" %s,%s;"%(5,dy*(5-i-1)) 
    res+=" %s,%s;"%(0,dy*(5-i-1)) 
    res+=" %s,%s;"%(0,dy*(5-i-2)) 
  res+=" %s,%s;"%(5,dy*1) 
  res+=" %s,%s;"%(5,0) 
  res+=" close;"
  if circ: 
     for c in circ: res+="; circle; %s,%s; %s;"%(c[0],c[1],c[2])
  return res

def sideA(h, dy=6, x0=False, wh=False, circ=0):
  w=dy*5 
  #res="line; 0,0; %s,0; %s,%s;"%(w,w,h)
  res="line; 0,0; %s,0;"%(w)
  for k in range(2):
    i=2*k
    res+=" %s,%s;"%(dy*(5-i),h) 
    res+=" %s,%s;"%(dy*(5-i-1),h) 
    res+=" %s,%s;"%(dy*(5-i-1),h-5) 
    res+=" %s,%s;"%(dy*(5-i-2),h-5)
  res+=" %s,%s;"%(dy,h) 
  res+=" %s,%s;"%(0,h) 
  res+="close;"
  if x0:
    res+="line; %s,%s;"%(x0[0],x0[1]) 
    res+="%s,%s;"%(x0[0]+wh[0],x0[1]) 
    res+="%s,%s;"%(x0[0]+wh[0],x0[1]+wh[1]) 
    res+="%s,%s;"%(x0[0],x0[1]+wh[1]) 
    res+="close;"
  if circ: 
     for c in circ: res+="; circle; %s,%s; %s;"%(c[0],c[1],c[2])
  return res

def sideB(h, dy=6, x0=False, wh=False, circ=0):
  w=dy*5 
  #res="line; 0,0; %s,0; %s,%s;"%(w,w,h)
  res="line; 0,0; %s,0;"%(w)
  for k in range(2):
    i=2*k
    res+=" %s,%s;"%(dy*(5-i),h-5) 
    res+=" %s,%s;"%(dy*(5-i-1),h-5) 
    res+=" %s,%s;"%(dy*(5-i-1),h) 
    res+=" %s,%s;"%(dy*(5-i-2),h)
  res+=" %s,%s;"%(dy,h-5) 
  res+=" %s,%s;"%(0,h-5) 
  res+="close;"
  if x0:
    res+="line; %s,%s;"%(x0[0],x0[1]) 
    res+="%s,%s;"%(x0[0]+wh[0],x0[1]) 
    res+="%s,%s;"%(x0[0]+wh[0],x0[1]+wh[1]) 
    res+="%s,%s;"%(x0[0],x0[1]+wh[1]) 
    res+="close;"
  if circ:
     for c in circ: res+="; circle; %s,%s; %s;"%(c[0],c[1],c[2])
  return res


w=30
dy=w/5

#Top In
l_int=120
t_int=top_sym(l_int,[[l_int/2,w/2.,4]],dy)
#print "Top In"
print t_int

#Top Out 
#BIG 
l_out=l_int+50
t_out=top_sym(l_out, [[l_out/2.-2.375,w/2.,2.5],[l_out/2.+2.375,w/2.,2.5]],dy)
#print "Top Out"
print t_out

#BIG (config2 35)
l_out=l_int+35
t_out=top_sym(l_out,[[l_out/2.-2.375,w/2.,2.5],[l_out/2.+2.375,w/2.,2.5]],dy)
#print "Top Out"
print t_out


#Top Out 
#SMALL 
l_out=l_int+44
t_out=top_sym(l_out,[[l_out/2.-2.375,w/2.,2.5],[l_out/2.+2.375,w/2.,2.5]],dy)
#print "Top Out"
print t_out

#SMALL (config2)
l_out=l_int+2.9
t_out=top_sym(l_out,[[l_out/2.-2.375,w/2.,2.5],[l_out/2.+2.375,w/2.,2.5]],dy)
#print "Top Out"
print t_out

#sides-In 
x0=0
wh=0

h=48
w=30
dy=w/5

cs=[[w/2,h-28,1], [w/2-8,h-28,.5], [w/2+8,h-28,.5], [w/2,h-28-8,.5], [w/2,h-28+8,.5]]

sA=sideA(h, dy, x0, wh, cs)
#sB=sideB(h, dy, x0, wh, 1)
#print "sides-In"
#print "In A"
print sA
#print "B"
#print sB

#sides-Out BIG
h=70
w=30
dy=w/5

wh=[21,42]
#x0=[(w-wh[0])/2., h-27-wh[1]]
x0=[(w-wh[0])/2., h-17-wh[1]]


sA=sideA(h, dy, x0, wh, 0)
#sB=sideB(h, dy, x0, wh, 0)
#print "sides-Out"
#print "A"
print sA
#print "B"
#print sB

#sides-Out SMALL

h=61
w=30
dy=w/5

wh=[12,24]
x0=[(w-wh[0])/2., h-27-wh[1]]


sA=sideA(h, dy, x0, wh, 0)
sB=sideB(h, dy, x0, wh, 0)
#print "sides-Out"
#print "A"
print sA
#print "B"
#print sB

