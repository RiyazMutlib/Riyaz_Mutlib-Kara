def encoder(digits):
   new_digits = ''
    for i in range(0, len(digits)):
      newdig = str((int(digit[i)) + 3))
      if int(digit[i]) >= 7:
            newdig = str((int(digit[i)) + 3 - 10))
      else:
            newdig = str((int(digit[i)) + 3))
      new_digits += newdig
