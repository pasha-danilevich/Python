# Question: Write a program which can compute the factorial 
# of a given numbers. The results should be printed in a 
# comma-separated sequence on a single line. Suppose the following 
# input is supplied to the program: 8 Then, the output should be: 40320

# My solution

number = 4


def factorial(number):
    result = 1
    for i in range(1, number):
        result += i * result
        print(f'Внутри цикла: {i}')
    return result
        
print(factorial(number))

# Current solution

def fact(x):
    if x == 0:
        return 1
    else:
        return fact(x - 1) * x
    
print(fact(4))


# mylist = (x*x for x in range(3))
# for i in mylist :
#     print(i)
    
    
# for i in mylist :
#     print(i)

        