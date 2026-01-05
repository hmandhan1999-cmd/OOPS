class encapsulation:

    def __init__(self, name, age):
        self.__name=name ##private
        self.age=age
    
    def get_name(self):
        return self.__name

obj=encapsulation('Hitesh', 20)

print(obj.age, obj._encapsulation__name)