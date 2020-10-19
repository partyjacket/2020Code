dict1 = {'one': 1}
dict1['two'] = 2


print(dict1)

list1 = [dict1[key] for key in dict1]

print(list1)

print(dict1['two'])

for x in dict1.items():
    print(x[1])


for i in range(len(dict1)):
    print(i)