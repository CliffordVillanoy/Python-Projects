def while_loop_example():
  i = 0
  while i < 5:
    i += 1
    print(i)
# Output: 1 2 3 4 5

# The while loop continues until i is no longer less than 5.
# The loop increments i by 1 in each iteration and prints its value.      
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Output: 1 2 4 5 6
# The continue statement skips the current iteration of the loop when i is 3.         