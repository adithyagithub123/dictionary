dictionary1 = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(dictionary1)
k = 2

count = 0

for i in dictionary1 :
    if dictionary1[i] == k :
        count = count + 1

print(count)
