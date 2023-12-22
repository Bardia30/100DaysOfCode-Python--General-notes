# #list unpacking
# my_list = [1,2,3]

# first, second, third = my_list


 # print(first)

 # my_list2 = [1,2,3,4,5,3,21,34,3,2]

 # first, second, *others = my_list2

 # print(others)

# # my_list3 = [1,3,4,69]

# first, *other, last =  my_list3


# letters = ["a", "b", "c"]

 # for letter in enumerate(letters):
 #     print(letter[0], letter[1])

 #for accessing the index and the list item ---> use enumerate()

# for index, item in enumerate(letters):
#     print(index, item)


# #add item to last
# letters = ["a", "b", "c"]
# letters.append('d')

# #add to beginning
# letters.insert(0, "z")


# #remove from last 
# letters.pop()

# #remove from index
# letters.pop(1)

# #remove a specific first occurance 
# letters.remove("a")

# #remove a range of items

# del letters[:2]

# #clear out the list 
# letters.clear()


# #find the index of an item 
# letters.index("a")

# #to see if item is in the list
# letters.count("a") #returns number of occurances in the list


# #sort list in ascending
# letters.sort()

# #sort in descending

# letters.sort(reverse=True)

# #.sort() will modify the original list

# sorted(letters) #returns a copy of the original

# sorted(letters, reverse=True)


# example
# items = [
#     ("product1", 10),
#     ("product2", 7),
#     ("product3", 13)
# ]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)


#LAMBDA FUNCTIONS
#basically an anonymous function in python
# items = [
#     ("product1", 10),
#     ("product2", 7),
#     ("product3", 13)
# ]

# items.sort(key=lambda item:item[1])
# print(items)


# items = [
#     ("product1", 10),
#     ("product2", 7),
#     ("product3", 13)
# ]


# for item in items:
#     prices.append(item[1])
# print(prices)

# prices = list(map(lambda item:item[1], items))

# print(prices)


# items = [
#     ("product1", 10),
#     ("product2", 7),
#     ("product3", 13)
# ]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


#LIST COMPREHENSION

#map with list comprehension

# prices = [item[1] for item in items]
# print(prices)

#filter with list comprehension

# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# list1 = ["a", "b", "c"]
# list2 = [1,2,3,4]

# zipped = list(zip(list2, list1))

# print(zipped)


#stack (a data structure) (like a stack of books)
#LIFO las in first out 

# browsing_session =[]
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)

# last = browsing_session.pop() 
# browsing_session[-1] #item on top of the stack


#Queue 
#FIFO (like a line up)
# from collections import deque

# queue = deque([])

# queue.append(1)
# queue.append(2)
# queue.append(3)

# queue.popleft()
# queue.popleft()
# queue.popleft()
# if not queue:
#     print("queue is empty")

# print(queue)


#tuples
# like a list, but it is immutable

# point = (1,2,3)
# # # or
# # point = 1,2,3

# #swapping variables

# x = 10
# y=11

# x, y = y, x

# # or

# # z = x
# # x = y
# # y = z

# print("x", x)
# print("y", y)

#Array
# for large list of numbers

# from array import array
# numbers = array("i", [1,2,3])
# #They are Typed. Can only take a specific type. For example only integer
# print(numbers[0])


#set
# a collection with no duplicates, unordered (cannot index)

# numbers = [1,2,3,3,4,5,5]

# uniques = set(numbers)
# print(uniques)
# uniques.add(6)
# uniques.remove(1)
# print(uniques)

# #union of two sets
# set1 | set2

# #intersection of two sets 
# set1 & set2

#difference of two sets 
# set1 - set2

#symmetric difference
#set1 ^ set2



#Dictionary (hash map)

# point = {
#     "x": 1, 
#     "y": 2
# }
# or 
# point = dict(x=1, y=2)
# print(point["x"])
# point["z"] = 3

# for p in point:
#     print(point[p])
    


# values = []
# for x in range(5):
#     values.append(x*2)

# values = [x*2 for x in range(0,5)]


# print(values)

# values = {}
# for x in range(5):
#     values[str(x)] = x*2

# values = {str(x): x*2 for x in range(1,5)}

# print(values)


#Exercise

sentence = "This is a common interview question"


# create an empty dictionary
#iterate through the string, gonna assume " " is also a character
#add each char as the key, and its count as the value 
# iterate through the list again, return the key with the highest count

# highest_count = 0
# highest_char = ""
# chars = {}

# for char in sentence:
#     if char in chars:
#         chars[char] += 1
#     else: 
#         chars[char] = 1
# del chars[" "]

# for key in chars:
#     if chars[key] > highest_count:
#         highest_count = chars[key]
#         highest_char = key
# print(highest_char, " : ",  highest_count)

#Mosh's solution
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])