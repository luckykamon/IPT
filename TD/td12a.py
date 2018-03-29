''' DU TD11 '''
def somme(p1,p2):
  n1,n2 = len(p1),len(p2)
  maxi = max(n1,n2)
  l = [0] * maxi
  for k in range(n1):
    l[k] = p1[k]
  for k in range(n2):
    l[k] += p2[k]
  return l

def produit(p1,p2):
  n1,n2 = len(p1),len(p2)
  l = [0] * (n1+n2-1)
  for i in range(n1):
    for j in range(n2):
      l[i+j] += p1[i] * p2[j]
  return l

def prod_ext(p,la):
  return [la*v for v in p]

def eval_pol(p,x):
  s = 0
  a = 1
  for k in range(len(p)):
    s += p[k] * a
    a *= x
  return s

def pol_lag(X,Y):
  n = len(X)
  l = [0]
  for i in range(n):
    lag = [1]
    for j in range(n):
      if j!=i:
        q = 1./(X[i]-X[j])
        lag = produit(lag,[-X[j]*q,q])
    l = somme(l, prod_ext(lag,Y[i]) )
  return l

def pol_prim(p):
  return [0]+[p[k]/(k+1.) for k in range(len(p))]

def integ_pol(p,a,b):
  q = pol_prim(p)
  return eval_pol(q,b)-eval_pol(q,a)

'''TD12'''
def quadrature(X):
  n = len(X)
  l = [0]*n
  for i in range(n):
    lag = [1]
    for j in range(n):
      if j!=i:
        q = 1./(X[i]-X[j])
        lag = produit(lag,[-X[j]*q,q])
    l[i] = integ_pol(lag,-1.,1.)
  return l
def integ_cano(f,x,l):
  s = 0
  for k in range(len(x)):
    s += l[k] * f(x[k])
  return s

def integ_quad(f,a,b,x):
  l = quadrature(x)
  f_rond_phi = lambda t: f( (a+b)/2. + (b-a)/2. * t )
  return (b-a) / 2. * integ_cano(f_rond_phi,x,l)

def integ_subd(f,a,b,x,m):
  subd = [a + k * (b-a)*1./m for k in range(m+1)]
  s = 0
  for k in range(m):
    s += integ_quad(f,subd[k],subd[k+1],x)
  return s

#pour calculer l moins souvent

def integ_quad(f,a,b,x,l):
  f_rond_phi = lambda t: f( (a+b)/2. + (b-a)/2. * t )
  return (b-a) / 2. * integ_cano(f_rond_phi,x,l)

def integ_subd(f,a,b,x,m):
  subd = [a + k * (b-a)*1./m for k in range(m+1)]
  l = quadrature(x)
  s = 0
  for k in range(m):
    s += integ_quad(f,subd[k],subd[k+1],x,l)
  return s




