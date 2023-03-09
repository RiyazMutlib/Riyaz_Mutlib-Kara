def encoder(digits):
   new_digits = ''
   for i in range(0, len(digits)):
      newdig = str((int(digits[i])) + 3))
      if int(digits[i]) >= 7:
          newdig = str((int(digits[i])) + 3 - 10))
      else:
          newdig = str((int(digits[i]) + 3))
      new_digits += newdig

    return newdigits
