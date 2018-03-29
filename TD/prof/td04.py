def composee(f,g):
  return lambda x: f(g(x))

def suiterecur(a,f,n):
  c = a
  for k in range(n):
    c = f(c)
  return c

def racine_dichot(f,a,b,eps):
  if f(a)*f(b)>0:
    return 'methode non applicable'
  c,d = a,b
  while abs(d-c)>eps:
    m = (c+d)/2.
    if f(m)*f(c)>0:
      c = m
    else:
      d = m
  return c

def recherche_dichot(l,a):
  n =len(l)
  if a<l[0] or a>l[n-1]:
    return False
  i,j = 0,n-1
  while j>i+1 and l[i]!=a and l[j]!=a:
    k = (i+j)//2
    if l[k]<a:
      i = k
    else:
      j = k
  return l[i]==a or l[j]==a

