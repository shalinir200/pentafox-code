import random
text=input()
prefix=random.choice(text)
print(prefix.upper()+text[::-1])