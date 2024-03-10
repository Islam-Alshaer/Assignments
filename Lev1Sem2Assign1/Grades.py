"""
#File : onehundred
#purpose : the user enters a mark and the program retruns the grad A+, A...etc.
#ID : 20230062
#Author : Islam Waleed Salah AbdElmotaleb
"""

"""
note that this program could be done using the idea 
of dictionary but our team decided that this method (using lists is much simpler and understandable code) 
"""

# this code can be done using a gigantic if else block, but I did it using a #### for the sake of reducing code size

print("This program will print the (grade A+, A..etc.) of your mark")
while True:
    #promp the user to enter a number 
    grade = input("please, enter your grade : ")
    print("if you want to exit enter E")

    #checking if the input is a number
    if not grade.isnumeric() : 
        if grade == 'E':
            exit()
        else:
            print("invalid input")
        continue

    grade = int(grade)
    #checking if the input is a valid number
    if not ( 100 >= grade >= 0) :
        print("invalid input")
        continue
    #this array will lead us to the right grade for each mark to avoid doing a lot of (if else)s
    #note that those grades might be different for each college according to its rules
    grades = ['D','D','D+','C','C+','B', 'B+', 'A', 'A+', 'A+']

    if grade < 50 : 
        print('F')
    #handeling the case of 100 seperately
    elif grade == 100 : 
        print("A+")
    else :
        #this equation will get the nearest grade for each mark
        print(grades[ grade // 5 - 10])

