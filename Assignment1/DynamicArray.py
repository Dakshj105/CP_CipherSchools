import ctypes

class myList:

    def __init__(self):
        self.number_of_ele = 0
        self.size = 1
        self.Dy_Array = self._make_dyArray(self.size)


    def _make_dyArray(self, capacity):

        return (capacity * ctypes.py_object)()


    def append(self, value):
        
        if self.size == self.number_of_ele:
            self.resize(2 * self.size)
            
        self.Dy_Array[self.number_of_ele] = value
        self.number_of_ele += 1

    def resize(self, new_cap):
        
        temp = self._make_dyArray(new_cap)
        self.size = new_cap
        
        for i in range(self.number_of_ele):
            temp[i] = self.Dy_Array[i]

        self.Dy_Array = temp

    def __len__(self):

        return self.number_of_ele

    def __getitem__(self, index):
        
        try:
            return self.Dy_Array[index]

        except(IndexError):
            return "Index out of bounds"

    def __str__(self):

        lis = ""
        for i in range(self.number_of_ele):
            lis += str(self.Dy_Array[i]) + ","
        lis = lis[:-1]
        return "[" + lis + "]"

    def insert(self, index: 'Index', value: 'Value'):
            try:
                if self.size == self.number_of_ele:
                    self.resize(2 * self.size)
                for i in range(self.number_of_ele, index, -1):
                    self.Dy_Array[i] = self.Dy_Array[i - 1]
                self.Dy_Array[index - 1] = value
                self.number_of_ele += 1

            except(IndexError):
                print("Index Out Of Bounds")

    def __delitem__(self, index:"Index"):                 #Magic Function
        if 0 <= index  <= self.number_of_ele:
            for i in range(index + 1, self.number_of_ele):
                self.Dy_Array[i - 1] = self.Dy_Array[i]

            self.number_of_ele -= 1

        else:
            print("Index Error")
    def searchIndex(self, value:'Value'):
        for i in range(self.number_of_ele):
            if self.Dy_Array[i] == value:
                return i
        return -1

    def removeitem(self, value:"Value"):
        index = self.searchIndex(value)
        if index != -1:
            myList.__delitem__(self, index)                 #Syntax to call a magic function

    def pop(self):
        myList.__delitem__(self, self.number_of_ele - 1)

    def clear(self):
        self.number_of_ele = 0
        self.size = 1


a = myList()
a.append(1)
a.append(2)
print(a[10],len(a))
print(a)
a.append(4)
print(a)
a.insert(10, 5)
print(a)
del a[1]
print(a)
a.removeitem(1)
print(a)
a.append(1)
a.append(6)
a.append(6)
a.append(7)
print(a)
print(a.searchIndex(6))
a.pop()
print(a)
a.clear()
print(a)