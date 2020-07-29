from random import randint
from time import perf_counter

"""An automated light bulb mechanism applying FSM principles"""


##================================
#State = type("State", (object,), {})
class State(object):
    def enter(self):
        print("not defined")
        pass

class LightOn(State):
    def execute(self):
        print('light is on!')

class LightOff(State):
    def execute(self):
        print('light is off!')
##================================

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print("Transitioning")

##================================


class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def setState(self, stateName):
        self.curState = self.states[stateName]

    def transition(self, transName):
        self.trans = self.transitions[transName]

    def execute(self):
        if self.trans:
            self.trans.execute()
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.execute()

##================================

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True


##================================

if __name__ == "__main__":
    light = Char()

    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["toOn"] = Transition("On")
    light.FSM.transitions["toOff"] = Transition("Off")


    light.FSM.setState("On")

    for i in range(20):
        startTime = perf_counter()
        timeInterval = 1
        while startTime + timeInterval > perf_counter():
            pass
        if randint(0, 2):
            if light.LightOn:
                light.FSM.transition("toOff")
                light.LightOn = False
            else:
                light.FSM.transition("toOn")
                light.LightOn = True
        light.FSM.execute()
