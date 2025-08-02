from datetime import datetime
from functools import wraps
import time

def metric(func):
    @wraps(func)  # wrapper.__name__ = func.__name__
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"Function '{func.__name__}' executed in {duration:.4f} seconds")
        return result
    return wrapper


def log(func):
    @wraps(func) # wrapper.__name__ = func.__name__
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log  # now = log(now)
def now():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def log_with_args(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{text} - Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_args("INFO") # greet = log_with_args("INFO")(greet)
def greet(name):
    print(f"Hello, {name}!")

@metric  
def slow(): # slow = metric(slow)
    print("slow function is running...")
    time.sleep(20)  # Simulating a slow operation
    return "Done"

def main():
    now()
    print(f"Function '{now.__name__}' was called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    greet("Alice")
    print(f"Function '{greet.__name__}' was called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if "Done" == slow():
        print(f"Function '{slow.__name__}' was called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} and returned 'Done'.")

if __name__ == "__main__":
    main() 