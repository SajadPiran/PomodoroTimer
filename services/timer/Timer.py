import threading
from interfaces.states.context import Context
from services.interval_context.interval_context import IntervalContext
from services.interval_context.states.focus import Focus
from services.setting.setting import Setting

class Timer :

    def __init__(self , context : Context) :
        self.__context = context

    def start(self) :
        thread = threading.Timer(1 , self.start)
        thread.start()
        self.__context.request()

interval_context = IntervalContext( Focus() , Setting() )
timer = Timer(interval_context)
timer.start()