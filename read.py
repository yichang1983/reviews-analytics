data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1					#count = count +1
		if count % 10000 == 0:		# %是取餘數，意思就是如果count /1000 的餘數等於零，則印出來。
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:						#for loop 的意思就是把清單（data）的東西一個個拿出來，存到 d 裡。
	sum_len = sum_len + len(d)		#運用len 來計算 d 的長度然而把它加到sum_len 裡。

print('留言的平均長度為', sum_len / len(data))		#sum_len 己經計算出總文字的數目在除以 len(data)(留言的筆目，共100萬筆資料)。


new =[]
for d in data:						#for loop 的意思就是把清單（data）的東西一個個拿出來，存到 d 裡。
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留這長度小於100')
print(new[0])
print(new[2])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留這長度提到good')
print(good[0])
print(good[100])
