def fib(n):
    a, b = 0, 1
    result = [a, b]
    try:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n < 0:
            return []
        if isinstance(n, float):
            n = int(n)
    except TypeError:
        print("incorrect value")
        return []

    for i in range(2, n):
        a, b = b, a + b
        result.append(b)
    return result


assert fib(0) == []  # Case 1
assert fib(1) == [0]  # Case 2
assert fib(2) == [0, 1]  # Case 3
assert fib(3) == [0, 1, 1]  # Case 4
assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Case 5

assert fib(-1) == []  # Case 6
assert fib(4.0) == [0, 1, 1, 2]  # Case 7
assert fib("1") == []  # Case 8




