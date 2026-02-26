# def fruits(fruits):
#     for fruit in fruits:
#         print(fruit)
# fruits(["apple", "banana", "cherry"])       


# def multiply(a,b):
#     return  a*b
# print(multiply(2,5))

# numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

# def even_numbers(numbers):
#     even=[]
#     for number in numbers:
#         if number % 2 ==0:
#             even.append(number)
#             print(even)
# even_numbers(numbers)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


# machines = ["mac", "window", "linux", "php"]

# def check_machine(machines):
#     if "apple" not in machines:
#         print("Apple is not there")
#     else:
#         print("Apple is there")

# check_machine(machines)

lists=[2,3,4,5]

print(list(map(lambda x:pow(x,2),lists)))
