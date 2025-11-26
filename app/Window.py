import os.path
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import  loadUi

from libs.helper import path


class Window(QMainWindow) :

    def __init__(self) :
        super().__init__()
        loadUi( path('app' , 'ui' , 'mainWindow.ui') , self)
        self.setWindowTitle('Pomodoro Timer')
        self.setWindowIcon( QIcon( path('app' , 'icons' , 'icon.png') ) )
        self.show()

