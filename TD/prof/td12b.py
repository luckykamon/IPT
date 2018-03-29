def somme (p,q):
  n,m = len(p),len(q)
  mini = min(n,m)
  l1 = [p[k]+q[k] for k in range(mini)]
  l2 = [p[k] for k in range(mini,n)]
  l3 = [q[k] for k in range(mini,m)]
  return l1+l2+l3
def produit(p,q):
  n, m = len(p), len(q)
  l = [0] * (n + m - 1)
  for k in range(n):
    for j in range(m):
      l[k+j] += p[k] * q[j]
  return l
def prod_ext(la,p):
  return [la * v for v in p]
def eval_pol(p,x):
  s = 0
  a = 1
  for k in range(len(p)):
    s += p[k] * a
    a *= x
  return s

def pol_prim(p):
  return [0] + [p[k]/(k+1.) for k in range(len(p))]  

def integ_pol(p,a,b):
  q = pol_prim(p)
  return eval_pol(q,b)-eval_pol(q,a)

def quadrature(x):
  n = len(x)
  lambd = [0] * n
  for k in range(n):
    l = [1]
    for j in range(n):
      if j != k:
        q = 1./(x[k]-x[j])
        l = produit(l, [-x[j] * q, q] )
    lambd[k] = integ_pol(l,-1,1)
  return lambd

def integ_cano(f,x,l):
  s = 0
  for k in range(len(x)):
    s += l[k] * f(x[k])
  return s

def integ_quad(f,a,b,x,l):
  g = lambda x: f( (a+b)/2. + (b-a)/2. * x )
  return (b-a)/2. * integ_cano(g,x,l)

def integ_quad(f,a,b,x,l):
  m = (a+b)/2.
  c = (b-a)/2.
  s = 0
  for k in range(len(x)):
    s += l[k] * f( m + c * x[k] )
  return (b-a)/2. * s

def integ_subd(f,a,b,x,m):
  l = quadrature(x)
  s = 0
  y = [a + k * (b-a)*1./m for k in range(m+1)]
  for k in range(m):
    s += integ_quad(f,y[k],y[k+1],x,l)
  return s





