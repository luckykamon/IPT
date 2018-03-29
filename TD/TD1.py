f = lambda x : 2*x+3
def float (x):
  return 2*x+3
def g(x):
  if x>=0:
    return True
  else:
    return False
def positif(x):
  return x>=0
def heavyside(x):
  if x>=0:
    return 1
  else:
    return 0


def critere(a,b,c):
  return a**2+b**2==c**2

def pythagore(a,b,c):
  return critere(a,b,c) or critere(b,c,a) or critere (c,a,b)
  
def eq1(a,b):
  if a==0 and b==0:
    return 'S=R'
  if a==0:
    return 'S=pas de solutions'
  else:
    c=-b*1./a
    return c


def eq2(a,b,c):
  from math import sqrt
  d=b**2-4*a*c
  if d<=0:
    return 'S=Pas de solutions dans R'
  else:
    return (-b-sqrt(d))/(2*a), (-b+sqrt(d))/(2*a)

def somme_entiers(n):
  return (n*(n+1))/2


def somme_impairs(n):
  i=0
  p=1
  for i<=n
    p=p+2
  return p
