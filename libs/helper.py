from datetime import datetime

from config import BASE_DIR
import os

def path( *path : str ) -> str:
    return str( os.path.join( BASE_DIR, *path ) )

def format_date( date : datetime ) -> str :
    return date.strftime('%Y-%m-%d %H:%M:%S')