# -*- coding: utf-8 -*-
fichier = open("essai.txt","rwa+")

def imprime1(fichier):
  for k in fichier.readlines():
    print k

def imprime2(fichier):
  print fichier.read()

def test1():
  fichier = open("essai.txt", "rw+")
  fichier.writelines(["test"])
  fichier.close()

def seek():
  fo = open("essai.txt","arw+")
  seq = "qukl45suhi"
  fo.writelines( seq )
  #fo.seek(0,0)
  #for index in range(7):
  # line = fo.next()
  # print "Line No %d - %s" % (index, line)



def test2():
  # Open a file in witre mode
  fo = open("essai.txt", "ra+")
  fo.seek(5,0)
  fo.write("abc")
  fichier.close()

def remplace(a,b,c):
  fichier = open("essai.txt","rwa+")
  l = fichier.readlines()
  n = len(b)
  for k in range(len(l)):
     for j in range(len(l[k])-n):
       if l[k][j:j+n] == b:
         l[k] = l[k][:j]+c+l[k][j+n:]
  s = ""
  for v in l:
     s += v
  fo = open("essai.txt", 'w')
  fo.write(s)
  fo.close()

def csv_to_list(nom,sepligne,sepcolonne):
  f = open(nom,'r')
  string = f.read()
  l1 = string.split(sepligne) #les \n
  for k in range(len(l1)):
    l1[k] = l1[k].split(sepcolonne) #les ","
  return l1



