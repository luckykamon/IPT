from random import randint

def additions():
  j=0
  r=0
  n=randint(2,5)
  a,b,c,d,e=0,0,0,0,0
  a=randint(2,10000)
  b=randint(2,10000)
  if n>2:
    c=randint(2,10000)
  if n>3:
    d=randint(2,10000)
  if n>4:
    e=randint(2,10000)
  if n==2:
    print(str(a)+'+'+str(b)+'=')
  if n==3:
    print(str(a)+'+'+str(b)+'+'+str(c)+'=')
  if n==4:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=')
  if n==5:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'+'+str(e)+'=')
  r=input()
  j=a+b+c+d+e
  if r==j:
    return('Oui')
  else:
    print('Non')
    return(str(j))

def soustraction():
  j=0
  r=0
  n=randint(2,5)
  a,b,c,d,e=0,0,0,0,0
  a=randint(2,10000)
  b=randint(2,10000)
  if n>2:
    c=randint(2,10000)
  if n>3:
    d=randint(2,10000)
  if n>4:
    e=randint(2,10000)
  if n==2:
    print(str(a)+'+'+str(b)+'=')
  if n==3:
    print(str(a)+'+'+str(b)+'+'+str(c)+'=')
  if n==4:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'+'+'=')
  if n==5:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'+'+str(e)+'=')
  r=input()
  j=a+b+c+d+e
  if r==j:
    return('oui')
  else:
    return(str(j))
