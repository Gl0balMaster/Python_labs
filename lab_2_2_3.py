import time

def log_calls(file_name):
    def logging(func):
        def wrapper(*args,**kwargs):
            cur_time = time.asctime()
            f = open(file_name + ".txt",'w')
            f.write("название функции: " + str(func.__name__) + ", аргументы: " + str(args) +", именованные аргументы : " + str(kwargs) + ", дата вызова: " +  str(cur_time))

        return wrapper
    return logging