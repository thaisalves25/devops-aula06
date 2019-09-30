num = int(input())
primos = []
for i in range (num-num,num+num):
    if i % 2 !=0:
        primos.append(i)
        i + = 1
print (primos)
