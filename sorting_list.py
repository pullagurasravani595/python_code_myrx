# Given a sorted array of positive and negative numbers. You have to Square it and sort it. 

def sorting_given_list_square(list_a):
    list_b = []
    for item in list_a:
        num = item * item
        list_b.append(num)
    list_c = sorted(list_b)  
    return list_c
    
list_a = list(map(int, input().split(",")))
res = sorting_given_list_square(list_a)
print(res)