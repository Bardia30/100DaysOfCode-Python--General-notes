class Array:
    def __init__(self, size):
        self.size = size
        self.__array= []
        if self.size < 0:
            raise ValueError("size cannot be less than zero")
        # elif type(self.size) != "<class 'int'>":   
        #     raise TypeError("Size must be of type integer")
        
        for i in range(self.size):
            self.__array.append(0)

    def insert(self, item):
        for i in range(self.size):
            if self.__array[i] == 0:
                self.__array[i] = item
                break
        return self.__array

    def removeAt(self, index):
        self.__array[index] = 0
        return self.__array

    def indexOf(self, element):
        for i in range(len(self.__array)):
            if self.__array[i] == element:
                return i
            
numbers = Array(3)

print(numbers.insert(10))
print(numbers.insert(20))
print(numbers.insert(30))

print(numbers.removeAt(1))

print(numbers.indexOf(30))









