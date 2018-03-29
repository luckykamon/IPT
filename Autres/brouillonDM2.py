def rechercheCaractere(mot,texte):
  n,m=len(mot),len(texte)
  for a in range(n-m+1):
    k=0
    while k<m and mot[k]==texte[a+k]:
      k+=1
    if k==m:
      return True
  return False

def enTeteDeSuffixe(mot,texte,k):
  return mot==texte[k:k+len(mot)]

def rechercherMot (mot,tab):
  m,n=len(mot),len(tab)
  for k in range(n-m+1):
    if enTeteDeSuffixe(mot,tab,k):
      return  True
  return False

def compteroccurences(mot,texte):
  n,m=len(texte),len(mot)
  s=0
  for k in range(n-m+1):
    if enTeteDeSuffixe(mot,texte,k):
      s+=1
  return s

def effectifLettre(texte):
  l=[]
  for v in texte:
    trouve=False
    for k in range(len(l)):
      if l[k][0]==v:
        l[k]=(l[k][0],l[k][1]+1)
        trouve=True
        break
    if not trouve:
      l.append((v,1))
  return l

def effectifBigramme(texte):
  n=len(texte)
  l=[]
  for v in range(len(texte)-1):
    trouve=False
    for k in range(len(l)):
      if l[k][0]==texte[v:v+2]:
        l[k]=(l[k][0],l[k][1]+1)
        trouve=True
        break
    if not trouve:
      l.append((texte[v:v+2],1))
  return l

def calculerSuffixes(texte):
  n=len(texte)
  l=[k for k in range(n)]
  for i in range(n-1):
    ind=i
    for j in range(i,n):
      if texte[l[j]:]<texte[l[ind]:]:
        ind=j
    l[i],l[ind]=l[ind],l[i]
  return l


