char=input("Press any key :")
if(char.isalpha()):
     print("Entered value is char")
elif(char.isdigit()):
     print("Entered value is a digit")
elif(char.isspace()):
     print("Entered value is space")
else:
     print("You have entered a special character")
