print ("""LOGIN PAGE.
Please enter your username and password to login.""")
print()
username = input("Username: ")
password = input("Password: ")
if username == "Jack" and password == "Jack1":
  print("Login successful. Welcome Jack!")
elif username == "Jill" and password == "Jill1":
  print("Login successful. Welcome Jill!")
elif username == "Jane" and password == "Jane1":
  print("Login successful. Welcome Jane!")
else:
  print("Login unsuccessful. Please try again.")