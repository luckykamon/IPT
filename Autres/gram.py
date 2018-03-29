from fractions import *

base = [[Fraction(1),Fraction(2),Fraction(3)],[Fraction(4),Fraction(5),Fraction(6)],[Fraction(7),Fraction(8),Fraction(8)]]

vect = []


def scal(base,vect):
  c = len(base)
  scal = 0
  for k in range(c):
    scal+=(Fraction(base[k])*Fraction(vect[k]))
  print scal
  return scal

def mul(a,b):
  mul = []
  for k in range(len(b)):
    mul.append(b[k]*a)
  return mul

def sous(base,c):
  op = []
  d = len(base)
  for t in range(d):
    op.append(base[t]-c[t])
  return op

def add(tab,c):
  op = []
  d = len(base)
  for t in range(d):
    op.append(tab[t]+c[t])
  return op

def div(tab,l):
  for k in range(len(tab)):
    tab[k] = Fraction(tab[k])/Fraction(l)
  return tab

vect.append(base[0])

for k in range(1,len(base)):
  c = [Fraction(0)]*len(base)
  for i in range(k):
    d = Fraction(0)
    for l in vect[i]:
      d += Fraction(l)*Fraction(l)
    s = scal(base[k],vect[i])
    f = mul(s,vect[i])
    c = add(c,div(f,d))
  u = sous(base[k],c)
  vect.append(u)

print vect

