#  Input: arr = [2, 7, 11, 15], target = 9  
#  Output: [0, 1]  // because arr[0] + arr[1] = 2 + 7 = 9

arr = [2, 7, 6, 3]
target = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j] == target):
            print(f"{arr[i]} {arr[j]} is match the target {target}")

       