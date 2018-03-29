def somme(c,a):
  n = len(c)
  s = 0
  for i in range(n):
    if a[i]:
      s = s + c[i]
  return s

def somme(c,a):
  return sum([int(a[i])*c[i] for i in range(len(c)) ])

def estReussie(c,a,Obj):
  return somme(c,a) >= Obj

def estStable(c,a,Obj):
  s = somme(c,a)
  if s < Obj:
    return False
  for k in range(len(a)):
    if a[k] and s-c[k]>=Obj:
      return False
  return True

def AllianceMin(c,Obj):
  n = len(c)
  a = [False]*n
  s = 0
  k = n-1
  while s < Obj and k>=0:
    s = s+ c[k]
    a[k] = True
    k = k - 1
  if s < Obj:
    raise ValueError
  return a


def suivanteDe(a):
  for k in range(len(a)):
    if not a[k]:
      a[k] = True
      return True
    else:
      a[k]=False
  return False      

def binaire(a):
  return sum([int(a[k]) * (2**k) for k in range(len(a))])


def AlliancesStables(c,Obj):
  a = [False]*len(c)
  l = []
  while suivanteDe(a):
    if estStable(c,a,Obj):
      l.append(binaire(a))
  return l












