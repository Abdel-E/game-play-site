print("hello pilot, which jet will you be flying for today's mission? The F22 raptor or the F35 lightning")
player_pick = input("Pick a jet (F22/F35):")
if player_pick == "F22":
    print("you picked the F22 raptor")
if player_pick == "F35":
    print("you picked the F35 lightning")
print("An enemy fighter has been detected flying in allied airspace, get out there and intercept it. Its current course is towards a top secret bunker holding highly advanced nuclear weapons you must stop it no matter the cost")
safety_check = input(
    "do you wish to perform a safety check on the jet before take-off? (y/n):")
if safety_check == "n":
    print("Ending one: as you were taking off your missile cargo was dropped because of the safety check not being performed and the , you exploded and died")
if safety_check == "y":
    print("safety check was performed and everything is set, you are now flying 1000 feet above sea level approaching your target")
print("your ETA is 40 minutes at current speed, Ingage afterburners to reach target in 25 minutes")
after_burner = input("ingage afterburners (y):")
if after_burner == "y":
    print("afterburners have been engaged, exceeding mach 1. We now know what jet you are intercepting, it is a SU 27. since you are flying a 5th gen fighter taking this 4th gen fighter on should be no problem")
print("you are now approaching the target from above, wait what is this? The SU 27 is being escorted by a 5th gen SU 57 it must have stayed undetected with its stealth technology, this is going to complicate things. you should disengage the afterburners to avoid being detected")
disengage = input("would you like to disengage afterburners? (y/n):")
if disengage == "n":
    print("Ending two: you were detected by the SU 57, it fell back to your six and shot you down")
if disengage == "y":
    print("you are still undetected, continuing approach")
print("there is a chance to take out the SU 57 and then dog fight the SU 27 or you can wait for assistance from the F22 raptor that is coming to assist you")
dog_fight = input(
    "do you want to wait for assistance from the F22 raptor or do you want to attempt this on your own (wait/fight):")
if dog_fight == "fight":
    random.randint(1, 2)
if dog_fight == 1:
    print("you were lucky and successfully took out both jets before they reached the top secret nuclear lab, return to homebase")
if dog_fight == 2:
    print("Ending three: you were unsuccessful and got shot down by the enemy jets")
if dog_fight == "wait":
    print("Ending four: You fall back waiting for support but the enemy is approaching the nuclear lab and support doesn't reach you in time, the enemy bombs the lab and sets of a nuclear explosion that destroys all of north amarica")
