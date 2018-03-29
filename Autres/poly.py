def tri(t):
  n= len (t)
  c=0
  for i in range(n):
   j = i
   for k in range(i,n):
     if t[k]<t[j]: j = k
   if i!=j:
     c+=1
     print j
     t[i],t[j] = t[j],t[i]
     print t
  return c
