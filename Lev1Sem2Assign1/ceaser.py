#describe the game to the user
print("Welcome to the Ceaser game, where the ceaser enters a message and encrypt it")
print("the \"key\" is the number of letter shift the ceaser wants to encrypt using it")
print("as letter a converts to letter c using key of 2 for example")

#promp the user to enter the text
message = input("Enter the text ceaser wants to encrypt: ")
key = input("Enter the key to encrypt: ")

#making sure key is an integer
while not key.isnumeric():
    key = input("Enter the key to encrypt: ")
key = int(key)

output = ""
#encrypting
for ch in message :
    #maximum and minimum values are used to deal with letters that will exceed z
    if ch.islower() :
        mx_value = ord('z')
        mn_value = ord('a')
    elif ch.isupper() :
        mx_value = ord('Z')
        mn_value = ord('A')

    if ch.isalpha():
        #if the letter does not exceed z after adding the encrypting key
        if ord(ch) + key <= mx_value:
            output += chr(ord(ch) + key)
        #if it does we return it to the beggining using % operator and then adding the min value
        else:
            output += chr( (ord(ch) + key) % mx_value + mn_value - 1)

    else:
        output += ch

#printing
print(output)