#Q1 Debugged code#
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = input(("What language are we writing in?"))
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = input("Which lesson number is this?")
if ans2 > "12":
  print("We're not quite that far yet")
elif ans2 == "12":
  print("That's right!")
else:
  print("We've gone well past that!")

#Q2 solution#
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
num = int(input())
if num in x:
    print("bingo")

