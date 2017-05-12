def big_brack(l,h,x1,x2,p,circ=False):
  res="line; 0,0;"
  res+=" %s,%s;"%(l, 0)
  res+=" %s,%s;"%(l, h)
  res+=" %s,%s;"%(0, h)
  res+=" %s,%s;"%(0, 0)
  res+=" close;"
  res+="; circle; %s,%s; %s;"%(l/2+23,h/2.,2)
  res+="; circle; %s,%s; %s;"%(l/2-23,h/2.,2)


  res+="line; %s,0; %s,%s;"%(x1,x1,h)
  res+="line; %s,0; %s,%s;"%(x2,x2,h)

  res+="line; %s,%s;"%(p[0],p[1])
  res+=" %s,%s;"%(p[0]+p[2],p[1])
  res+=" %s,%s;"%(p[0]+p[2],p[1]+p[3])
  res+=" %s,%s;"%(p[0],p[1]+p[3])
  res+=" %s,%s;"%(p[0],p[1])
  res+=" close;"
  """
  res+="; circle; %s,%s; %s;"%(p[0]-2,p[1]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]+p[2]+2,p[1]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]+p[2]+2,p[1]+p[3]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]-2,p[1]-33,1)
  """

  res+="line; %s,%s;"%(l-p[0],p[1])
  res+=" %s,%s;"%(l-(p[0]+p[2]),p[1])
  res+=" %s,%s;"%(l-(p[0]+p[2]),p[1]+p[3])
  res+=" %s,%s;"%(l-p[0],p[1]+p[3])
  res+=" %s,%s;"%(l-p[0],p[1])
  res+=" close;"

  """ 
  res+="; circle; %s,%s; %s;"%(l-(p[0]-2),p[1]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]+p[2]+2,p[1]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]+p[2]+2,p[1]+p[3]+3,1)
  res+="; circle; %s,%s; %s;"%(p[0]-2,p[1]-33,1)
  """

  return res

def small_brack(l,h,sh,c,d,h0=0):
  #res="line; 0,%s;"%h0
  #res="line %s,%s;"%(l, h0)
  res="line; %s,%s;"%(l, h0)
  res+=" %s,%s;"%(l, h+h0)
  res+=" %s,%s;"%(0, h+h0)
  res+=" %s,%s;"%(0, h0)
  #res+=" close;"

  res+="circle; %s,%s; %s;"%(c,h0+h/2.,1.2)
  res+="; circle; %s,%s; %s;"%(l-c,h0+h/2.,1.2)

  res+="circle; %s,%s; %s;"%(c+d,h0+h/2.,1)
  res+="circle; %s,%s; %s;"%(c-d,h0+h/2.,1)

  res+="; circle; %s,%s; %s;"%(l-c-d,h0+h/2.,1)
  res+="; circle; %s,%s; %s;"%(l-c+d,h0+h/2.,1)

  res+="; circle; %s,%s; %s;"%(l/2,h0+h/2.,5)

  res+="line; %s,%s; %s,%s;"%(sh,h0,sh,h+h0)
  res+="line; %s,%s; %s,%s;"%(l-sh,h0,l-sh,h+h0)

  return res


 
l=340
h=30
x1=85
x2=l-x1

res=big_brack(l,h,x1,x2,[15,4,45,21],circ=2.5)
print res

h0=h
l=115+50*2
h=30
sh=45
c=23
d=7.5

res=small_brack(l, h, sh, c, d, h0)
print res


