#code to take input from disctionary and output its value.
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
} #created dictionary

#saving key value of dictionary
year = car['year']
brand = car['brand']
color = car['color']
mileage = car['mileage']

#taking input from user
x = str(input())

#setting conditions
if x == 'brand':
    print(brand)
elif x == 'color':
    print(color)
elif x == 'year':
    print(year)
else:
    print(mileage)