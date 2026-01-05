class encapsulation:

    __user_id=0

    def __init__(self, name, age):
        self.__name=name ##private
        self.age=age
        encapsulation.__user_id+=1
        self.user_id=encapsulation.__user_id

    
    def get_id(self):
        return self.user_id

    def set_id(self):
        self.user_id=encapsulation.__user_id+5
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name=name

# obj=encapsulation('Hitesh', 20)

# print('sample',obj.get_name())

# obj.set_name('New')

# print(obj.get_name())


obj1=encapsulation('h', 20)

print(obj1.user_id)

obj2=encapsulation('j', 20)

obj2.set_id()

print(obj2.user_id)
