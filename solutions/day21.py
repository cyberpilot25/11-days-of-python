#code to retrieve values from dictionary:

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

x = str(input())

if x == 'Singapore':
    print(data['Singapore'])
elif x == 'Ireland':
    print(data['Ireland'])
elif x == 'United Kingdom':
    print(data['United Kingdom'])
elif x == 'Germany':
    print(data['Germany'])
elif x == 'Armenia':
    print(data['Armenia'])
elif x == 'United States':
    print(data['United States'])
elif x == 'Canada':
    print(data['Canada'])
elif x == 'Italy':
    print(data['Italy'])
else:
    print('Not found')