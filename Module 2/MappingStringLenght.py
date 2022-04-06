"""
Name: Trever Cluney
Email: tlcluney@dmacc.edu
Date: 01/24/22
Overview: function that takes in strings or list of strings that outputs a list of string with a size
"""


def mapping_string_size(string_size):
    """returns a list that holds the sting input and its size"""
    return [str(string_size), len(str(string_size))]


if __name__ == '__main__':
    list_of_strings = ["Hello", "Jon", "I'm", "afraid", "can't", "do", "that", "goodbye", "space", "looping"]
    print(mapping_string_size("myword"))
    results = list(map(mapping_string_size, list_of_strings))
    print(results)
    for result in results:
        if result == results[-1]:
            print(result[1], end='')
        else:
            print(result[1], end=', ')

    pass
