#code for defining args and kwargs
def my_min(*args):
    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value

print(my_min(8, 13, 4, 42, 120, 7))