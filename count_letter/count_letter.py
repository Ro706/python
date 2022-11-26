s=list(str(input()))
subtotal=[]
for i in s:
  sub=[]
  for j in s:
    if i == j:
      sub.append(i)
    else:
      continue
  if i not in subtotal:
       subtotal.append(i)
       print(i,"=",len(sub))
  else:
      continue     
  del sub    

      
