def square(x):
    '''
    引数xを2乗して結果を返す
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x

if __name__ == "__main__":
    import doctest, my_math
    doctest.testmod(my_math)