data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: 
			print(len(data))
print('there are total', len(data), 'datas')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)
	
print('the average length of chat is',sum_len/len(data),)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('there are total', len(new),'chats are less than 100 chareters')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('there are', len(good), 'chats are include "good" word') 
print(good[0])