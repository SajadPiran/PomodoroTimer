from PyQt6.QtCore import QTimer, QEvent, Qt
from PyQt6.QtGui import QIcon
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.uic import  loadUi
from app.SettingWindow import SettingWindow
from app.clickableLabel import ClickableLabel
from interfaces.states.context import Context
from libs.helper import path
from services.interval_context.states.focus import Focus


class MainWindow(QtWidgets.QMainWindow) :

    def __init__(self , context : Context) :
        super().__init__()
        loadUi( path('app' , 'ui' , 'mainWindow.ui') , self)
        self.setWindowTitle('Pomodoro Timer')
        self.setWindowIcon( QIcon( path('app' , 'icons' , 'icon.png') ) )
        self._QTimer = QTimer()
        self._QTimer.timeout.connect( self.__start_timer )
        self._context = context
        self._is_running = False

        self.__title = self.findChild(QtWidgets.QLabel, 'title')
        self.__time = self.findChild(QtWidgets.QLabel, 'time')
        self.__setting_button = self.findChild(QtWidgets.QPushButton, 'setting')
        self.__start_timer_button = self.findChild( QtWidgets.QPushButton, 'startTimer' )
        self.__tasks_layout = self.findChild( QtWidgets.QVBoxLayout, 'TasksLayout' )
        self.__task_input = self.findChild( QtWidgets.QTextEdit, 'AddTask' )
        self.__task_input.installEventFilter(self)
        self.__start_timer_button.clicked.connect( self.__on_clicked )
        self.__setting_button.clicked.connect( self.__open_setting_window )
        self.show()

    def eventFilter(self, obj, event):
        if obj is self.__task_input and event.type() == QEvent.Type.KeyPress :
            if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return) :
                label = ClickableLabel(self.__task_input.toPlainText().strip())
                label.setStyleSheet( 'font: 57 8pt "JetBrains Mono Medium";' )
                label.setWordWrap(True)
                label.clicked.connect( self.__done_label )
                label.doubleClicked.connect(self.__delete_label)
                self.__tasks_layout.addWidget( label )
                self.__task_input.setPlainText(None)
                return True

        return super().eventFilter(obj, event)

    def __create_intervals(self) :
        self._context.state = Focus()
        self._context.data = self._context.setting.create_times_intervals()['data']
        self._context.set_current_data_to_next(0)

    def __on_clicked(self) :
        if not self._is_running :
            self.__create_intervals()
            self._is_running = True
            self.__start_timer_button.setText('Stop Timer')
            self._QTimer.start(1000)
        else :
            self._is_running = False
            self.__start_timer_button.setText('Start New Timer')
            self._QTimer.stop()

    def __start_timer(self) :
        self._context.request()
        state_result = self._context.state_result
        self.__time.setText( state_result['diff'] )
        self.__title.setText( state_result['title'] )

    def __open_setting_window(self) :
        if not self._is_running :
            self.__setting_window = SettingWindow(self._context)
            self.__setting_window.show()

    def __done_label(self , label : QLabel) :
        label.setStyleSheet('font: 57 8pt "JetBrains Mono Medium";text-decoration:line-through')

    def __delete_label(self , label : QLabel) :
        label.deleteLater()