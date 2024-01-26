#code to add increment in salaries
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

salaries = list(map(lambda salaries: salaries + bonus, salaries))
print(salaries)