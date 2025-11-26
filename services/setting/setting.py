import json
import os
from datetime import datetime, timedelta
from typing import Optional
from common_types.result import Result
from common_types.setting_type import SettingType
from common_types.interval import Interval
from libs.helper import path, format_date

default_value : SettingType = {
    'focus': 25,
    'short_break': 5,
    'long_break': 30,
    'cycle': 4
}
class Setting :

    def __init__(self) :
        self.__file_name : str = 'settings.json'
        self.__times_file_name : str = 'intervals.json'
        self.create_times_intervals()

    def create( self , setting : Optional[SettingType] = None ) -> Result[SettingType]:

        file_path : str = path( 'config' , self.__file_name )
        setting_data = json.dumps(default_value) if setting is None else json.dumps(setting)
        if os.path.exists( file_path ) :
            os.remove( file_path )
        with open( file_path, 'w') as file :
            file.write( setting_data )

        return {
            'result' : 'success' ,
            'message' : 'The setting created successfully.' ,
            'data' : default_value
        }

    def get( self ) -> SettingType :
        file_path: str = path('config', self.__file_name)
        if not os.path.exists( file_path ) :
            return default_value

        with open(file_path, 'r') as file :
            return json.load( file )

    def create_times_intervals( self ) -> Result[list[Interval]] :
        file_path: str = path('config', self.__times_file_name)
        settings : SettingType = self.get()
        focus , short_break, long_break, cycle = settings['focus'] , settings['short_break'] , settings['long_break'] , settings['cycle']

        timer_intervals : list[Interval] = []
        current_time : datetime = datetime.now()

        # For create a focus[Interval] and short_break[Interval]
        # For each timer cycle
        range_number : int = cycle * 2 + 1
        cycle_number : int = 1
        for i in range(1 , range_number ) :
            if i % 2 != 0 :
                current_time += timedelta(minutes=focus)
                data : Interval = {
                    'id' : i ,
                    'time' : format_date( current_time ) ,
                    'number' : cycle_number ,
                    'state' : 'focus' ,
                    'is_last_focus' : True if cycle_number == cycle else False
                }
                timer_intervals.append( data )
            else :
                current_time += timedelta(minutes=short_break)
                data: Interval = {
                    'id': i,
                    'time': format_date( current_time ),
                    'number': cycle_number,
                    'state': 'short_break'
                }
                timer_intervals.append(data)
                cycle_number += 1

        long_break_interval : Interval = {
            'id' : range_number ,
            'time' : format_date( current_time + timedelta(minutes=long_break) ),
            'number' : range_number,
            'state' : 'long_break'
        }
        timer_intervals.append(long_break_interval)

        if os.path.exists( file_path ) :
            os.remove( file_path )
        with open( file_path, 'w') as file :
            file.write( json.dumps(timer_intervals) )

        return {
            'result' : 'success' ,
            'message' : 'The timer intervals created successfully.' ,
            'data' : timer_intervals
        }

    def get_times_intervals(self) -> list[Interval] :
        file_path: str = path('config', self.__times_file_name)
        if not os.path.exists( file_path ) :
            return self.create_times_intervals()['data']

        with open(file_path, 'r') as file :
            return json.load( file )
