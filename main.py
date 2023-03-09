def encoder(digits):
   new_digits = ''
   new_dig =''
   for i in range(0, len(digits)):
      if int(digits[i]) >= 7:
          newdig = str((int(digits[i])) + 3 - 10)
      else:
          newdig = str((int(digits[i]) + 3))
      new_digits += newdig

    return newdigits


if __name__ == "__main__":
    menu = True
    while menu:
        password = 0
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input("Please enter your password to encode: ")
            if len(password) != 8:
                print('Please enter an 8 digit password.')
            if len(password) == 8:
                password = int(password)
                # run the encoder function: new_pass = encoder(password)
                # have a variable like encoded_pass exist
                print("Your password has been encoded an stored!")
        elif option == 2:
            if password == 0:
                print("Please encode a password first.")
            # use a decode function to print the statement or just use the print statement
            # print(f"The encoded password is {encoded_pass}, and the original password is {password}.")
        elif option == 3:
            menu = False
        else:
            print("Please enter a valid option.")
