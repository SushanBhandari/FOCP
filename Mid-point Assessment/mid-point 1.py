
name = input("Greetings! How shall we call you? ")

name=name.title()

if name.startswith("Lord") or name.startswith("Lady"):
    print("It shall be so, " + name + "!")
else:
    print("You may not be known by that name!")
 