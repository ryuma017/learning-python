def gcd(a, b):
    '''
    引数a, bの最大公約数を返す
    >>> gcd(10, 15)
    5
    >>> gcd(12, 18)
    6
    '''
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

if __name__ == "__main__":
    import doctest, exer16
    doctest.testmod(exer16)