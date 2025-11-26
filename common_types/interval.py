from typing import TypedDict , Literal , NotRequired

class Interval(TypedDict) :
    id : int | str
    time : str
    number : int
    state : Literal['focus' , 'short_break' , 'long_break']
    is_last_focus : NotRequired[bool]
