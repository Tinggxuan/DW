from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world

class MySMClass(sm.SM):
    start_state=None
    
    def get_state(self, inp):
        ground = inp.prox_ground.delta
        if ground[0] < 200 and ground[1] < 200:
            return "black"
        elif ground[0] > 200 and ground[1] < 200:
            return "aligned"
        else:
            return "white"
        
    def get_next_values(self, state, inp):
        # These two lines is to stop the robot
        # by pressing the backward button.
        # This only works when using the real robot.
        # It will not work in simulator.
        if inp.button_backward:
            return 'halt', io.Action(0,0)
        #####################################
        next_state = self.get_state(inp)
        if state == None:
            return self.get_state(inp), io.Action(fv=0.1, rv=0.0)
        elif state == "black":
            if next_state == state:
                return next_state, io.Action(fv=0.1, rv=0.0)
            else:
                return "align-right", io.Action(fv=0.0, rv=-0.2)
        elif state == "white":
            if next_state == state:
                return next_state, io.Action(fv=0.1, rv=0.0)
            else:
                return "align-left", io.Action(fv=0.0, rv=0.2)
        elif state == "align-left":
            if next_state == "aligned":
                return next_state, io.Action(fv=0.1, rv=0.0)
            else:
                return state, io.Action(fv=0.0, rv=0.2)
        elif state == "align-right":
            if next_state == "aligned":
                return next_state, io.Action(fv=0.1, rv=0.0)
            else:
                return state, io.Action(fv=0.0, rv=-0.2)
        elif state == "aligned":
            if next_state == "black":
                return "align-left", io.Action(fv=0.0, rv=0.2)
            elif next_state == "white":
                return "align-right", io.Action(fv=0.0, rv=-0.2)
            else:
                return state, io.Action(fv=0.1, rv=0.0)

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################


            
    def done(self,state):
        if state=='halt':
            return True
        else:
            return False

MySM=MySMClass()

############################

m=ThymioSMReal(MySM)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
