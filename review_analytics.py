
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
print('留言平均長度為', total_num / len(data))

# total_num = 0
# for str_number in data:
#     total_num = total_num + len(str_number)
# print('留言平均長度為', total_num / len(data))
