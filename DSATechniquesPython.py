#  Input: arr = [2, 7, 11, 15], target = 9  
#  Output: [0, 1]  // because arr[0] + arr[1] = 2 + 7 = 9

# arr = [2, 7, 6, 3]
# target = 9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if(arr[i]+arr[j] == target):
#             print(f"{arr[i]} {arr[j]} is match the target {target}")


# Find the longest palindromic substring in a given string using brute force.



# def palindrom(palin):
#     return palin == palin[::-1]

# def longest_palindromic_substring(s):
#     max_len = 0
#     longest = ""
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             # print(i,j)
#             sub = s[i:j]
#             # print(sub)
#             if(palindrom(sub) and len(sub) > max_len):
#                 max_len = len(sub)
#                 longest = sub

#     return longest


# print(longest_palindromic_substring("madam"))
       

# find longest word in sentence

# sentence = "Hello my name is saad"
# slpsentenc = sentence.split(" ")
# log_word = ""

# for i in range(len(slpsentenc)):
#     if(len(slpsentenc[i]) > len(log_word)):
#         log_word = slpsentenc[i]

# print(log_word)
