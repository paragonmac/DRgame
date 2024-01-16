import sys
import threading

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QSplitter, QTextEdit

import game
import player


class SenderWidget(QWidget):
    textEntered = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.lineEdit = QLineEdit()
        self.lineEdit.returnPressed.connect(self.onReturnPressed)
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.setStyleSheet("QTextEdit {background-color: #333333; color: #ffffff;}")

    def onReturnPressed(self):
        self.textEntered.emit(self.lineEdit.text())
        self.lineEdit.clear()

class GameWindow(QMainWindow):    
    def __init__(self, senderWidget):
        super().__init__()
        self.senderWidget = senderWidget
        self.senderWidget.textEntered.connect(self.update_display)
        self.initUI()
        #make custom color scheme
        self.setStyleSheet("QTextEdit {background-color: #333333; color: #ffffff;}")

    def initUI(self):
        self.setWindowTitle('Game Title')
        self.setGeometry(100, 100, 1800, 1600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        splitter = QSplitter(Qt.Vertical)
        self.Room = QTextEdit()
        self.Room.setReadOnly(True)
        splitter.addWidget(self.Room)

        self.Body = QTextEdit()
        self.Body.setReadOnly(True)
        splitter.addWidget(self.Body)

        splitter.addWidget(self.senderWidget)

        layout.addWidget(splitter)

    def update_display(self, text):
        self.Body.setText(text)
        self.Body.new

def thread_start(objGame):
    thread_game_output = threading.Thread(target=objGame.check_game_output_queue)
    thread_game_output.daemon = True

    thread_gameLogicWorker = threading.Thread(target=objGame.main_game_loop)
    thread_gameLogicWorker.daemon = True

    thread_gameLogicWorker.start()
    thread_game_output.start()

def main():
    app = QApplication(sys.argv)

    senderWidget = SenderWidget()
    mainWin = GameWindow(senderWidget)
    mainWin.show()

    objPlayer = player.clsPlayer("Default_Player_Name", 100, "knife", 100, None)
    objGame = game.clsGame()

    thread_start(objGame)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
