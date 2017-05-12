def top(l,circ=False,dy=6):
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
 
def sideA(h, dy=6, x0=False, wh=False):
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
    res+="close"
  return res

def sideB(h, dy=6, x0=False, wh=False):
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
    res+="close"
  return res

t=top(110,circ=4,dy=6)
print t

h=70
w=30
dy=w/5

sA=sideA(h, dy, x0=False, wh=False)

wh=[13,24]
x0=[(w-wh[0])/2., h-20-wh[1]]
sA=sideA(h, dy, x0, wh)
print "A"
print sA

sB=sideB(h, dy, x0, wh)
print "B"
print sB


