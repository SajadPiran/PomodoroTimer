from interfaces.states.context import Context

class Timer :

    def __init__(self , context : Context) :
        self.__context = context

    def start(self) :
        self.__context.request()
