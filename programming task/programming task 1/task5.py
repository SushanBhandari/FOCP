No_of_students=[113,175,12]
lab_group=24

for i in range(0,3):
    print("group is " %(i+1,No_of_students[i]/lab_group))
    print("students leftover is"%(i+1,No_of_students[i]%lab_group) )
    
