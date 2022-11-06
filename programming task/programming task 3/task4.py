BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1=(input("please enter password:"))
password2=(input("please enter password:"))

if password1 in BAD_PASSWORDS:
    print("Password cannot form list")

else:

    if len(password1)>=8 and len (password1)<=12:
        if password1 == password2:
            print("Password set")

        else:
            print("Passwords do not match!")
        
    else:
        print("Password must be between 8 - 12!")

