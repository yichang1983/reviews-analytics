data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1					#count = count +1
		if count % 10000 == 0:		# %是取餘數，意思就是如果count /1000 的餘數等於零，則印出來。
			print(len(data))
print(len(data))

print(data[0])
print('----------------')
print(data[1])