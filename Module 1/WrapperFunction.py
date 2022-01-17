"""
Name: Trever Cluney
Date: 01.17.22
Email: tlcluney@dmacc.edu
Overview: Testing newly learnt wrapper function
"""


def my_decorator(func):
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
    print(divide("Hello", "Hi"))
    print(divide(17, 0))
    print(divide(12, 2))
