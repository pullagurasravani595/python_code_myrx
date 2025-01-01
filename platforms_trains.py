# the task is to find the minimum number of platforms required so that no train waits. 

def create_num_list(list_a):
    new_list = []
    for item_1 in list_a:
        split_item = item_1.split(":")
        Sum = ""
        for item_2 in split_item:
            Sum += item_2
        new_list.append(int(Sum))
    return new_list   
 
list_a = input().split(",")
list_b = input().split(",")
num_arrive = sorted(create_num_list(list_a))
num_depture = sorted(create_num_list(list_b))
#print(num_arrive)
#print(num_depture)
platform = 1 
result = 1 
i = 1 
j = 0 
while i < len(num_arrive) and j < len(num_depture):
    if num_arrive[i] <= num_depture[j]:
        platform += 1 
        i += 1 
    elif num_arrive[i] > num_depture[j]:
        platform -= 1 
        j += 1 
    if platform > result:
        result =platform
print(result)