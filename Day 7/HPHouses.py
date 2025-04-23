gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

answer = int(input("Enter your choice: "))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print ("Wrong input")

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer = int(input("Enter your choice: "))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print ("Wrong input")

print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer = int(input("Enter your choice: "))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print ("Wrong input")

print ("\nScore: ")
print ("Gryffindor: ", gryffindor)
print ("Ravenclaw: ", ravenclaw)
print ("Hufflepuff: ", hufflepuff)
print ("Slytherin: ", slytherin)


maxScore = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print ("\nFinal Score: ")
if gryffindor == maxScore:
  print ("Welcome to Gryffindor")
elif ravenclaw == maxScore:
  print ("Welcome to Ravenclaw")
elif hufflepuff == maxScore:
  print ("Welcome to Hufflepuff")
elif slytherrin == maxScore:
  print ("Welcome to Slytherin)")
else:
  print ("You are not a wizard")
# The code above is a simple quiz that determines which Hogwarts house a user belongs to based on their answers to a series of questions.