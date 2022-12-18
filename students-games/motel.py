game_start = input("Would you like to play a game? y/n: ")
if game_start == 'y':
    game_begin = input(
        "You awake in a rundown motel and the door is locked from the outside, do you investigate the bathroom or the bedside table?")
else:
    print("wimp.")
if game_begin == "bathroom":
    game_riddle = input(
        "You head into the bathroom and find shards of glass from the mirror in the sink, on one of the shards is a riddle...what is black and white and read all over?")
else:
    print("You search through the bedside drawers and you come across a seemingly insignificant newspaper, and a bottle filled with mysterious liquid. You feel hopeless so you drink the entire bottle and succumb to the posion within.")
if game_riddle == "newspaper":
    game_answer = input("You search the room until you find the newspaper in the bedside drawer along with a bottle of unknown liquid. You read through the newspaper until you come across an article about how people hide their keys in their bathroom. do you check the bathtub drain or the bar of soap?")

    if game_answer == "bathtub drain":
        game_answer = print(
            "You pull the drain up to reveal a key at the end of the chain, you quickly unlock the door and rush to freedom!")
    else:
        print("You break the bar of soap open to reveal a key, you run to the door to unlock it but the key doesn't turn, feeling hopeless you give up and slump over crying your eyes out.")
