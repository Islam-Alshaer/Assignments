"""
File : CS112_A1_T2_1_20230062.py
purpose : A game that two players play adding numbers from 1 : 10 and the one who reaches 100 first is the winner
ID : 20230062
Author : Islam Waleed Salah AbdAlmotaleb
"""

print("Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins, have fun")


def take_input():
    valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    adding_number = input("enter a number between one and ten: ")
    
        
    if (adding_number not in valid_inputs ) or not (1 <= int(adding_number) <= 10) :
        print("enter a valid number")
        return take_input()
    else : 
        return int(adding_number)



#intializing variables to use later
current_score = 0
player_count = 1
player_count = 1


while True :
    #Minue one 
    query = input("enter one of the choices : \n A : enter the program \n B: Exit \n").upper()
    if query == "B" :
        break
    elif query != "A" :
        print("invalid input")
        continue
    else : 
        while True : 

            #to determine current player 
            if player_count % 2 == 1 :
                current_player = 1
            else :
                current_player = 2
            
            print("player" , current_player , "," , "it's your turn")

            #prompt a player to enter a number to add to the 100
            adding_number = take_input()
            
            #processing
            current_score += adding_number

            #invalid input
            if  current_score > 100 :
                print("invalid input")
                current_score -= adding_number
                continue
            elif current_score == 100 :
                #a player has won so we print
                print("player" , current_player , "has won")
                break
            #no need for else here as any other case will stop the loop
            print("current score is :" , current_score)
            player_count += 1
