# Alya Mohammed Al-hababi 20230800
# Jana Hassan Ali 20230106
# Salah Hammad Salah Mohammed 20230194

def fill_zero(bin1, length):
    # Prepend zeros to a binary number until it reaches the specified length
    return '0' * (length - len(bin1)) + bin1

def is_valid_binary(number):
    # Check if a string consists only of binary digits (0 and 1)
    for char in number:
        if char not in['0', '1']:
            return False
    return True

def maximum(n1, n2):
    # Return the maximum of two numbers
    m = n1
    if n2>m:
        m = n2
    return m

def add_binary(bin1, bin2):
    # Add two binary numbers
    max_len = maximum(len(bin1), len(bin2))  # Find the maximum length of the two binary numbers
    bin1 = fill_zero(bin1, max_len)          # Fill with zeros to make both numbers equal in length
    bin2 = fill_zero(bin2, max_len)
    result = ''                             # Variable to store the result of addition
    carry = 0                               # Variable to store the carry during addition

    # Iterate over each bit, adding them along with the carry
    for i in range(max_len - 1, -1, -1):
        r = carry
        if bin1[i] == '1':
            r+=1
        if bin2[i] == '1':
            r+=1
        if r % 2 == 1:
            result = '1'+result
        else:
            result = '0'+result
        if r < 2:
            carry = 0
        else:
            carry = 1

    if not (carry == 0):
        result = '1' + result

    return fill_zero(result, max_len) # Fill zeros to the final result

def subtract_binary(bin1, bin2):
    result = add_binary(bin1, twos_complement(bin2))
    if len(result) > len(bin1):
        result = result[1:]
    return result

def ones_complement(bin1):
    # Calculate the one's complement of a binary number
    result = ""
    for x in bin1:
        if x == '0':
            result += '1'
        else:
            result += '0'
    return result

def twos_complement(bin1):
    # Calculate the two's complement of a binary number
    return add_binary(ones_complement(bin1), '1')



def main_menu():
    # Main loop for user interaction
    while True:
        # Display the main menu options
        print("\n"+"="*30)
        print("   ** Binary Calculator **")
        print("="*30)
        print("\n"+"-"*30)
        print(" A) Insert new numbers")
        print(" B) Exit")
        print("-"*30)

        # Get the user's choice
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            # If the user chooses to insert numbers
            bin1 = input("Enter the first binary number: ")

            # Validate the first binary number
            while not is_valid_binary(bin1):
                bin1 = input("Please insert a valid binary number: ")

            while True:
                # Display the operations menu
                print("\n"+"="*30)
                print("      ** Operations **")
                print("="*30)
                print("\n"+"-"*30)
                print("A) Compute one's complement")
                print("B) Compute two's complement")
                print("C) Addition")
                print("D) Subtraction")
                print("-"*30)

                # Get the user's choice of operation
                operation = input("Enter your choice: ").upper()
                # Validate the choice
                if operation in ['A','B','C','D'] :
                    break
                else:
                    print("operation not valid")

            if operation == 'A':
                # Perform one's complement operation
                print("One's Complement:", ones_complement(bin1))
            elif operation == 'B':
                # Perform two's complement operation
                print("Two's Complement:", twos_complement(bin1))
            elif operation in ['C', 'D']:
                # If the user chooses addition or subtraction
                bin2 = input("Please insert the second number: ")
                while not is_valid_binary(bin2):
                    bin2 = input("Please insert a valid binary number: ")

                if operation == 'C':
                    # Perform addition operation
                    print("Addition Result:", add_binary(bin1, bin2))
                elif operation == 'D':
                    # Perform subtraction operation
                    print("Subtraction Result:", subtract_binary(bin1, bin2))

        elif choice == 'B':
            # If the user chooses to exit
            print("   ---- Exiting the program ----")
            break
        else:
            # If the user enters an invalid choice
            print("Please select a valid choice.")
# Start the main menu
main_menu()
