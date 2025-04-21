height = 137
credits = 10 

validHeight = int(input("How tall are you: "))
validCredits = int(input("How many credits do you have: "))

ride = validHeight, validCredits

if validHeight >= height and validCredits >= credits:
    print ("Enjoy the ride!")

elif validHeight < height and validCredits >=credits:
    print ("You are not tall enough to ride.")

elif validHeight >= height and validCredits < 10:
     print ("You don't have enough credits.")

else:
    print ("You have not met either requirements")