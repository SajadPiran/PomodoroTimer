import os
from datetime import datetime, timedelta
from common_types.interval import Interval
from interfaces.states.state import State
from libs.helper import str_to_datetime, notify, number_to_text, path
from services.interval_context.interval_context import IntervalContext

class LongBreak(State):

    def __init__(self):
        super().__init__()

    def request(self, context: IntervalContext):
        from services.interval_context.states.focus import Focus

        interval: Interval = context.current_data
        current_time: datetime = datetime.now().replace(microsecond=0)
        interval_time: datetime = str_to_datetime(interval['time'])
        diff: timedelta = interval_time - current_time

        if interval['state'] != 'long_break':
            raise RuntimeError("Invalid state")

        if diff.total_seconds() <= 0.0 :
            notify( 'Pomodoro Timer' , f'A new pomodoro timer has started...' )
            context.data = context.setting.create_times_intervals()['data']
            context.set_current_data_to_next(0)
            context.state = Focus()

        context.state_result = {
            'result' : 'success' ,
            'state' : 'long_break',
            'diff' : diff,
            'interval' : interval,
        }