from datetime import datetime, timedelta
from common_types.interval import Interval
from interfaces.states.state import State
from libs.helper import str_to_datetime, notify, number_to_text
from services.interval_context.interval_context import IntervalContext

class ShortBreak(State):

    def __init__(self):
        super().__init__()

    def request(self, context: IntervalContext):
        from services.interval_context.states.focus import Focus

        interval: Interval = context.current_data
        current_time: datetime = datetime.now().replace(microsecond=0)
        interval_time: datetime = str_to_datetime(interval['time'])
        diff: timedelta = interval_time - current_time

        if interval['state'] != 'short_break':
            raise RuntimeError("Invalid state")

        if diff.total_seconds() <= 0.0:
            notify( 'Focus' , f'The {number_to_text( str(interval['number'] + 1) )} focus has started...' )
            context.set_current_data_to_next()
            context.state = Focus()

        context.state_result = {
            'result' : 'success' ,
            'state' : 'short_break',
            'diff' : diff,
            'interval' : interval,
        }