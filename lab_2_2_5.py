cache_list = dict()

def caching(func):
    def wrapper(*args,**kwargs):
        if cache_list.get(args) is None:
            result = func(*args,**kwargs)
            cache_list[args] = result
            return result
        else:
            print("результат из кэша: ", cache_list[args])
            return cache_list[args]
    return wrapper