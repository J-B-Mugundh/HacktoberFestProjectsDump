def is_palindrome():
    """
    One-liner palindrome check.

    Examples:
        >>> is_palindrome()  # test with 'madam'
        madam
        Palindrome
        >>> is_palindrome()  # test with 'hello'
        hello
        Not a palindrome
    """
    print("Palindrome" if (s := input()) == s[::-1] else "Not a palindrome")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    is_palindrome()
