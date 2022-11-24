n = int(input())
num,z =n,0
counts =0
while (n!=0):
    counts +=1
    n//=10
    z+=1
sum,k=0,num
while (num != 0):
    sum += pow(num%10,counts)
    num //=10
if sum == k:
    print("arm")
else:
    print("not arm")        
