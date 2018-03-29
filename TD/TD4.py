def f(x):
  return x*x-15

def racine_dichot(f,a,b,eps):
  if f(a)==0:
    return a
  if f(b)==0:
    return b
  if f(a)*f(b)>0:
    return 'pas de solution'
  x=a
  y=b
  while y-x>eps:
    z=(x+y)/2.
    if f(z)==0:
      return z
    if f(x)*f(z)>0:
      x=z
    else:
      y=z
  return x

l=[0,2,4,5,8,11,20,34,36,45,43,101]

def recherche_dichot(l,a):
  n=len(l)
  e=n
  while e>1:
    e=e/2
    if a==l[n-1]:
      return True
    if a<l[n-1]:
      n=n-e
    if a>l[n-1]:
      n=n+e
    e=e/2
  return False
