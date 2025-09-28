def type_check(type_1, type_2):
    def checker(func):
        def wrapper(*args,**kwargs):
            if(type_1 != type(args[0]) or type_2 != type(args[1])):
                raise TypeError("один из типов не совпадает с заданным")
        return wrapper
    return checker