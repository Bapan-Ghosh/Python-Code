pan = input("Enter the PAN card no: ")

if len(pan) == 10 and pan[0:5].isalpha() and pan[0:5].isupper() and pan[5:9].isdecimal() and pan[9].isupper():

          print("It's a Valid PAN card")

else:

          print("It's an Invalid PAN card")
