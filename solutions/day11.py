#Day 11: grade generator
test = str(input("Enter test name: "))
obtained_score = int(input("Enter obtained score: "))
max_score = int(input("Enter maximum score: "))
percentage = float(round(obtained_score/max_score * 100))
if percentage >= 90 and percentage <= 100:
  print("You got A+")
elif percentage >= 80 and percentage <= 89:
  print("You got A")
elif percentage >= 70 and percentage <= 79:
  print("You got B")
elif percentage >= 60 and percentage <= 69:
  print("You got C")
elif percentage >= 50 and percentage <= 59:
  print("You got D")
else:
  print("You got U")