cache_list = dict()

def caching(func):
    def wrapper(*args,**kwargs):
        if cache_list.get(args) is None:
            result = func(*args)
            cache_list[args] = result
            return func(*args,**kwargs)
        else:
            print("результат из кэша: ", cache_list[args])
            return cache_list[args]
    return wrapper