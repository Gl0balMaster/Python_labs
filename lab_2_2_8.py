import time

def timing(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        runtime = end - start
        print(f"время выполнения в милисекундах: {runtime*1000:.7f}")
        return result
    return wrapper