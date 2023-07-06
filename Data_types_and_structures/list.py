
list_word = list('word') 
# ['w', 'o', 'r', 'd']

in_list = [12,[1,2,3], 23]
# print(in_list[1][0])
# 1

c = [word for word in 'shit'] 
# ['s', 'h', 'i', 't']

c = [word for word in 's hi t' if word != ' '] 
# ['s', 'h', 'i', 't']

def task_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # Выведите все элементы, которые меньше 5.
    sort_list = []
    for i in a:
        if i < 5:
            sort_list.append(i)
    
    return sort_list

# print(task_1()) # [1, 1, 2, 3]
    




def task_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return list(filter(lambda elem: elem in a, b))

print(task_2())