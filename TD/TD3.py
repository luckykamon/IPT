def recur3(n):
  a,b,c = 0,1,3
  for k in range (n):
    a,b,c = b,c,(4*c-5*b+2*a)
  return a


def sommesimple(n):
  a=0
  for i in range (1,n+1):
    a=((i+3)*(i+3))/(i+2)+a
  return a


def sommedouble(n):
  a=0
  b=0
  for i in range (1,n+1):
    for j in range (1,n+1):
      a=a+((i+j)*(i+j))/(i*i+j*j)
    b=b+a
  return b


def sommeproduit(n):
  a=1
  b=0
  for i in range (1,n+1):
    for j in range (1,n+1):
      a=a*(((i+j)**2)/(i**2+j**2))
    b=b+a
  return b

def sommetriangulaire(n):
  s=0
  for i in range (1,n+1):
    a=0
    for j in range (i,n+1):
      a=a+(i+j)**3*1./(i**3+2*j**3)
    s=a+s
  return s

def sommetriangulaire2(n):
  s=0
  for j in range (1,n+1):
    a=0
    for i in range (1,j+1):
      a=a+(i+j)**3*1./(i**3+2*j**3)
    s=a+s
  return s


l=[1,3,2,5]
def tri_selec(l):
  n=len(l)
  for j in range (n):
    for i in range (n):
      m=l[j]
      e=j
      if l[i]<m:
        m=l[i]
        e=i
    l[j],l[e]=l[e],l[j]
  return l

def tri_selec(l)
  n= len(l)
  for i in range(0,n-1):
    ind=i
    for j in range(i+1,n)
      if l[j]<l[ind]:
        ind=j
    l[i],l[ind]=l[ind],l[i]
  return l








  
    

