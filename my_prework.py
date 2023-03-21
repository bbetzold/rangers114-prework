# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#     def hello_name(user_name):
# ...........................................................

def hello_name(user_name):
    print(user_name)
user_name =  input("Please enter your name. ")
hello_name(user_name)

#_________________________________________________________________________________              
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#     def first_odds():
# ...........................................................
def first_odds(number_range):
    for x in range(1,number_range,2):
        print(x)
number_range = 101
first_odds(number_range)

#_________________________________________________________________________________  
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#     def max_num_in_list(a_list):
# ...........................................................

#create a_list from user input


continue_list = True
a_list = []

while continue_list == True:
    yes_no = input("Do you want to add a new item to the list? Enter Y, for yes, or N for no\n")
    if yes_no.lower() == "y":
        new_item = int(input("Please enter the list item.\n"))
        a_list.append(new_item)
    else:
        continue_list = False

def max_num_in_list(b_list):
    b_list.sort()
    print(b_list[-1])
    print(b_list)
        
max_num_in_list(a_list)



#_________________________________________________________________________________               
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#     def is_leap_year(a_year):
# ...........................................................

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0 and a_year % 100 == 0 and a_year % 4 ==0):
        return True
    else:
        return False

user_year = int(input("Please enter any year.\n"))

result = is_leap_year(user_year)

if result == True:
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is not a leap year.")


#_________________________________________________________________________________               
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#     def is_consecutive(a_list):
# ...........................................................

#create a_list from user input


index_list = True
d_list = []

while index_list == True:
    yes_no = input("Do you want to add a new item to the list? Enter Y, for yes, or N for no\n")
    if yes_no.lower() == "y":
        new_item = int(input("Please enter the list item.\n"))
        d_list.append(new_item)
    else:
        index_list = False

def is_consecutive(f_list):
    list_length = len(f_list)
    for x in range (0,list_length-1,1):
        status = True
        if (f_list[x] + 1 or f_list[x]-1)== (f_list[x+1]):
            status = True
        elif (f_list[x] == f_list[0]) and (f_list[x] + 1 == f_list[x+1]):
            status = True
        else:
            status = False
            return status
            break
    return status

if is_consecutive (d_list) == True:
    print("The list is consecutive.")
else:
    print("The list is not consecutive")

