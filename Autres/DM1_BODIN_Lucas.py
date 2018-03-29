# Ensemble E et En
E=[0,1,2,3]
n=len(E)
En=[]
for i in range(n):
  En.append(i)



# Question 1
def estPermutation(t):
  if not n==len(t):
    return False
  for k in range(n):
    v=False
    p=0
    while v==False:
      if k==t[p]:
        v=True
      p=p+1
      if p==n and v==False:
        return False
  return True
    
    

# Question 2
def composer(t,u):
  v=[]
  for k in range(n):
    v.append(t[u[k]])
  return v



# Question 3
def inverser(t):
  v=[0]*n
  for k in range(n):
    v[t[k]]=k
  return v



# Question 4
"""Exemple de permutation d'ordre 1: t=[0,1,2,3,4]
Exemple de permutation d'ordre n: t=[1,2,3,4,0]"""



# Question 5
def ordre(t):
  p=1
  v=composer(t,t)
  while t!=v:
    p=p+1
    v=composer(t,v)
  return p



# Question 6
def periode(t,i):
  p=1
  q=ordre(t)
  f=0
  n=1
  v=composer(t,t)
  while t[i]!=i and p!=q:
    v=composer(t,v)
    p=p+1
  if q%p!=0:
    return q
  g=p
  while True:
    if g==q:
      return p
    if v[i]==i:
      g=n*p
      while f!=g:
        v=composer(t,v)
        f=f+1
    if v[i]!=i:
      return q
    n=n+1



# Question 7
def estDansOrbite(t,i,j):
  q=ordre(t)
  v=composer(t,t)
  for k in range(q):
    if v[i]==j:
      return True
    v=composer(t,v)
  return False



# Question 8
def estTransposition(t):
  e=0
  f=-1
  g=-1
  v=[3,2,1,0]
  for k in range(n):
    if t[k]!=v[k] and e>0:
      g=k
      e=e+1
    if t[k]!=v[k] and e==0:
      e=1
      f=k
  if e!=2:
    return False
  if t[f]==v[g] and t[g]==v[f]:
    return True



# Question 9
def estCycle(t):
  for i in range(n):
    v=composer(t,t)
    e=0
    for k in range(ordre(t)):
      if v[k]>1:
        e=e+1
      v=composer(t,v)
    if e!=1:
      return False
  return True



# Question 10
def periodes(t):
  p=[]
  for i in range(n):
    p.append(periode(t,i))
  return p



# Question 11
def itererEfficace(t,k):
  p=periodes(t)
  u=[0]*n
  v=t
  for i in range(n):
    r=k%p[i]
    if r>1:  
      for o in range(r-1):
        v=composer(t,v)
    u[i]=v[i]
  return u



# Question 12
"""Exemple de permutation dont l'ordre excede strictement la taille: t=[5,3,2,6,7,4,1,0]'"""



# Question 13
def pgcd(a,b):
  r=a%b
  while r!=0:
    a,b=b,r
    r=a%b
  return b



# Question 14
def ppcm(a,b):
  return (a*b)/pgcd(a,b)



# Question 15
def ordreEfficace(t):
  p=periodes(t)
  a=p[0]
  q=[a]
  for b in p:
    c=False
    for i in q:
      if b==i:
        c=True
    if c==False:
      q.append(b)
  for j in range(1,len(q)):
    a=ppcm(a,q[j])
  return a
