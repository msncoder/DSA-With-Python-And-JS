# Check Even or Odd

# a = input("Enter a number: ")
# a = int(a)
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# Multiplication Table

# table = int(input("Enter a number"))

# for i in range(1,11):
#     print(f"{table} X {i} = {table*i}")


    # natural_number = int(input("Enter a natural number"))
    # sum_of_natural_number = 0

    # for i in range(1,natural_number+1):
    #     # print(i)
    #     sum_of_natural_number += natural_number

    # print(sum_of_natural_number)


# Swap Two Numbers

# a = 10
# b = 20
# temp = b
# b = a
# a = temp

# print(a)
# print(b)


# Closest Number

# n = 16
# m = 4

# q = int(n / m)
# # print(q)
# n1 = m * q
# # print(n1)
# if ((n*m) > 0):
#     n2 = (m*(q+1))
    
# else:
#     n2 = (m*(q-1))

# if(abs(n-n1) < abs(n-n2)):
#     print(n1)
# else:
#     print(n2)


# Dice Problem

# dice = int(input("Roll a dice: "))

# if(dice == 1):
#     print("6")

# elif(dice == 2):
#     print("5")

# elif(dice == 3):
#     print("4")

# elif(dice == 4):
#     print("3")

# elif(dice == 5):
#     print("2")

# else:
#     print("1")

# Nth term of AP from First Two Terms

# Input : a1 = 1, a2 = 3, n = 10
# Output : 19

# a1 = 1
# a2 = 3 
# n = 10
# a = n * 2
# output = 15

# for i in range(1,a,2):
#     if(i == output):
#         print(i)
        

# Easy Problems

# Sum of Digits

# Explanation: The sum of its digits are: 6 + 8 + 7 = 21

# sum = 0
# inp = int(input("Enter a three digits"))

# a = inp%10

# b = inp//10

# c = b % 10

# d = b // 10

# print(a)
# print(b)
# print(c)
# print(d)
# print(a+c+d)

# Write a program to reverse digits of a number
inp = int(input("Enter a tree digit"))
rev = 0

while(inp > 0):
    a = inp % 10
    rev = rev * 10 + a
    inp = inp // 10

print(rev)