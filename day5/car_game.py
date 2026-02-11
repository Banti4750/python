cammand = ""

while cammand.lower() != "quit":
    cammand = input(">").lower()
    if cammand == "start":
        print("Car started...Ready to go!")
    elif cammand == "stop":
        print("Car stopped.")
    elif cammand == "help":
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif cammand == "quit":
        print("Exiting the game. Goodbye!")