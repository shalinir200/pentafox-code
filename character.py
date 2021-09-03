def printwrd(s) :
	j = 0
	while( j < len(s) - 1) :
		count = +1
		while s[j] == s[j + 1] :
			j += 1
			count += 1
			if j + 1 == len(s):
				break
		print(str(s[j]) + str(count),end = " ")
		j += 1
	print()
if _name_ == "_main_" :
	printwrd("All is well")