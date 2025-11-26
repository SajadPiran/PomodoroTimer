from abc import ABC
from common_types.interval import Interval
from services.setting.setting import Setting
from .state import State

class Context(ABC) :

    def __init__(self , state : State , setting : Setting) :
        self.__state_result = None
        self.__setting = setting
        self.__state : State = state
        self.__index : int = 0
        self.__data : list[Interval] = self.__setting.get_times_intervals()
        self.__current_data = self.__data[self.__index]

    @property
    def state(self) :
        return self.__state

    @state.setter
    def state(self, value: State):
        self.__state = value

    @property
    def state_result(self) :
        return self.__state_result

    @state_result.setter
    def state_result(self , value) :
        self.__state_result = value

    @property
    def data(self) :
        return self.__data

    @data.setter
    def data(self , data) :
        self.__data = data

    @property
    def current_data(self) :
        return self.__current_data

    @property
    def setting(self) :
        return self.__setting

    def set_current_data_to_next(self , index : int | None = None) :
        if self.__index < len(self.__data) and index is not None :
            self.__index = index
            self.__current_data = self.__data[index]

        if self.__index < len(self.__data) and index is None :
            self.__index += 1
            self.__current_data = self.__data[self.__index]

    def request(self) :
        return self.__state.request(self)

