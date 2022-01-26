st = input("Enter any string: ")
dic = {}
length = len(st)
for i in range(length):
    if st[i] not in st[0:i]:
        count = 0
        for j in range(i, length):
            if st[j] == st[i]:
                count += 1
        dic[st[i]] = count

print("The frequency of each character is:")
for key, val in dic.items():
    print(key, val)
