import random
#defining list
CONSTANTS=["sushan","hem","saimon","birajan","suyoj","bijesh","mohan","sasank"]
PLACES=["naikap","kirtipur","baneshowr","maitidevi","kalanki","balaju","maitighar","thapathali"]
SURNAMES=["bhandari","saha","shrestha","raj","sitaula","karki","khati","koirala"]

def password_generate():

    #Creating a list of combination string
    strings_combination=[]
    for constant in CONSTANTS:
        for place in PLACES:
            for surname in SURNAMES:
                combination = (constant, place, surname)
                string_combination = "".join(combination)
                strings_combination.append(string_combination)

                    
                #length of combination is 512
                #total_combinations = len(combination_strings)
                #print(total_combinations

    # Select a random combination string    
    password = random.choice(strings_combination)
    return password

 
print("Password Generator\n==================\n\n")
try:
    num_passwords= int(input("How many passwords are needed?:"))
    if num_passwords < 1 or num_passwords > 24:
        print("Please enter a value between 1 and 24.")
    else:
    #generate and print the passwords
        for i in range(num_passwords):
            password=password_generate()
            print(f"{i+1} --> {password}")
except ValueError:
    print("Please enter a number.")





