def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = 3 * func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b):
    return a + b


@logger
def summ_1(a,b):
    return a - b


# function = logger(summ)
# print(function(2,3))

# print(logger(summ)(2,3))

# summ = logger(summ)
# print(summ(2,3))

print(summ(2, 3), summ_1(4, 2))
