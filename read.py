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


#進階寫法(清單快寫法：影片 057)
good = [d for d in data if 'good' in d]			#等於29-31行的合併，而剛開始的d 就是good.append(d).
print('一共有', len(good), '筆留這長度提到good')
print(good[0])
print(good[100])


#文字計數

word_count = {}				#建立一個字典

for d in data:				#從1百萬筆清單(data)中 讀取，然而每一筆存成 d
	words = d.split(' ')	# d.split(' ') , 的意思是指在這一筆的字串（整篇文章它算是一筆字串）中，如果有空格就切一刀，讓每個單字變成一個字串。
	for word in words:		# words 是（第上面一行（18行））清單，裡面裝著很多字串，然而從這個清單（words）中讀取，然而每一個字存成word.
		if word in word_count:		#如果這個字(word)有出現在字典（word_count）裡。
			word_count[word] += 1	#把目前的次數加1
		else:						#如果沒有出現過
			word_count[word] = 1	#把它新增進字典（word_count），然而它的次數是1。

for word in word_count:				#從字典（word_count）裡讀取，每一個key,然而存成word.
	if word_count[word] > 1000000:
		print(word, word_count[word])	#印出key(word), 也印出查找出來的次數也印出來(world_count[word])


print(len(word_count))
print(word_count['Thomas'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in word_count:
		print(word,'出現過的次數為：', word_count[word])
	else:
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能')

