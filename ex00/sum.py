a = input().split()

k = 0
for i in range(len(a)): 
    a[i] = int(a[i])
    k += a[i]

print (k)

