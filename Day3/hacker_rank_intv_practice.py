# def plusMinus(arr):
#     # Write your code here
#     array_length = len(arr)
#     positive_array = []
#     negative_array = []
#     zero_array = []
#     for i in arr:
#         if i>0:
#             positive_array.append(i)
#         elif i == 0:
#             zero_array.append(i)
#         else: 
#             negative_array.append(i)
#     negative_count = len(negative_array)
#     positive_count = len(positive_array)
#     zero_count = len(zero_array)
    
#     pos_ratio = round(positive_count/array_length, 6)
#     neg_ratio = round(negative_count/array_length, 6)
#     zero_ratio = round(zero_count/array_length, 6)
    
#     print(f"{pos_ratio:.6f}")
#     print(f"{neg_ratio:.6f}")
#     print(f"{zero_ratio:.6f}")

# plusMinus([1,1,0,-1,-1])


# def miniMaxSum(arr):
#     # Write your code here
#     array_of_integers = [int(num) for num in arr.split()]
#     array_sum = sum(array_of_integers)
#     max_sum = array_sum - min(array_of_integers)
#     min_sum = array_sum - max(array_of_integers)
#     print(min_sum, max_sum)

# miniMaxSum("1 2 3 4 5")

def timeConversion(s):
    am_pm = s[-2:]
    hour = int(s[0:2])
    if am_pm == 'PM' and hour != 12:
        hour += 12
    elif am_pm == 'PM' and hour == 12:
        hour = 0
    
    print(f"{hour,'02'}s[3:]")

timeConversion("12:01:00PM")