validPin = 1234
pin = None

while pin != validPin:
  try:
    pin = int(input('Enter your PIN: '))

  except:
    print ('Incorrect PIN. Enter your PIN again: ')
    continue

  if pin != validPin:
    print ('Incorrect PIN. Enter your PIN again: ')

print ('PIN accepted')
