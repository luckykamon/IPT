from random import randint

def creerListeVide(n):
  return [0]+[1]*n

def estDansListe(liste, x):
  for k in liste:
    if k==x:
      return True
  return False

def ajouteDansListe(liste, x):
  if not estDansListe(liste, x):
    liste.append(x)
    liste[0]+=1
  return liste

def plan1():
  return [[5,7],[2,2,3,0,0],[3,1,3,5,0],[4,1,2,4,5],[2,3,5,0,0],[3,2,3,4,0]]

def plan2():
  return [[5,4],[1,2,0,0,0],[3,1,3,4,0],[1,2,0,0,0],[2,2,5,0,0],[1,4,0,0,0]]

def creerPlanSansRoute(n):
  return [[n,0]]+[[0]]*n

def estVoisine(plan,x,y):
  for k in range(1,plan[x][0]+1):
    if plan[x][k] == y:
      return True
  return False

def ajouteRoute(plan,x,y):
  if not estVoisine(plan,x,y):
    plan[0][1]+=1
    plan[x][0]+=1
    plan[x].append(y)
    plan[y][0]+=1
    plan[y].append(x)
  return plan

def afficheToutesLesRoutes(plan):
  r=[]
  for k in range(1,plan[0][0]+1):
    for j in range(1,plan[k][0]+1):
      m=plan[k][j]
      c=True
      for l in r:
        if l==[k,m] or l==[m,k]:
          c=False
      if c:
        r.append([k,m])
  return r

def coloriageAleatoire(plan, couleur, k, s, t):
  for j in range(len(couleur)):
    couleur[j]=randint(1,k)
  couleur[s]=0
  couleur[t]=k+1

def voisinesDeCouleur(plan, couleur, i, c):
  r=[]
  for j in range(len(couleur)):
    if couleur[j]==c:
      if estVoisine(plan,j+1,i):
        c=True
        for k in r:
          if j+1==k:
            c=False
        if c:
          r.append(j+1)
  return r

def voisnesDeLaListeDeCouleur(plan, couleur, liste, c):
  r=[]
  for i in liste:
    t=voisinesDeCouleur(plan, couleur, i, c)
    for h in t:
      m=True
      for y in r:
        if y==h:
          m=False
      if m:
        r.append(h)
  return r
