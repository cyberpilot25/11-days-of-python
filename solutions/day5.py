interest = input("What is your interest? Movie,show or something else?")
if interest == "Movie":
  Movie = str(input("which movie?"))
  if Movie =="Harry Potter":
    print("Sounds good. I have to check it out.")
  else:
    print("I have not seen that one yet.")
elif interest == "Show":
  str(input("You got it. Which one?"))
  print("Yeah, that is interesting.")
elif interest == "something else":
  str(input("What is it?"))
  print("That is great. Tell me more.")
else:
  print("Bro you are not making sense.")