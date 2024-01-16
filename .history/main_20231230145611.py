import sys
import clsg
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
            self.textStored.emit(self.storedText)  # Emit the signal
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
        self.Main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

        self.Main = QTextEdit()
        self.Main.setReadOnly(True)
        splitter.addWidget(self.Main)
        self.Main.setMinimumHeight(100)

        self.textEdit = CustomTextEdit()
        splitter.addWidget(self.textEdit)
        self.textEdit.setFixedHeight(50)

        layout.addWidget(splitter)

def run(self):
        global thread_game_output, thread_gameLogicWorker
        thread_game_output = threading.Thread(target=self.check_game_output_queue)
        thread_game_output.setDaemon = True

        thread_gameLogicWorker = threading.Thread(target=self.main_game_loop)
        thread_gameLogicWorker.setDaemon = True
        
        thread_PyQtWindow = threading.Thread(target=pyqt_window.main)

        thread_gameLogicWorker.start()
        thread_game_output.start()
        thread_PyQtWindow.start()
        
def main():
    app = QApplication(sys.argv)
    mainWin = GameWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create QApplication instance
    main()
