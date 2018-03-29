#Dans les commentaires, il n'y a pas d'accent car ils perturbent le programme

#Question 1
def rechercheSousTexte(mot,texte):
  n=len(texte)
  m=len(mot)
  for k in range(n-m+1):
    if texte[k:k+m]==mot:
      return True
  return False

#Question 2
def rechercheCaractere(mot,texte):
  n=len(texte)
  m=len(mot)
  j=0#compteur de mot
  for k in range(n):
    if mot[j]==texte[k]:
      j+=1
    else:
      j=0
    if j==0 and n-k<=m:#si la 1ere lettre de mot n'est pas trouve et qu'il reste moins de m lettres dans texte alors mot n'est pas dans texte
      return False
    if j==m:
      return True
  return False

#Question 3
#Dans rechercheCaractere, si la 1ere lettre du mot n'est pas dans le texte alors on compare n-m fois 1 caractere. Pour la complexite de rechercheSousTexte elle est beaucoup plus grande car on compare n-m fois m caracteres. D'ou l'avantage de rechercheCaractere qui s'arrete des qu'un des caracteres du mot n'est pas identique.

#Question 4
def enTeteDeSuffixe(mot,texte,k):
  textesuf=texte[k:]
  return rechercheSousTexte(mot,textesuf)

#Question 5
def rechercherMot(mot,texte):
  return enTeteDeSuffixe(mot,texte,0)

#Question 6
def compterOcurrences(mot,texte):
  n=len(texte)
  m=len(mot)
  j=0
  for k in range(n-m+1):
    if texte[k:k+m]==mot:
      j+=1
  return j

#Question 7
def effectifLettre(texte):
  n=len(texte)
  m=0 #compteur permettant de determiner si le caractere est dans la liste l
  l=[(texte[0],0)]
  for k in range(n):
    for j in range(len(l)):
      if texte[k]==l[j][0]:
        m=1
        l[j]=(texte[k],l[j][1]+1)
    if m==0:
      l.append((texte[k],1))
    m=0
  return l

#Question 8
def effectifBigramme(texte):
  n=len(texte)
  m=0 #compteur permettant de determiner si les 2 caracteres sont dans la liste l
  l=[(texte[0]+texte[1],0)]
  for k in range(n-1):
    for j in range(len(l)):
      if texte[k]+texte[k+1]==l[j][0]:
        m=1
        l[j]=(texte[k]+texte[k+1],l[j][1]+1)
    if m==0:
      l.append((texte[k]+texte[k+1],1))
    m=0
  return l

#Question 9
def tri_bulles(l): #on trie la liste en fonction de l'ordre lexicographique
  n=len(l)
  m=[0]*n
  for i in range(n):
    m[i]=l[i]
  for i in range(n-1):
    for j in range(n-i-1):
      if m[j][0]>m[j+1][0]:
        m[j],m[j+1]=m[j+1],m[j]
  return m

def calculerSuffixes(texte):
  n=len(texte)
  listeT=[] #liste de transition a trier
  listeS=[]
  for k in range(n):
    listeT.append((texte[k:],k))
  listeT=tri_bulles(listeT)
  for i in range(n):
    listeS.append(listeT[i][1]) #on attribue a liste S la deuxieme valeur de chaque couple de listeT
  return listeS

#Question 10
def rechercherMot2(mot,texte,listeS):
  n=len(listeS)
  m=len(mot)
  listeT=[]
  for k in range(n):
    listeT.append(texte[listeS[k]:])
  a=0
  b=n-1
  e=-1 #une valeur negative pour ne pas etre egale a d lors de la premiere boucle du while
  if listeT[a][:m]>mot: #permet de ne pas modifier la valeur de a ou b lors de la premiere boucle du while
      c=b
  else:
      c=a
  while True:
    if listeT[a][:m]>mot:
      b=c
    else:
      a=c
    d=(abs(a-b))
    if d==e: #arrete le programme lorsque les valeurs de a et b ne changent pas
        return False
    e=d
    if listeT[a][:m]>mot or listeT[b][:m]<mot:
      return False
    if len(listeT[a])>=m:
      if listeT[a][:m]==mot:
        return True
    if len(listeT[b])>=m:
      if listeT[b][:m]==mot:
        return True
    c=(a+b)//2 #methode de dichotomie

#Question 11
#Dans rechercherMot, on a la meme complexite que rechercheSousTexte d'ou une complexite de n-m+1 fois m caractere avec n la taille du texte, m la taille du mot.
#Pour celle de rechercherMot2, on a n suffixes et en utilisant la methode de dichotomie, dans le pire des cas, on a k comparaisons. Ou quand on parcours les valeurs, on a n=2^k d'ou k=log(n), log en base 2.
#L'interet dans un moteur de recherche internet est de ne rechercher dans les sites que les mots cles des sites appeles ici suffixes pour ainsi eviter de rechercher dans toutes les pages internets qui existent.

#Question 12
def rechercherPremierSuffixe(mot,texte,listeS): #on effectue une dichotomie comme avec le programme precedant
  n=len(listeS)
  m=len(mot)
  listeT=[]
  for k in range(n):
    listeT.append(texte[listeS[k]:])
  a=0
  b=n-1
  e=-1
  f=0
  if listeT[a][:m]>mot:
      c=b
  else:
      c=a
  while f==0:
    if listeT[a][:m]>mot:
      b=c
    else:
      a=c
    d=(abs(a-b))
    if d==e:
        return -1 #a la place de renvoyer False on renvoie -1
    e=d
    if listeT[a][:m]>mot or listeT[b][:m]<mot:
      return -1
    if len(listeT[a])>=m:
      if listeT[a][:m]==mot:
        f=1
    if len(listeT[b])>=m:
      if listeT[b][:m]==mot:
        f=2
    c=(a+b)//2
  if f==2: #la variable a a l'emplacement dans listeT de mot
    a=b
  while listeT[a][:m]==mot: #on recule dans listeT pour avoir le premier suffixe qui contient mot
    a-=1
  return a+1

#Question 13
def compterOcurrences2(mot,texte,listeS):
  r=rechercherPremierSuffixe(mot,texte,listeS)
  if r==-1:
    return "Le mot n'est pas dans le texte"
  else:
    return rechercherDernierSuffixe(mot,texte,listeS)-r

#Question 14
def effectifKgramme(texte,listeS,k):
  listeT=[]
  test=[]
  r=0
  for i in range(len(listeS)):
    if len(texte[listeS[i]:])>=k:
      listeT.append(texte[listeS[i]:])
  for j in range(len(listeT)):
    for m in range(len(test)):
      if test[m][0]==listeT[j][:k]: #si le mot est deja dans la liste, on incremente de 1 l'effectif
          test[m][1]=test[m][1]+1
          r=1
    if r!=1: #sinon on ajoute le mot a la liste
      test.append([listeT[j][:k],1])
    r=0
  return test
