"""
Name: Trever Cluney
Date: 01.17.22
Email: tlcluney@dmacc.edu
Overview: Testing newly learnt wrapper function
"""


def my_decorator(func):
    def wrapper(*args):
        print(f"Doubling {str(args[0])} and tripling {str(args[1])}")
        return func(args[0] * 2, args[1] * 3)
    return wrapper
    pass


@my_decorator
def divide(x, y):
    result = 0
    try:
        result = float(x) / float(y)
    except ZeroDivisionError:
        print("Attempted to divide by zero")
    except ValueError:
        print("Inputs were not numbers")
    finally:
        return result


if __name__ == '__main__':
    print(divide(12, 2))
    print(divide(36, 4))
    print(divide(12, 0))
    print(divide(12, "hi"))
