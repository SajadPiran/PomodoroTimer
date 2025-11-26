from interfaces.states.context import Context
from interfaces.states.state import State
from services.setting.setting import Setting

class IntervalContext(Context) :

    def __init__(self , state : State , setting : Setting) :
        super().__init__(state, setting)

