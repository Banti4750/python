cammand = ""

while cammand.lower() != "quit":
    cammand = input(">").lower()
    if cammand.lower() == "start":
        print("Car started...Ready to go!")
    elif cammand.lower() == "stop":
        print("Car stopped.")
    elif cammand.lower() == "help":
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif cammand.lower() == "quit":
        print("Exiting the game. Goodbye!")