""" Custom game using a Finite State Machine."""

from sys import exit
from textwrap import dedent
from random import randint

prompt = '> '


# Create a Room() base-class
class Room(object):
    def enter(self):
        print("This is the room baseclass.")
        print("Subclass is and move on.")
        pass


# An Engine() class to control changing and executing room scenes.
class Engine(object):
    # init method To collect map(s) as class() attributes..
    def __init__(self, room_map, dream_map):
        self.room_map = room_map
        self.dream_map = dream_map

    # method to control running and changing of rooms in given map(s).
    def play_room(self):
        # To collect the MasterBedroom() class as the current_room variable.
        current_room = self.room_map.opening_room()
        # To collect Outside() class as the last_room variable.
        last_room = self.room_map.closing_room()

        # To run block of code while the last room has not been called.
        while current_room != last_room:
            # To execute the current room and return the next room key into...
            # ...a next_room_name variable.
            next_room_name = current_room.enter()
            # collect the class value of the returned next room key as the current room.
            current_room = self.room_map.next_room(next_room_name)
        # To execute the last room after the while loop exits.
        current_room.enter()

    # method to control running and changing of dreams in given map(s)
    def play_dream(self):

        current_dream = self.dream_map.opening_dream()
        last_dream = self.dream_map.closing_dream()

        while current_dream != last_dream:
            next_dream_name = current_dream.enter()
            current_dream = self.dream_map.next_dream(next_dream_name)
        current_dream.enter()



# Sub-class of Room()
class MasterBedroom(Room):
    def enter(self):
        print(dedent("""
            Pass me the kpo,
            pass me the cho,
            pass me the ting wey dey make me go,
            pass me the codine make me slow,
            pass me the kpo kpo di kpo.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                return 'bathroom'
            elif ans == 'right':
                return 'living_room'
            elif ans == 'forward':
                print("You run into a wall.")
            elif ans == 'backward':
                print("You decide to go back to bed.")
                return 'dream'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class LivingRoom(Room):
    def enter(self):
        print(dedent("""
            For instance,
            say i be the one wey dey make plans,
            say i be the one wey dey give chance,
            wey make the people disappear,
            and to make them reappear.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                print("You run into a wall.")
            elif ans == 'right':
                return 'balcony'
            elif ans == 'forward':
                return 'dining_room'
            elif ans == 'backward':
                return 'master_bedroom'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class Kitchen(Room):
    def enter(self):
        print(dedent("""
            When i look into your eyes
            all i see is designer
            gucci, dolce and gabanna
            you got me going bannanas.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                print("You run into a wall.")
            elif ans == 'right':
                return 'outside'
            elif ans == 'forward':
                print("you run into a wall.")
            elif ans == 'backward':
                return 'dining_room'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class Balcony(object):
    def enter(self):
        print(dedent("""
            I'm in chains,
            you're in chains too.
            I wear uniforms and,
            you wear uniforms too.
            I'm a prisoner,
            You're a prisoner too.
            Mr. Jailer.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                print("You run into a wall.")
            elif ans == 'right':
                print("You run into a wall.")
            elif ans == 'forward':
                return 'outside'
            elif ans == 'backward':
                return 'living_room'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class DiningRoom(Room):
    def enter(self):
        print(dedent("""
            Ni Ojuelegba ooo,
            me and sinzu,
            for hold up studio,
            we dey hustle to chop.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                return 'kitchen'
            elif ans == 'right':
                return 'second_room'
            elif ans == 'forward':
                print("You run into a wall.")
            elif ans == 'backward':
                return 'living_room'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class Bathroom(Room):
    def enter(self):
        print(dedent("""
            Shower, shower, shower le,
            shower, shower shower le.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                print("You run into a wall.")
            elif ans == 'right':
                return 'master_bedroom'
            elif ans == 'forward':
                return 'living_room'
            elif ans == 'backward':
                return 'bathroom'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class SecondRoom(Room):
    def enter(self):
        print(dedent("""
            Folake, anything for me,
            Lagbaja nothing for you.
            Mo ni, bisi anything for me,
            Lagbaja nothing for you.
        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                return 'second_bathroom'
            elif ans == 'right':
                print("You ran into a wall.")
            elif ans == 'forward':
                return 'dream'
            elif ans == 'backward':
                return 'dining_room'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class SecondBathroom(Room):
    def enter(self):
        print(dedent("""

        """))
        while True:
            ans = input(f"Choose next your destination\n {prompt}")
            if ans == 'left':
                return 'second_room'
            elif ans == 'right':
                return 'dining_room'
            elif ans == 'forward':
                print("You ran into a wall.")
            elif ans == 'backward':
                return 'second_bathroom'
            else:
                print("Invalid entry.")


# Sub-class of Room()
class Outside(Room):
    def enter(self):
        print(dedent("""
            Better not get confused outside,
            you go lose outside,
            so watch how you move outside.
            You no go know if you no go,
            No try reap what you no sow.
        """))

        return 'finished'


# Sub-class of Room()
class Finished(Room):
    def enter(self):
        print(dedent("""
            OluwaBurna!!!
        """))
        while True:
            ans = input(f"Would you like to play again?\n {prompt}")
            # condition to run reinitialize the program.
            if ans == 'yes' or ans == 'y':
                a_map = Map('master_bedroom', 'finished')
                a_game = Engine(a_map, d_map)
                a_game.play_room()
            elif ans == 'no' or ans == 'n':
                # To exit program.
                return exit(1)
            else:
                pass

# Dream() base-class to initialize a different method of Engine() class to run a different map.
class Dream(object):
    def enter(self):
        print(dedent("""
            We enter into the world where lobsters are lords,
            and humans are subjects.
        """))

        # code to initialize a new engine functionality to run the dream map.
        d_map = Map('astroworld', 'wake_up')
        a_game = Engine(a_map, d_map)
        a_game.play_dream()


# Sub-class of Room()
class Astroworld(Room):
    def enter(self):
        print(dedent("""
            LET'S GO!
            We see the hype outside,
            right from the house,
            took it straight from outside,
            straight to the couch,
            we put the mic outside,
            air this shit out.
        """))

        while True:
            ans = input(f"Enter artist name to advance\n {prompt}")
            if ans.lower() == 'travis':
                return 'neverland'
            elif ans == 

            else:
                print("Invalid entry.")


class Neverland(Room):
    def enter(self):
        print(dedent("""
            I heard you got too lit last night,
            did you make it home.
            Mixing purple with your dirty sprite,
            things you shouldn't know.
        """))
        return 'ashina_depths'


class AshinaDepths(Room):
    def enter(self):
        print(dedent("""
            The shinobi of sakura town will now see you.
            Lady butterfly leads you through a horde of undead samurai,
            you finally meet with prince cudi and lord kanye under the canopy.
        """))
        return 'cloud9'


class Cloud9(Room):
    def enter(self):
        print(dedent("""
            cudi hands you a blunt and
            tells you to present it to the tunchi statue for prayers.
            Your vision starts to blur as you get closer to the statue.
            You wake up in a white room with no walls and piano Trap bumping.
            Right before you pass out again, you glimpse kanye and tunechi vibing.
            As burna joins them for tea.
        """))
        return 'wake_up'



class WakeUp(Room):
    def enter(self):
        return exit(1)


# map base-class containing all maps,
# and functions to call scenes within the maps.
class Map(object):
    # room map containing room key mapped to room value as Room() sub-classes.
    rooms = {
        'master_bedroom': MasterBedroom(),
        'living_room': LivingRoom(),
        'kitchen': Kitchen(),
        'balcony': Balcony(),
        'dining_room': DiningRoom(),
        'bathroom': Bathroom(),
        'second_room': SecondRoom(),
        'second_bathroom': SecondBathroom(),
        'outside': Outside(),
        'finished': Finished(),
        'dream': Dream()
    }

    # dream map containing dream key mapped to dream value as Room() sub-classes.
    dreams = {
        'astroworld': Astroworld(),
        'neverland': Neverland(),
        'ashina_depths': AshinaDepths(),
        'cloud9': Cloud9(),
        'wake_up': WakeUp()
    }


    # init method to collect first room and last room as class attributes.
    def __init__(self, start_room, end_room):
        self.start_room = start_room
        self.end_room = end_room

    # method to collect room dict key as attribute and return mapped Room() sub-class.
    def next_room(self, room_name):
        val = self.rooms.get(room_name)
        return val

    # method to return the first room's mapped Room() subclass using the next_room() method.
    def opening_room(self):
        return self.next_room(self.start_room)

    # method to return the last room's mapped Room() subclass using the next_room() method.
    def closing_room(self):
        return self.next_room(self.end_room)
##=============================================
    # method to collect dream dict key as attribute and return mapped Room() sub-class.
    # this mrthod allows you to pick any key and call the corresponding class() value.
    def next_dream(self, dream_name):
        val = self.dreams.get(dream_name)
        return val

    # method to return the first dream's mapped Room() subclass using the next_dream() method.
    def opening_dream(self):
        return self.next_dream(self.start_room)

    # method to return the last dream's mapped Room() subclass using the next_dream() method.
    def closing_dream(self):
        return self.next_dream(self.end_room)



a_map = Map('master_bedroom', 'finished')
d_map = Map('astroworld', 'wake_up')
a_game = Engine(a_map, d_map)
a_game.play_room()
