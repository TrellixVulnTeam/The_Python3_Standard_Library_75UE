class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
    """
    return [obj]
