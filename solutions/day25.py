#creating lamda function
price = int(input())
perc = int(input())

calculate_discount = lambda x, y: y/100 * x
res = calculate_discount(price, perc)

print(res)