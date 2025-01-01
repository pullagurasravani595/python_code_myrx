# Given an array of Red Green Blue balls.You have to sort it. 

def get_required_sorted_list(list_a):
    for i in range(len(list_a)):
        for j in range(0, len(list_a)-i-1):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
    return list_a            
            
list_a = input().split()
res = get_required_sorted_list(list_a)
print(res)