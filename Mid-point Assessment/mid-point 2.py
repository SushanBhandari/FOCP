slices=int(input("How many slices of spam?"))
if slices > 1:
    print("egg with spam,",end=" "  )
    for i in range(slices -2):
        print("spam,",end=" ")
    print("and spam comming up!")
else:
    print("egg with spam comming up!")        