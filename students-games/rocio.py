print("Welcome to the haunted house adventure game. Halloween edition")
play = input("Do you want to play? (y/n): ")
if play == "y":
    while True:
        # ask for a character name
        name1 = input("what's your name?")
        print("Hi, %s, welcome to the haunted house game" % (name1))
        # ask if would like to wake up
        play2 = input("Would you like to wake up? (y/n):")
        # end of the game
        if play2 == "n":
            print("End of the game. See you next time")
        if play2 == "y":
            print("It's 11pm, outside you can see a big fullmoon that illuminates the dark room where you are at. You can see a moody bed and a broken mirror.")
        question1 = input("Are you scared?(y/n):")
        if question1 == "y":
            print("This is only the beginning, you should be more prepared.")
        if question1 == "n":
            print("I don't see why not, I see you shaking.")
        print("it's time to keep going. You are now walking towards the hall. There you can find to doors.")
        doors = input("do you want to turn left or right?l (l/r):")
        if doors == "l":
            print("You now walk to the door left, you find yourself in a kitchen. You think you are alone, but suddenly you look at the floor and see blood. You can see a scary old granny stabbing a young girl. You really don't know what to do.")
            decision = input(
                "what should you do, run or slap her? (run/slap):")
            if decision == "slap":
                print("She caught you, you are done. She killed you.")
                print("End of the game. Hope you have more luck last time.")
            if decision == "run":
                print("she is now following you, you have to run quicker then. It's been 5 minutes running around the house. You have to make a decision.")
                final = input(
                    "Would you like to go into another room or accept that you are done? (op1/op2):")
                if final == "op2":
                    print("You chose the easy decision. End of the game.")
                if final == "op1":
                    print("You now are in an other room. Two things can happen")
                    ab = input("Do you choose option a or b? (a/b):")
                    if ab == "a":
                        print(
                            "YOU CAN'T OPEN THE ROOM, IT'S LOCKED. YOU CAN SEE THE GRANNY.")
                        print("End of the game. See you next time.")
                    if ab == "b":
                        print("You walk through the door and get into a small creepy room covered by old furniture and spiders. One minute later you find a knife, A BIG KNIFE!")
                        print(
                            "you suddenly see the granny and think twice about your decision.")
                left = input(
                    "Should you run or try to kill her with the knife? (op1/op2):")
                if left == "op2":
                    print("It is your lucky day, you should be really happy. You stab her in the heart and you find the house keys in her pocket, you are now free and can happily walk thru the door and run as fast as you know. YOU WON!")
                if left == "op1":
                    print("You run as fast as you can, you put all your effort on running but she caught! You are now unconscious. When you wake up you have the granny in front of you and you are tie on a chair.")
                    print("You actually think that everything is lost, but she offers you a game, the coins game, she tells you that if you win you will be relive and free but if you lost you will be done.")
                    print(
                        "You are kind of scared by you accept since you know you don't have another chance.")
                    print(
                        "WELCOME TO THE COINS GAME, I hope you remember the rules and accept the destiny.")

                    import random
                    # take guess
                    guess = input("head or tails h/t:")
                    # flip coin
                    flip = random.randint(0, 1)
                    # converting guess to number
                    if guess == "h":
                        guess_number = 0
                    if guess == "t":
                        guess_number = 1
                    # converting flip to words
                    if flip == 1:
                        flip_word = "tails"
                    if flip == 0:
                        flip_word = "heads"
                    if guess_number == flip:
                        # check results
                        print(
                            "it was %s you win, you can now go to your home and be relieve." % (flip_word))
                    else:
                        print(
                            "it was %s you loose, you know what's next... End of the game." % (flip_word))

        if doors == "r":
            print("You are now in the bathroom.When you walk threw the door you find blood all over the floor and the mirrors which said 'made yourself a favour and RUN'")
            choose = input(
                "You can only come up with two ideas which are, scream at her because you are scoocked or run to another room. What should you do? (op1/op2):")
            if choose == "op1":
                print("You now start yelling at her thinking it will actually work. You think it is working but suddenly she gets you and tells you 'you are done'")
                print("You actually think that everything is lost, but she offers you a game, the coins game, she tells you that if you win you will be relive and free but if you lost you will be done.")
                print(
                    "You are kind of scared by you accept since you know you don't have another chance.")
                print(
                    "WELCOME TO THE COINS GAME, I hope you remember the rules and accept the destiny.")

                import random
                # take guess
                guess = input("head or tails h/t:")
                # flip coin
                flip = random.randint(0, 1)
                # converting guess to number
                if guess == "h":
                    guess_number = 0
                if guess == "t":
                    guess_number = 1
                # converting flip to words
                if flip == 1:
                    flip_word = "tails"
                if flip == 0:
                    flip_word = "heads"
                if guess_number == flip:
                    # check results
                    print(
                        "it was %s you win, you can now go to your home and be relived." % (flip_word))
                else:
                    print(
                        "it was %s you loose, you know what's next... End of the game." % (flip_word))

            if choose == "op2":
                print("You started running and going toward a new room, that room seems the same as the other ones but it had a difference, there was a key that on it it was written '2'.")
                room = input(
                    " Should you go to room 2 or go to sleep in the bed that you can find in that bed? (op1/op2):")
                if room == "op2":
                    print(
                        "While you were sleeping the granny came into the room and quietly killed you. End of the game.")
                if room == "op1":
                    print("You go directly to room number 2, everything seems normal but suddenly you find a knife. NO WAY. WILL THIS GET YOU OUT OF THAT HOUSE?")
                    print(
                        "you suddenly see the granny and think twice about your decision.")
                    right = input(
                        "Should you run or try to kill her with the knife? (op1/op2):")
                    if right == "op2":
                        print("It is your lucky day, you should be really happy. You stab her in the heart and you find the house keys in her pocket, you are now free and can happily walk through the door and run as fast as you know. YOU WON!")
                    if right == "op1":
                        print("You run as fast as you can, you put all your effort on running but she caught! You are now unconscious. When you wake up you have the granny in front of you and you are tie on a chair.")
                        print("You actually think that everything is lost, but she offers you a game, the coins game, she tells you that if you win you will be relive and free but if you lost you will be done.")
                        print(
                            "You are kind of scared by you accept since you know you don't have another chance.")
                        print(
                            "WELCOME TO THE COINS GAME, I hope you remember the rules and accept the destiny.")

                        import random
                        # take guess
                        guess = input("head or tails h/t:")
                        # flip coin
                        flip = random.randint(0, 1)
                        # converting guess to number
                        if guess == "h":
                            guess_number = 0
                        if guess == "t":
                            guess_number = 1
                        # converting flip to words
                        if flip == 1:
                            flip_word = "tails"
                        if flip == 0:
                            flip_word = "heads"
                        if guess_number == flip:
                            # check results
                            print(
                                "it was %s you win, you can now go to your home and be relived." % (flip_word))
                        else:
                            print(
                                "it was %s you loose, you know what's next... End of the game." % (flip_word))

game_start = input("Do you want to start over? (y/n): ")
if game_start == "n":
    print("Have a good they. See you")


playagain = input("Would you like to play again?")
if playagain == "no":
    print("End of the game")
