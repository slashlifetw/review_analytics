
data = []
count = 0
total_num = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1 # count = count + 1
        if count % 1000 == 0: #假設count目前是1001去除1000餘數等於1，不等於0，所以不會印出來
            print(len(data))
        total_num = total_num + len(line)
        print(total_num)
print('檔案讀取完畢，總共有', len(data), '筆資料')

new = []
for every_commit in data:
    if len(every_commit) < 100:
        new.append(every_commit)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for every_commit in data:
    if 'good' in every_commit:
        good.append(every_commit)
print('一共有', len(good), '筆留言提到good')
print(good[0])
print(good[1])

# good = [every_commit for every_commit in data if 'good' in every_commit]
# 清單快寫法

# bad = ['bad' in every_commit for every_commit in data]
# print(bad)

# 文字計數
word_count = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 # 新增新的key進word_count字典

for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])

print(len(word_count))
print(word_count['Allen'])


while True:
    word = input('請問你想查什麼? ')
    if word == 'q':
        break
    if word in word_count:
        print(word, '出現過的次數為： ', word_count[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')

print('留言平均長度為', total_num / len(data))






# total_num = 0
# for str_number in data:
#     total_num = total_num + len(str_number)
# print('留言平均長度為', total_num / len(data))
