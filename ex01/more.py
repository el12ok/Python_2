a = input().split()
b = a 
a = set(a)
for i in a:
    if b.count(i) > 1:
        print (i,end = " ")
print()
