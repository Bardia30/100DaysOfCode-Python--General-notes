
#create an empty array
#create a variable, asign the first element to it
#loop over array
# if current num plus variable, is targetSum, add current to array, else, re-assign variable to next element  
#return that created array


def twoNumberSum(array, targetSum):
    # Write your code here.
    new_dict = {} 
    
    for x in array:
        # print(f"current num: {num} \n current initial_element: {initial_element}")
        # print(F"sum: {num + initial_element}")
        y = targetSum - x
        if y in new_dict:
            return [x, y]
        else:
            new_dict[x] = True
    return []
print(twoNumberSum([3,5,-4,-8,11, 1, -1, 6], 10))