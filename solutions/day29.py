def convert(num):
    if num == 0:
        return "0"
    else:
        return str(num % 2 + 10 * int(convert(num // 2)))

# Taking input from the user
decimal = int(input())

# Calling the function and printing the result
print(convert(decimal))
