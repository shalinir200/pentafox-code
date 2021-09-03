message = input(" ")
translation = '' 
x = len(message) - 1
while x >= 0:
   translation = translation + message[x]
   x = x - 1
print(" ", translation)