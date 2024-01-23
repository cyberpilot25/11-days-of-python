#Learning tuple unpacking
def calc(x):
    p = 4 * side
    a = side * side
    return (p, a)

side = int(input())
p, a = calc(side)

print("Perimeter:", p)
print("Area:", a)

#Learning sets
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

matched_skills = skills & job_skills

if matched_skills:
    print(matched_skills.pop())
else:
    print()

