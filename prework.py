# Question 1- Write a function to print "Hello_USERNAME"

# def hello_name(user_name):
#     print("Hello, " + user_name.upper() + "!")

# hello_name('Carlos')

# Question 2- Print first odd numbers between 1 and 100

# def odd_numbers():
#     for i in range(1,101,2):
#         print(i)

# odd_numbers()

# # Question 3- Write a function that returns the max number in a given list:

# def max_num_in_list(a_list):
#     max_num = max (a_list)
#     return max_num

# test = max_num_in_list([2,3,5,8,9])
# print(test)

#Question 4 - Write a function to return of the given year is leap year

# def is_leap_year(a_year):
#     if a_year % 4 == 0 and a_year % 100 != 0:
#         print(f'{a_year} is a leap year')
#     elif a_year % 400 == 0:
#         print(f'{a_year} is a leap year')
#     else:
#         a_year = False
#         print(f'{a_year}')


# Question 4 1.b solution

def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap(2019)

#Question 5 - Write a function to check if all numbers in a list are consecutive
# def is_consecutive(a_list):
#     i = 0
#     status = True
#     while i < len(a_list) - 1:
#        if a_list[i] + 1 == a_list[i + 1]:
#            i += 1
#        else:
#             status = False
#             break
#     return(status)

# my_list=[2,3,4,5,6,7,8,9,10]

# if is_consecutive(my_list):
#     print("The list is consecutive")
# else:
#     print("The list is not consecutive")


