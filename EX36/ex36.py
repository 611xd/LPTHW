from sys import exit



def unicorn_zone():
    print "Your pony have brought you to the kingdom of the unicorn! \n a unicorn guard offer you 2 choices for the welcoming gift, A candy cone or A unicorn poop. \n Which would you choose? "

    choice = raw_input("> ")
    if "candy cone" in choice:
        print "You are dead from poison, Rest in Peace man. :P"
        exit(0)
    elif "unicorn poop" in choice:
        print "The unicorn guard asked, 'It would be great if you eat this!'"
        print "Are you going to eat the unicorn poop. Yes or No."
        choice = raw_input("> ")
        if "yes" in choice:
            print "Yay! Congratulations! You have gained the trust from unicorns and became a permanent residence of the unicorn zone!"
            exit(0)
        elif "no" in choice:
            print "You gave up the chance to be a residence of unicorn zone but you could still travel around the zone like a tourist :)"
            exit(0)
        else:
            print "What the fuck are you talking about? Wrong channel bye"
            exit(0)
    else:
        print "What the fuck are you talking about? Wrong channel bye"
        exit(0)



def skettles_land():
    print "Welcome to the land full of skettles, there are 2 bottons on the door gate. Please choose one of them."
    print "Rainbow or Brown button."

    choice = raw_input("> ")
    if  "rainbow" in choice:
        print "You became the slave in the Skettlesland. Congraz ^__^"
        exit(0)
    elif "brown" in choice:
        print "You got unlimited Skettles for the rest of your life! Congraz ^_____^~!!!!!"
        exit(0)
    else:
         print "Stop talking bullshit man. Get outta here."
         exit(0)



def castle_in_the_sky():
    print "Howl the handsome wizard loved you at the first sight and proposed to you immediately. You lucky bastard! "
    print "I won't offer you choices to reject him coz you shouldn't be. hahahahahahahaha"
    exit(0)


def underworld():
    print "Oops, you unlucky piece of shit, got eaten by the whale. \n you forgot to take a look before choosing it, it's a fucking killer whale LOL"
    exit(0)

def start():
    print "You joined the adventure time league."
    print "You can choose Pony, Hawk, Whale or Skateboard as your transportation."
    print "Your adventure starts........ NOW!!!"

    choice = raw_input("> ")

    if choice == "pony":
        unicorn_zone()
    elif choice == "hawk":
        castle_in_the_sky()
    elif choice == "whale":
        underworld()
    elif choice == "skateboard":
        skettles_land()
    else:
        print "You fucking LOSER. BYE FOREVER."
        exit(0)


start()
