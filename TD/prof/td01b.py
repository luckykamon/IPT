# -*- coding: utf-8 -*-

a = 1
if a==1:
  3
#commentaire sur une ligne

"""
commentaires
sur plusieurs lignes


éé

"""

def f(x):
  return 2*x+3
f = lambda x:2*x+3

def positif(x):#maladroit
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

def cr(a,b,c):
  return a*a+b*b==c*c

def pythagore(a,b,c):
  return cr(a,b,c) or cr(b,c,a) or cr(c,a,b)

def eq1(a,b):
  if a != 0:
    return -b*1./a
  else:
    if b != 0:
      return 'ensemble vide'
    else:
      return 'droite reelle'

def eq1(a,b):#raccourci du fait des return
  if a != 0:
    return -b*1./a
  if b != 0:
    return 'ensemble vide'
  return 'droite reelle'

'toto dit "bonjour"'

"tata dit 'au revoir'"


from math import sqrt

def eq2(a,b,c):
  if a == 0:
    return eq1(b,c)
  delta = b*b-4*a*c
  if delta < 0:
    return 'ensemble vide'
  if delta == 0:
    return -b/(2.*a)
  de = sqrt(delta)
  return (-b-de)/2.*a),(-b+de)/(2.*a)


if bool1:
  instruc1
  if bool2:
    instruc2
  elif:
  












  
  

  
















