# Alya Mohammed Al-Hababi 20230800
# Jana Hasan Ali 20230106
# Salah Hamad Salah Mohammed 20230194

def input_number_to_decimal(number, base):
    """
    Convert a number from a given base to decimal.
    """
    decimal_number = 0
    number = str(number).upper()
    digits = "0123456789ABCDEF"

    for digit in number:
        decimal_number = decimal_number * base + digits.index(digit)

    return decimal_number

def decimal_to_output_number(number, base):
    """
    Convert a decimal number to a given base.
    """
    digits = "0123456789ABCDEF"
    if number == 0:
        return '0'

    converted_number = ''
    while number > 0:
        converted_number = digits[number % base] + converted_number
        number //= base

    return converted_number

def main_menu():
    while True:
        print("** Numbering System Converter **")
        print("A) Insert a new number")
        print("B) Exit program")
        choice = input("Enter your choice: ").strip().upper()

        if choice == 'A':
            number = input("Please insert a number: ").strip()
            from_base = base_menu("from")
            to_base = base_menu("to")
            decimal_number = input_number_to_decimal(number, from_base)
            converted_number = decimal_to_output_number(decimal_number, to_base)
            print(f"Converted number: {converted_number}")
        elif choice == 'B':
            print("Exiting the program.")
            break
        else:
            print("Please select a valid choice.")

def base_menu(direction):
    while True:
        print(f"** Please select the base you want to convert a number {direction} **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")
        choice = input("Enter your choice: ").strip().upper()

        base_dict = {'A': 10, 'B': 2, 'C': 8, 'D': 16}
        if choice in base_dict:
            return base_dict[choice]
        else:
            print("Please select a valid choice.")
#start the main menu:
main_menu()

