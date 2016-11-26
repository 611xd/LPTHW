from sys import exit
from random import randint

weapon = None

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "Maybe it's better to die in this place.",
        "She died, you died. I'm so sorry for that",
        "Fuck, that's the end. Zombie Apocalypse, human-made disaster",
        "Baby can't you see, you're dying. Oops, nah, you died."
]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class TownHall(Scene):

    def enter(self):
        print "You are the mayor of town and just woke from your nap."
        print "You raise your head up to the news on TV."
        print "You discovered that the world that you're at is no longer the same."
        print "You are inside a world of Zombie Apocalypse, the whole world is tearing apart."
        print "Suddenly there's a moan and someone knocks your door."
        print "You opened the door and see your secretary who is ready to be a mother."
        print "Help.. Mr. Eastwood! I think it's time for me to give birth..!"
        print "You decided to bring her to the hospital nearby."
        print "You have to take a weapon with you."
        print "You got a gun, a knife and a hammer, which would you choose?"

        action = raw_input("> ")

        if action == "gun":
            print "You took your gun with some extra bullet with you."
            print "Are you a smartass? You would know then. "
            weapon = "gun"
            return 'corridor_gun'

        elif action == "knife":
            print "A short knife looks simple yet sharp."
            print "Let's grab the time and go."
            weapon = "knife"
            return 'corridor'

        elif action == "hammer":
            print "It's a pretty heavy one, but it's like legit hard as fuck."
            print "Probably can break a skull with this."
            weapon = "hammer"
            return 'corridor'

        else:
            print "You just got these 3 weapons bro. Choose again please."
            return 'town_hall'

class CorridorGun(Scene):

    def enter(self):
        print "You went out from your room to your corridor."
        print "You are shock how the hallway has become, It's smelly as fuck."
        print "It's really gloomy."
        print "You see the janitor."
        print "He is staring at you and start coming at you."
        print "You take out your gun and started to shoot at him."
        print "However, the sound of gun draws all zombies attention."
        print "More and more coming at you and finally you went out of bullet."
        return 'death'

class Corridor(Scene):

    def enter(self):
        print "You went out from your room to your corridor."
        print "You are shock how the hallway has become, It's smelly as fuck."
        print "It's really gloomy."
        print "You see the janitor."
        print "He is staring at you and start coming at you."
        print "You take out your weapon and start aiming at his brain."
        print "He is killed and you move out of the building silently."
        return 'road'


class Road(Scene):

    def enter(self):
        print "You escape from the building and here is the road."
        print "You try to figure out a way for escorting them safely."
        print "You saw your car was destroyed but you saw Mark's car is perfectly parked beside you."
        print "There's also a huge food truck."
        print "As well as a motorbike with keys attached."

        action = raw_input("> ")

        if action == "car":
            print "You decided to steal Mark's car, coz he really is an asshole lol"
            print "But well once you open the door he came at you..."
            print "It's too late, you neglected the possibility that he is a zombie inside the car."
            return 'death'

        elif action == "food truck":
            print "You entered the food truck."
            print "It's pretty safe inside as it's high up and it crashes every zombie coming on your way."
            print "But be minded that there's a pregnant lady beside you, it's urgent."
            return 'hospital'

        elif action == "motorbike":
            print "It kinda difficult to drive this shit, it's been a long time."
            print "It's really a good one tho, it's super fast."
            print "You arrive at the hospital within minutes."
            return 'hospital'

        else:
            print "Fuck you it's in a hurry. Please choose it properly."
            return 'road'


class Hospital(Scene):

    def enter(self):
        print "Finally here comes the hospital, you rush inside."
        print "You entered the elevator."
        print "3rd floor: Hospital Dean Office"
        print "2nd floor: ICU"
        print "1st floor: the ER"

        action = raw_input("> ")

        if action == "1":
            print "The elevator door opened and tons of zombies are waiting for you there."
            return 'death'

        elif action == "2":
            print "There's no one on the corridor."
            print "You glanced at every room possible. You then saw a doctor's back."
            print "You rushed into the room and the doctor turned around."
            print "You quickly escape and run back to the elevator."
            return 'hospital'

        elif action == "3":
            print "You step out of the elevator and rush to the dean's office."
            return 'deans_office'

        else:
            print "Please choose one floor that is actually exist"
            return 'hospital'

class DeansOffice(Scene):

    def enter(self):
        print "You arrived at the Dean's office."
        print "The door is locked."
        print "However, the dean is a fucking coward, he doesn't want to open the door."
        print "Your secretary starts having a labor, she is screaming in huge pain."
        print "You could either break the door with your weapon and beg for the dean's help"
        print "or just deliver the baby right here."
        print "or what?! you want to leave them alone and leave...?!"

        action = raw_input("> ")

        if action == "break the door":
            print "He shot you with the gun and thought that you both are infected."
            return 'death'

        elif action == "deliver the baby":
            print "You made a great decision, it is successful."
            print "It's a baby boy and the dean saw it and allowed you to get inside to his office."
            print "You guys should start planning what to do next."
            print "See you in the next episode."
            exit(1)

        elif action == "leave them alone":
            print "You human trash, but you made your way through and got out of the hospital."
            print "See you in the next episode."
            exit(1)

        else:
            print "Theres no time left, please decide."
            return 'deans_office'



class Map(object):

    scenes = {
        'town_hall': TownHall(),
        'corridor_gun': CorridorGun(),
        'corridor': Corridor(),
        'hospital': Hospital(),
        'road' : Road(),
        'deans_office': DeansOffice(),
        'death': Death()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('town_hall')
a_game = Engine(a_map)
a_game.play()
