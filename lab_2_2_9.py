def type_check(*types):
    def checker(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {i+1} должен быть {expected_type}, получен {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return checker