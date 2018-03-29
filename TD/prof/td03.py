def recur3(n):
  a,b,c = 0,1,3
  for k in range(n):
    a,b,c = b,c,4*c-5*b+2*a
  return a

def sommesimple(n):
  s = 0
  for i in range(1,n+1):
    s = s + (i+3)*(i+3.)/(i+2)
  return s

def sommedouble(n):#code avec somme dans le bon ordre
  s = 0
  for i in range(1,n+1):
    a = 0
    for j in range(1,n+1):
      a = a + (i+j)*(i+j)*1./(i*i+j*j)
    s = s + a
  return s

def sommedouble1(n):#code avec somme dans le bon ordre
  s = 0
  for i in range(1,n+1):
    a = 0
    for j in range(1,n+1):
      a = a + (i+j)*(i+j)*1./(i*i+j*j)
    s = s + a
  return s

"""pour sommedouble1, la phrase
'a la fin de l'etape j, a vaut somme de 1 a j des aik' est un invariant de boucle pour la boucle "for j", 
donc la phrase ' a la fin de l'etape i, s vaut la somme de 1 a i des sommes de 1 a n des alk' est un invariant de boucle pour la boucle "for i" 
""" 

def sommedouble2(n):#code avec un seul compteur
  s = 0
  for i in range(1,n+1):
    for j in range(1,n+1):
      s = s + (i+j)*(i+j)*1./(i*i+j*j)
  return s

def sommeproduit(n):#meme structure que sommedouble1
  s = 0
  for i in range(1,n+1):
    a = 1
    for j in range(1,n+1):
      a = a * (i+j)*(i+j)*1./(i*i+j*j)
    s = s + a
  return s 

def sommetriangulaire1(n):
  s = 0
  for i in range(1,n+1):
    a = 0
    for j in range(i,n+1):
      a = a + ((i+j)**3)*1./(i**3+2*j**3)
    s = s + a
  return s

def sommetriangulaire2(n):
  s = 0
  for j in range(1,n+1):
    a = 0
    for i in range(1,j+1):
      a = a + ((i+j)**3)*1./(i**3+2*j**3)
    s = s + a
  return s
    
    
def tri_selec(l):
  n = len(l)
  for i in range(0,n-1):
    ind = i  
    for j in range(i+1,n):
      if l[j]<l[ind]:
        ind = j
    l[i],l[ind] = l[ind],l[i]
  return l







