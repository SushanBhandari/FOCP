def password_checker(password):
  from string import ascii_letters as letters, digits, punctuation
  has_letter = has_digit = has_punc = False
  for character in password:
    if character in letters:
      has_letter = True
    elif character in digits:
      has_digit = True
    elif character in punctuation:
      has_punc = True
  return has_letter and has_digit and has_punc


password = input("Enter a password: ")


if password_checker(password):
  print("The password is acceptable.")
else:
  print("The password is not acceptable.")
