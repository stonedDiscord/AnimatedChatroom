from PyQt5 import QtCore, QtWidgets, uic
from ui.viewport import Viewport
from ui.sound_mixer import SoundMixer
from ui.ooc import OOCChat


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("main.ui", self)

        self.viewport = Viewport(self)

        self.load_widgets()
        self.show()

    def load_widgets(self):
        # self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.viewport)
        self.setCentralWidget(self.viewport)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, SoundMixer(self))
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, OOCChat(self))

    def open_about(self):
        QtWidgets.QMessageBox.about(self, "Animated Chatroom", "Hi")

    def open_feedback(self):
        pass

    def open_guide(self):
        pass

    def open_howto(self):
        pass