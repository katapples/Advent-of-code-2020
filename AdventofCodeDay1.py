#find the two (or three for part two) numbers in a text file that add to 2020 and output their product 
file = open(r"numbersForDay1.txt")
arr = file.readlines()  #read all lines into an array

for a in range(len(arr)):
    arr[a] = int(arr[a]) #converting to integers
# print arr #check the array

for i in range (len(arr)-1): #go thru each number
    for j in range (len(arr)): # and check it against every other number in the array
        for k in range (len(arr)): # and check it against the third number for part two of the challenge
            if  arr[i]+arr[j]+arr[k]== 2020: #output product if nunmbers sum to 2020
