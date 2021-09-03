def check(word):
    new=word
    for j in range(len(word)):
        count=word.count(word[j])
        if count>=2: occur=word.find(word[j])
            new=word[:occur+1]+str(count)+word[occur+count:]
    print(new,end=" ")

text=list(map(str,input().split()))
for j in range(len(text)):
    check(text[j])