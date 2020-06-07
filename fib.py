def fib_gen(n):
    a, b = 0, 1
    yield a
    yield b
    for i in range(0, n):
        a, b = b, a + b
        yield b


def fib(n):
    # try:
    #     if isinstance(n, float):
    #         n = int(n)
    # except TypeError:
    #     print("incorrect value")
    #     return []
    if isinstance(n, float):
        n = int(n)
    if isinstance(n, str):
        return []
    x = fib_gen(n)
    result = [next(x) for i in range(n)]
    return result


assert fib(0) == []  # Case 1
assert fib(1) == [0]  # Case 2
assert fib(2) == [0, 1]  # Case 3
assert fib(3) == [0, 1, 1]  # Case 4
assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Case 5

assert fib(-1) == []  # Case 6
assert fib(4.0) == [0, 1, 1, 2]  # Case 7
assert fib("2") == []  # Case 8
