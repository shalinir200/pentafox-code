li=list(map(int,input().split()))
n=int(input())
pair=[]
for k in range(len(li)):
    for l in range(k+1,len(li)):
        if li[k]+li[l]==n:
            pair.append(li[k])
            pair.append(li[l])
if len(pair)>0:
    print("pair")
else:
    print("No pairs found")