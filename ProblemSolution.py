# Basic Problems

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
        

# Introduction to Primality Test and School Method

# n = int(input("Enter a prime Number"))

# if n <= 1:
#     print("false")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print("False")
#             break
#     else:
#         print("true")


# Check if a number is a power of another number

# p = int(input("Enter a power number"))
# n = int(input("Enter a number"))

# if p == 1:
#     print(n == 1)

# else:
#     pow = 1
#     while pow < n:
#         pow *= p
#     print(pow == n)


# Distance between Two Points

# p1 = int(input("Enter a point one"))
# p2 = int(input("Enter a point two"))
# s1 = int(input("Enter a point one"))
# s2 = int(input("Enter a point two"))
# distance = (((p2 - p1) ** 2) + ((s2 - s1) ** 2)) ** 0.5

# print(f"distance between two point {distance}")       


# Check whether triangle is valid or not if sides are given

# inp1 = int(input("enter a first side"))
# inp2 = int(input("enter a second side"))
# inp3 = int(input("enter a third side"))

# if(((inp1+inp2)>inp3) or ((inp1+inp3)>inp2) or ((inp2+inp3)>inp1)):
#     print("valid triangle")
# else:
#     print("not a valid triangle")


# Find if two rectangles overlap  

# Rectangle 1 coordinates
x1_left = 0
y1_top = 10
x1_right = 10
y1_bottom = 0

# Rectangle 2 coordinates
x2_left = 5
y2_top = 5
x2_right = 15
y2_bottom = -5

# Check if they do not overlap
if (x1_left >= x2_right or x2_left >= x1_right or
    y1_bottom >= y2_top or y2_bottom >= y1_top):
    print("Rectangles do NOT overlap")
else:
    print("Rectangles OVERLAP")
