import operator
import time
import functools


def task_1():
    def get_multiplier(factor):
        def multiplier(num):
            return factor * num

        return multiplier

    doubler = get_multiplier(2)

    print(doubler(56))


    three_times = get_multiplier(3)
    
    print(three_times(5))


def task_2():
    def get_itemgetter(i):
        def ig(iterable):
            return iterable[i]

        return ig

    second_item = get_itemgetter(1)

    d = {
        'red': 34,
        'blue': 3,
        'black': 100
    }

    print(sorted(d.items(), key=second_item, reverse=True))
    print(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted(d.items(), key=lambda x: x[1], reverse=True))


def task_3():
    def wrapper(f):
        def wrapped():
            print('I am gonna run a function')
            r = f()
            print('Function ran successfully')

        return wrapped


    @wrapper
    def some_function():
        print('Hi i am here!')

    some_function()


def task_4():
    def timer(f):
        def wrapped():
            t0 = time.time()
            f()
            print(time.time() - t0)

        return wrapped


    @timer
    def some_function():
        for _ in range(1000):
            print('Hi i am here!', end=' ')
        print()

    some_function()


def task_5():
    """
    With args and ret value
    """
    def with_arg_info(f):
        def wrapped(*args, **kwargs):
            print(f'My variables: {args, kwargs}')
            r = f(*args, **kwargs)
            print(f'Gonna return {r}')
            return r

        return wrapped


    @with_arg_info
    def add(a=1, b=0):
        return a + b


    print(add(3, 4))
    print(add(a=3, b=4))
    print(add(3, b=4))


def task_6():
    def repeat(n):
        def wrapper(f):
            def wrapped():
                for _ in range(n):
                    f()

            return wrapped
        return wrapper

    @repeat(5)
    def some_function():
        print('Hi i am here!')

    some_function()


def task_7():
    def print_func_name(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            print(f'Gonna run function "{f.__name__}", that "{f.__doc__.strip()}"')
            r = f(*args, **kwargs)
            return r

        return wrapped


    @print_func_name
    def add(a=1, b=0):
        """
        Returns the sum of a and b
        """
        return a + b

    print(add.__name__)  # ft.wraps nélkül ez 'wrapped'
    print(add(3, 4))




def task_8():
    @functools.lru_cache()
    def add(a, b):
        print(f'Calculating {a}+{b}')
        return a + b

    print(add(3, 4))
    print(add(3, 4))
    print(add(3, 5))




def task_9():
    @functools.lru_cache()
    def factorial(n):
        print(f'Calculating the factorial of {n}')
        return n * factorial(n - 1) if n else 1

    print(factorial(4))
    print(factorial(7))
    print(factorial(7))
    print(factorial(8))



def task_10():
    """
    Parse url call
    :return:
    """

def task_11():
    """
    Return json
    :return:
    """







if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    task_9()
    # task_10()
    pass
