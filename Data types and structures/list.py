
list_word = list('word') 
# ['w', 'o', 'r', 'd']

in_list = [12,[1,2,3], 23]
# print(in_list[1][0])
# 1

c = [word for word in 'shit'] 
# ['s', 'h', 'i', 't']

c = [word for word in 's hi t' if word != ' '] 
# ['s', 'h', 'i', 't']

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5.
sort_list = []
for i in a:
    if i < 5:
        sort_list.append(i)

print(sort_list)