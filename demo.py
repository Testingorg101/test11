a = 11
# If given is greater than 1
if a > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(a/2)+1):
		 
		# 2 and n / 2, it 
		if (a % i) == 0:
			print(a, "")
			break
	else:
		print(a, "")
else:
	print(a, "")
