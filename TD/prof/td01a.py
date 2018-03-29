toto = 2.3


tata = lambda x : x*x

a = 3+2

def f(x):
  return 2*x+3

f = lambda y: 2*y+3
  
def positif(x): #version maladroite
  if x>=0:
    return True
  else:
    return False

def positif(x): 
  return x>=0

def critere(a,b,c):
  return a**2+b**2==c**2

def pythagore(a,b,c):
  return critere(a,b,c) or critere(c,a,b) or critere(b,c,a)

#commentaire sur une ligne
"""
commentaire sur plusieurs lignes 
par exemple pour du code a ne pas prendre en compte

def fonctionpasencorefinie(arguments):
  if destrucs:
  
"""

from math import sqrt

def eq1(a,b):
  if a == 0:
    if b == 0: 
      return "R tout entier"
    else: 
      return "ensemble vide"
  else: 
    return -b*1./a

def eq2(a,b,c):
  if a == 0:
    return eq1(b,c)
  delta = b*b-4*a*c
  if delta < 0:
    return 'pas de racine reelle'
  if delta == 0:
    return -b/(2.*a)
  return (-b-sqrt(delta))/(2.*a),(-b+sqrt(delta))/(2.*a)






