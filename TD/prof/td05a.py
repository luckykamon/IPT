def polynomenul(p):#avec un for
  for v in p:
    if v != 0:
      return False
  return True
def polynomenul(p):#avec un while
  n = len(p)
  i = 0
  while i<n and p[i] == 0:#ordre d'evaluation
    i = i+1
  return i == n
def degre(p):
  n = len(l)
  for i in range(1,n+1):
    if p[-i] != 0:
      return n-i
  return 0
def degre(p):
  n = len(l)
  for i in range(-1,-n-1,-1):
    if p[i] != 0:
      return n+i
  return 0

def derivee(p):
  n = len(p)
  l = [0]*(n-1)
  for i in range(1,n):
    l[i-1] = p[i]*i
  return l
def derivee(p):
  n = len(p)
  l = []
  for i in range(1,n):
    l.append( p[i]*i )
  return l
     
#python a la fonction max, on definit
def maxi(a,b):
  if a<b:
    return b
  else:
    return a
def mini(a,b):
  if b<a:
    return b
  else:
    return a  
def somme(p,q):#ou l'on veut avoir en un coup l[k] = 
  n1 = mini(len(p),len(q))
  n2 = maxi(len(p),len(q))
  l=[0]*n2
  for k in range(n1):
    l[k] = p[k]+q[k]
  if len(p)<len(q):  
    for k in range(n1,len(p)):
      l[k] = p[k]
  else:
    for k in range(n1,len(q)):
      l[k] = q[k]    
  return l
def somme(p,q):#ou l'on modifie l[k] au fur et a mesure 
  n2 = maxi(len(p),len(q))
  l=[0]*n2 
  for k in range(len(p)):
      l[k] = p[k]
  for k in range(len(q)):
      l[k] = l[k] + q[k]    
  return l 


def produit(p,q):#nombre d'ecritures dans l quadratique
  n,m = len(p),len(q)
  l = [0] * (n+m-1)
  for i in range(n):
    for j in range(m):
      l[i+j] = l[i+j] + p[i]*q[j]
  return l

#en une seule ecriture
def produit(p,q):#nombre lineaire
  n1 = len(p)
  n2 = len(q)
  m = [0] * (n1+n2-1)
  for k in range(0,n1+n2-1):
    s = 0
    for i in range(max(0,k-n2+1) ,min(k,n1-1)+1 ):
      s = s + p[i]*q[k-i]
    m[k] = s
  return m

def maxim(l):#maximum d'une liste
  a = l[0]
  for v in l:
    if v > a:
      a = v
  return a

def degre_c(p):#sans coef nul
  a = p[0][1]
  for v in p:
    if v[1] > a:
      a = v[1]
  return a
def degre_c(p):#avec coef nul eventuel
  a = 0
  for v in p:
    if v[1] > a and v[0]!=0:
      a = v[1]
  return a








