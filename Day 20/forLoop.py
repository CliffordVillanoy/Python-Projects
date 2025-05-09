print("Example 4: Demonstrating break and continue")
for i in range(1, 10):
    if i == 5:
        print("Skipping number 5")
        continue  # Skip the rest of this loop iteration
    if i == 8:
        print("Stopping loop at number 8")
        break  # Exit the loop completely
    print(f"Number: {i}")