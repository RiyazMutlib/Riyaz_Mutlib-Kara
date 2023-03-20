
def encoder(digits): #subtracts 3 or adds 7 to each digit of the input and returns an encoded password
    new_digits = ''
    new_dig = ''
    for i in range(0, len(digits)):
        if int(digits[i]) >= 7:
            new_dig = str(int(digits[i]) - 7)
        else:
            new_dig = str(int(digits[i]) + 3)
        new_digits = new_digits + new_dig
    return new_digits

def decoder(digits): #subtracts 3 or adds 7 to each digit of the input and returns the decoded password
    new_digits = ''
    new_dig = ''
    for i in range(0, len(digits)):
        if int(digits[i]) <= 2:
            new_dig = str(int(digits[i]) + 7)
        else:
            new_dig = str(int(digits[i]) - 3)
        new_digits = new_digits + new_dig
    return new_digits

def main():
    menu = True
    while menu: #loop till user selects option 3
        password = ''
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = int(input('Please enter an option: '))
        if option == 1: #encodes password if option == 1
            password = input("Please enter your password to encode: ")
            if len(password) != 8:
                print('Please enter an 8 digit password.')
            if len(password) == 8:
                encoded_password = encoder(password)
                print("Your password has been encoded an stored!\n")
        elif option == 2: #decodes password and prints encoded and original password
            if len(encoded_password) == 8:
                decoded_password = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("Please encode a password first.")
        elif option == 3:
            menu = False
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()