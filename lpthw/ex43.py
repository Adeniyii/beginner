"""Gothons from planet percal #25"""

"""

Aliens have invaded a spaceship and our hero has to go through a maze of rooms
defeating them so he can get to an escape pod and escape to a planet below.
The game will be like a zork/adventure type with text outputs and funny
ways to die. The game will involve an engine that runs a map full of rooms
os scenes. Each room will print it's description when the player enters it and
then tell the engine what room to run next out of the map.

scenes and descriptions

1 death -- This is when the player dies and should be something funny.
2 central corridor -- This is the starting point and already has a gothon there
which the player has to defeat with a joke before continuing.
3 laser weapon armory -- this is where the hero gets a neutron bomb to blow up
the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
4 the bridge -- this is another battle scene with a gothon where the hero places the bomb.
5 escape pod -- this is where the hero excapes but only after guessing the right escape pod.

list of nouns

Aliens
spaceship
hero
escape pod
scenes
rooms
central corridor
laser weapon armory
bridge
gothon
bomb
planet
maze
engine
map
death


List of verbs

1 Run - engine
2 get - scene
3 enter - scene
4


Create a class hierarchy and object map for the concepts.

nouns are *
verbs are -

* Map
 - next scene
 - opening scene
* Engine
 - play
* Scene
 - enter
    * Death
    * Central corridor
    * Laser weapon armory
    * The bridge
    * Escape pod

"""
# import your shit
from sys import exit
from random import randint
from textwrap import dedent


# create a scene class
class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Sub-class it and implement enter().")
        exit(1)


# create an engine to play the game
class Engine(object):
    # define an init function that collects a scene_map attribute

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # create a function to play the game.
    def play(self):
        # call the opening_scene function on the given scene map
        # and store as current_scene variable
        # self.scene map represents an instance of the map class
        current_scene = self.scene_map.opening_scene()
        # call the next_scene function on the given scene map
        # and store as last_scene variable
        last_scene = self.scene_map.next_scene('finished')
        # while the current scene is not the last scene, run while loop
        while current_scene != last_scene:

            # enter the current scene and
            #store the return string as the next scene name.
            next_scene_name = current_scene.enter()
            # change the current scene to the returned scene name
            # from the next scene name variable.
            current_scene = self.scene_map.next_scene(next_scene_name)
        # run the last scene when the current scene is the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
    "You died. You kinda suck at this.",
    "Your president would be proud.. if he were smarter.",
    "Such a face-butt.",
    "I have a small puppy that's better at this",
    "You're worse than deji's jokes."
    ]
    def enter(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)



class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
                The gothons of planet percal #25 have invaded your ship and
                destroyed your entire crew. You are the last surviving member
                and your mission is to get the neutron destruct bomb from the
                weapons armory, put it in the bridge, and blow up the ship after
                getting into an escape pod. You're running down the central
                corridor to the weapons armory when a gothon jumps out.
                Red scaly skin, dark grimy teeth and evil clown costume flowing
                around his hate filled body. He's blocking the way to the armory
                about to pull a weapon to blast you.
        """))
        action = input("> ")
        if action == "shoot":
            print(dedent("""
                Quick on the draw, you yank out your blaster and fire it at the
                gothon. His clown costume is flowing around his body, which throws
                off your aim. Your laser hits his costume but misses him entirely
                This completely ruins his brand new costume his mother got him,
                which causes him to fly into an insane rage and blast you
                repeatedly in the face until you are very dead. Then he eats you.

            """))
            return 'death'
        elif action == "dodge":
            print(dedent("""
                Like a world class boxer you dodge,	weave, slip	and slide right
                as the gothon's laser cracks a laser past your head. In the
                middle of your artful dodge, your foot slips and you bang your
                head on the metal wall and pass out. You wake up shortly after
                only to die as the gothon stomps on your head and eats you.
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                Luckily, you were forced to learn gothon insults in the academy.
                You tell the one gothon joke you know: iunv jdnuc jhfubch fur
                fjjr jkiuu jfhuv uyy rjhv jhbf jhhv, jhu hvbuy wuye znzmlv nfj.
                The gothon stops, tries not to laugh, then bursts out laughing
                and can't move. While he's laughing, you run up and shoot him
                square in the face, then jump through the weapons armory door.
            """))
            return "laser_weapon_armory"
        else:
            print("Does not compute!")
            return 'central_corridor'



class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
            You do a dive roll into the weapons armory, crouch and scan the room
            for more gothons that might be hiding. It's dead quiet, too quiet.
            You stand and run to the far side of the room and find the neutron
            bomb in it's container. There's a keypad code on the box and you need
            the code to get the bomb out of the box. If you get the code wrong
            ten times, the lock closes forever and you can't get the bomb.
            The code is 3-digits.
        """))
        code = f"{randint(0,1)}{randint(1,2)}{randint(2,3)}"
        guess = input("[KEYPAD]> ")
        guess_count = 0
        while guess != code and guess_count < 10:
            print("BZZZDDDD")
            guess_count += 1
            guess = input("[KEYPAD]> ")
        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting out gas.
                You grab the neutron bomb and run as fast as you can to the bridge
                where you must place it correctly.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening
                melting sound as the mechanism is fused together. You decide to
                sit there, and finally the gothons blow up the ship and you die.
            """))
            return 'death'



class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            You burst onto the bridge with the neutron destruct bomb under your
            arm and surprise 5 gothons who are trying to take control of the ship.
            Each of them has an even uglier clown costume than the last. They
            haven't pulled their weapons out yet, as they see the active bomb
            under your arm and don't want to set it off.
        """))
        action = input("> ")
        if input == "throw the bomb!":
            print(dedent("""
                You throw the bomb.
            """))
            return 'death'
        elif action == 'slowly place the bomb':
            print(dedent("""
                You sucessfully place the bomb.
            """))
            return 'escape_pod'
        else:
            print(dedent("""Does not compute"""))
            return 'the_bridge'



class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            You rush to the ship and have to guess one pod.
        """))
        good_pod = randint(1,5)
        guess = input("POD[#]> ")
        if int(guess) != good_pod:
            print(dedent("You fake brah"))
            return 'death'
        else:
            print(dedent("""WE MOVE!"""))
            return 'finished'



class Finished(Scene):
    def enter(self):
        print("You won. Good job!")
        return 'finished'


class Map():

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    # function to get the scene function from the scenes dictionary.
    # this function allows the coder to pick scenes from any point in the
    # scene map.
    def next_scene(self, scene_name):
        self.scene_name = scene_name
        val = self.scenes.get(self.scene_name)
        # return the scene function
        return val
    # function to give the start scene key to the nextscene function
    # and return the function from the scenes dictionary.
    # this function basically returns just the value of the key given as the
    # init function attribute. i.e the opening scene in this case.
    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()
