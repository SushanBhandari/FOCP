
password = "parrot"
user_password = input("Greetings! What is the password? ")


while user_password != password:
    print("Incorrect! You may try again.")
    user_password = input("Greetings! What is the password? ")
print("Correct! You may enter.")
