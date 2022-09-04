
data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1 # count = count + 1
        if count % 1000 == 0: #假設count目前是1001去除1000餘數等於1，不等於0，所以不會印出來
            print(len(data))
print(len(data))

print(data[0])
print('------------------')
print(data[1])