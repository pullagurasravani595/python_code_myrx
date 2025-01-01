#  Sort hashmap by value. 

list_a = input().split(",")
dict_a = {}
for item in list_a:
    pair = item.split("=")
    key, value = pair[0], pair[1]
    dict_a[int(key)] = value
dict_b = dict(sorted(dict_a.items(), key=lambda x:x[1]))

print(dict_b)