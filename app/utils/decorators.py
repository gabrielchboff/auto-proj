def thrower(func):
    """
    Decorator to throw an exception if the function throws one.
    """

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise e

    return wrapper
