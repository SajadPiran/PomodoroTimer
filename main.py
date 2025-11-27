import os
import sys
from PyQt6.QtWidgets import QApplication
from app.MainWindow import MainWindow
from PyQt6.QtGui import QFontDatabase
from libs.helper import path
from services.interval_context.interval_context import IntervalContext
from services.interval_context.states.focus import Focus
from services.setting.setting import Setting

if __name__ == '__main__' :

    app = QApplication(sys.argv)
    fonts_path = path('app' , 'fonts')
    for font in os.scandir(fonts_path) :
        QFontDatabase.addApplicationFont( path( 'app', 'fonts', font.name ) )

    interval_context = IntervalContext(Focus(), Setting())
    window = MainWindow(interval_context)
    sys.exit(app.exec())

