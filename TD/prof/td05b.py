def polynomenul(l):
  for v in l:
    if v!=0:
      return False
  return True

def degre(p):
  n = len(p)
  for i in range(1,n+1):
    if p[n-i]!=0:
      return n-i
  return 0

def derivee(p):
  n = len(p)
  m = [0] * (n-1)
  for k in range(0,n-1):
    m[k] = p[k+1]*(k+1)
  return m

def derivee(p):
  n = len(p)
  m = []
  for k in range(0,n-1):
    m.append( p[k+1]*(k+1) )
  return m

def somme(p,q):#avec des append
  n,m = len(p),len(q)
  if n < m:
    n1,n2 = n,m
  else:
    n1,n2 = m,n
  l = []
  for k in range(n1):
    l.append(p[k]+q[k])
  if n < m:
    for k in range(n1,n2):
      l.append(q[k])
  else:
    for k in range(n1,n2):
      l.append(p[k])
  return l

def somme(p,q):#en reecrivant ou l'on a deja ecrit
  n,m = len(p),len(q)
  if n>m:
    n1 = n
  else:
    n1 = m
  l = [0]*n1
  for k in range(n):
    l[k] = p[k]
  for k in range(m):
    l[k] = l[k] + q[k]
  return l

#en une seule ecriture
def produit(p,q):#nombre lineaire d'ecritures dans m
  n1 = len(p)
  n2 = len(q)
  m = [0] * (n1+n2-1)
  for k in range(0,n1+n2-1):
    s = 0
    for i in range(max(0,k-n2+1) ,min(k,n1-1)+1 ):
      s = s + p[i]*q[k-i]
    m[k] = s
  return m

#nombre quadratique d'ecritures dans m
def produit(p,q):
  n1 = len(p)
  n2 = len(q)
  m = [0] * (n1+n2-1)
  for i in range(n1):
    for j in range(n2):
      m[i+j] = m[i+j] + p[i]*q[j]
  return m



