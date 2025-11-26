from datetime import datetime
from config import BASE_DIR
import os
from notifypy import Notify

def path( *path : str ) -> str:
    return str( os.path.join( BASE_DIR, *path ) )

def format_date( date : datetime ) -> str :
    return date.strftime('%Y-%m-%d %H:%M:%S')

def str_to_datetime( value : str ) -> datetime :
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

def notify( title : str , message : str ) -> None :
    notification = Notify()
    notification.icon = os.path.join(BASE_DIR, 'app', 'icons', 'icon.png')
    notification.application_name = 'Pomodoro Timer'
    notification.audio = os.path.join(BASE_DIR, 'app', 'notification.wav')
    notification.title = title
    notification.message = message
    notification.send()

def number_to_text(number : str) -> str :
    texts = {
        '1' : 'First' ,
        '2' : 'Second' ,
        '3' : 'Third' ,
        '4' : 'Fourth' ,
        '5' : 'Fifth',
        '6' : 'Sixth',
        '7' : 'Seventh',
        '8' : 'Eighth',
        '9' : 'Ninth',
        '10' : 'Tenth',
        '11' : 'Eleventh',
        '12' : 'Twelfth',
        '13' : 'Thirteenth',
        '14' : 'Fourteenth',
        '15' : 'Fifteenth',
        '16' : 'Sixteenth',
        '17' : 'Seventeenth',
        '18' : 'Eighteenth',
        '19' : 'Nineteenth',
        '20' : 'Twenty',
    }
    return texts.get(number, number)