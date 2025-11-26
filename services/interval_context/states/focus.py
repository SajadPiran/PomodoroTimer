from datetime import datetime, timedelta
from common_types.interval import Interval
from interfaces.states.state import State
from libs.helper import str_to_datetime, notify, number_to_text
from services.interval_context.interval_context import IntervalContext
from services.interval_context.states.long_break import LongBreak
from services.interval_context.states.short_break import ShortBreak


class Focus(State) :

    def __init__(self):
        super().__init__()

    def request(self , context : IntervalContext) :
        interval : Interval = context.current_data
        current_time : datetime = datetime.now().replace(microsecond=0)
        interval_time : datetime = str_to_datetime( interval['time'] )
        diff : timedelta = interval_time - current_time

        if interval['state'] != 'focus' :
            raise RuntimeError("Invalid state")

        if diff.total_seconds() <= 0.0 and interval['is_last_focus'] :
            notify('Pomodoro Cycle', f'The Pomodoro cycle has ended.')
            context.set_current_data_to_next( len(context.data) - 1 )
            context.state = LongBreak()
            return

        if diff.total_seconds() <= 0.0 :
            notify( 'Focus' , f'The {number_to_text( str(interval['number']) )} focus has ended...' )
            context.set_current_data_to_next()
            context.state = ShortBreak()

        context.state_result = {
            'result' : 'success' ,
            'state' : 'focus',
            'diff' : diff,
            'interval' : interval,
        }