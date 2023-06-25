n = int(input("Enter a number:"))
prime ={2}
for i in range(2,n):
        for j in range(2,i):
            prime.add(i)
            if i%j == 0:
                prime.discard(i)
                break
print(prime)
        
