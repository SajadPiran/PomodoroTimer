from typing import TypedDict , Literal

class Interval(TypedDict) :
    id : int | str
    time : str
    number : int
    state : Literal['focus' , 'short_break' , 'long_break']
