def divide_by_zero_safe():
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError:
        return None

result = divide_by_zero_safe()
if result is not None:
    print(result)
