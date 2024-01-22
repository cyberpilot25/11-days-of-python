#code to search in contacts
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()

found = False

for contact in contacts:
    if name == contact[0]: #0 represents column 1 ie, contact name
        print(name, 'is', contact[1]) #1 represents column 2 ie, age
        found = True
        break

if not found:
    print('Not Found')
