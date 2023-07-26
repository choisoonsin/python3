import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper

@timer
def my_function():
    print("do something")

if __name__ == '__main__':
    my_function()