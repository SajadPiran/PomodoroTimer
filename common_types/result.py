from typing import TypedDict, Literal, TypeVar, Generic

T = TypeVar("T")
class Result(TypedDict , Generic[T]) :
    result : Literal['success', 'failure']
    message : str
    data : T