def imprime1(fichier):
  for l in fichier.readlines():
    print l
def imprime2(fichier):
  for l in fichier:
    print l
def ecrire_a_la_suite(nom,texte):
  f = open(nom,'a')
  f.write(texte)
  f.close()
  f = open(nom,'r')
  return f.read()

def ecrire_abc(nom):
  f = open(nom,'w')
  f.write('abc')
  f.close()

def remplace(nom,texte1,texte2):
  f = open(nom,'r')
  l = f.readlines()
  n1 = len(texte1)
  for i in range(len(l)):
    for k in range(len(l[i])-n1):
      if l[i][k:k+n1] == texte1:
        l[i] = l[i][:k]+texte2+l[i][k+n1:]
  string = ''
  for v in l:
    string += v
  f = open(nom, 'w')
  f.write(string)
  f.close()

def csv_to_list(nom,sepligne,sepcolonne):
  f = open(nom,'r')
  string = f.read()
  l1 = string.split(sepligne)
  for k in range(len(l1)):
    l1[k] = l1[k].split(sepcolonne)
  return l1




