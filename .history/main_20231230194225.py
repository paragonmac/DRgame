import sys
import game
import player
import threading
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QVBoxLayout, QWidget, QSplitter, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QEventLoop


class CustomTextEdit(QTextEdit):
    textStored = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(CustomTextEdit, self).__init__(parent)
        self.storedText = ""  # Variable to store the text

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.storedText = self.toPlainText()  # Store the current text
            self.clear()  # Clear the text edit
            print("Stored Text:", self.storedText)  # Example action (e.g., print)
            GameWindow.update_display(self, self.storedText)
        else:
            super(CustomTextEdit, self).keyPressEvent(event)  # Handle other key presses

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("""
            QTextEdit {
                font-family: 'Arial';
                font-size: 24px;
                color: white;
                background-color: Black;
            }
        """)
        self.Room.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Body.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
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
        self.Room.setMinimumHeight(300)
        self.Room.adjustSize()

        self.Body = QTextEdit()
        self.Body.setReadOnly(True)
        splitter.addWidget(self.Body)
        self.Body.setMinimumHeight(100)

        self.textEdit = CustomTextEdit()
        splitter.addWidget(self.textEdit)
        self.textEdit.setFixedHeight(50)

        layout.addWidget(splitter)
        
    def update_display(self, text):
        self.Body.setText(text)


global thread_game_output, thread_gameLogicWorker
def thread_start():
    print("Starting threads")
    thread_game_output = threading.Thread(target=objGame.check_game_output_queue)
    thread_game_output.setDaemon = True

    thread_gameLogicWorker = threading.Thread(target=objGame.main_game_loop(objPlayer))
    thread_gameLogicWorker.setDaemon = True

    thread_gameLogicWorker.start()
    thread_game_output.start()

def main():
    print("Starting main")
    app = QApplication(sys.argv)
    mainWin = GameWindow()
    mainWin.show()
    sys.exit(app.exec_())

def exit():
    print("Exiting")
    thread_game_output.join()
    thread_gameLogicWorker.join()


if __name__ == '__main__':
    print("Starting")
    objPlayer = player.clsPlayer("Default_Player_Name", 100, "knife", 100, None)
    objGame = game.clsGame()
    
    main()
    thread_start()
