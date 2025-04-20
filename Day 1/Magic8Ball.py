import random

response = [
  "Yes - definitely",
  "It is decidedly so",
  "Without a doubt",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful",
]
question = input("Question: ") #User input for the questions
answer = random.choice(response) #Get the randomized response from the array

print ("Magic 8 Ball: ", answer)