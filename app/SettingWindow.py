import os.path
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton
from PyQt6.uic import  loadUi
from common_types.setting_type import SettingType
from interfaces.states.context import Context
from libs.helper import path


class SettingWindow(QtWidgets.QWidget) :

    def __init__(self , context : Context) :
        super().__init__()
        loadUi( path('app' , 'ui' , 'setting.ui') , self)
        self.setWindowTitle('Pomodoro Timer Setting')
        self.setWindowIcon( QIcon( path('app' , 'icons' , 'icon.png') ) )
        self._context = context
        self.__button : QPushButton = self.findChild( QPushButton , 'save' )
        self.__button.clicked.connect( self.__on_click )
        self.__init_data()

    def __init_data(self) :
        setting = self._context.setting.get()
        inputs : list[QtWidgets.QTextEdit] = self.findChildren(QtWidgets.QTextEdit)
        for input in inputs :
            data = setting[input.objectName()]
            input.setText( str(data) )

    def __on_click(self):
        setting : SettingType = self._context.setting.get()
        inputs: list[QtWidgets.QTextEdit] = self.findChildren(QtWidgets.QTextEdit)
        for input in inputs :
            if input.toPlainText() != '' and input.toPlainText() >= '1':
                setting[input.objectName()] = int(input.toPlainText())

        self._context.setting.create(setting)
        self._context.data = self._context.setting.create_times_intervals()['data']
        self._context.set_current_data_to_next(0)
        self.close()
