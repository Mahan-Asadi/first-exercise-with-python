def divide_by_zero_safe():
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError:
        print("Error: Division by zero occurred!")

result = divide_by_zero_safe()
if result is not None:
    print(result)
