password1=(input("please enter password:"))
password2=(input("please enter password:"))
if len(password1)>=8 and len (password1)<=12:

    if password1==password2  :
        print("Password set")
    
    
else:
    print("Error!")    
