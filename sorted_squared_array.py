#given an array of non-empty, sorted ascending integers, 
# a function that return an array of squared array, in sorted order. 



def sortedSquaredArray(array):
    # Write your code here.
    
    squared_array = []
    for item in array: #O(n)
        squared_array.append(item**2)
    squared_array.sort()
    return squared_array #O(nlogn)


print(sortedSquaredArray([-7, -4, 1,2,3,5,6,8,9]))