l=[5,3,5,7,3,11,2]
def max(l):
  m=l[0]
  for i in l:
    if i>m:
      m=i
  return m

def moyenne(l):
  n=len(l)
  s=0
  for i in l:
    s=s+i
  s=s*1./n
  return s

def variance(l):
  v=0
  n=len(l)
  m=moyenne(l)
  for i in l:
    v=v+(i-m)**2
  v=v/n
  return v

def tri(l):
  n=len(l)
  m=[0]*n
  for i in range(n):
    m[i]=l[i]
  for i in range(0,n-1):
    for j in range(0,n-i-1):
      if m[j]>m[j+1]:
        m[j],m[j+1]=m[j+1],m[j]
  return m

def mediane(l):
  l=tri(l)
  return l[int((len(l)-1)/2)]

def effectifs(l):
  l=tri(l)
  e=[]
  m=0
  for i in range(l):
    if
