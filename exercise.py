def divide_by_zero_safe():
    #add try
    try:
        result = 10 / 0
        return result
    #add except
    except ZeroDivisionError:
        print("Error: Division by zero occurred!")

result = divide_by_zero_safe()
if result is not None:
    print(result)
