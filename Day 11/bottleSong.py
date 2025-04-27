for bottles in range(99, 0, -1):
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
        if bottles - 1 == 1:
            print(f"1 bottle of beer on the wall\n")
        else:
            print(f"{bottles - 1} bottles of beer on the wall\n")
    else:
        print("1 bottle of beer on the wall")
        print("1 bottle of beer")
        print("Take one down, pass it around")
        print("No more bottles of beer on the wall!\n")
