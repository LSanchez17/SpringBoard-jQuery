def repeat(phrase, num):
    """Return phrase, repeated num times.
        >>> repeat('*', 3)
        '***'
        >>> repeat('abc', 2)
        'abcabc'
        >>> repeat('abc', 0)
        ''
    Ignore illegal values of num and return None
        >>> repeat('abc', -1) is None
        True
        >>> repeat('abc', 'nope') is None
        True
    """
    if num <= 0:
        return 'Incorect Data'
    else:
        return phrase*num

print(repeat('*', 3))
print(repeat('abc', 0))
print(repeat('abc', -1))
