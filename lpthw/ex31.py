
prompt = '> '

print("""
You enter a dark room with two doors,
do you go through door1 or door2?
 """, end=' ')

door = input(prompt)

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(prompt)

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well doing {bear} is probably better.")
        print("The bear runs away.")
        print("1. Chase after the bear.")
        print("2. Take the leftover cheesecake")
        choice = input(prompt)
        if choice == "1":
            print("1. The bear turns around and makes you his cheesecake")
        elif choice == "2":
            print("You die of ebola -- ijekuje edition.")
        else:
            print("Wise man.")

elif door == "2":

    print("You stare into the endless abyss at cthulu's abyss.")
    print("1. Bluberries.")
    print("2. Yellow jacket clothespin.")
    print("3. Understanding quantum piano hamstrings.")

    insanity = input(prompt)

    if insanity == "1" or "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job")


else:
    print("You stumble around, fall on a knife and die. Good job!")
