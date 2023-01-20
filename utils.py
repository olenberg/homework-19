def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print(result)
        print("after")
        # return result
    return wrapper

@decorator
def func(user_name):
    return user_name

# print(func("q"))