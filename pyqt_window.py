import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt



class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(CustomTextEdit, self).__init__(parent)
        self.storedText = ""  # Variable to store the text

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.storedText = self.toPlainText()  # Store the current text
            self.clear()  # Clear the text edit
            print("Stored Text:", self.storedText)  # Example action (e.g., print)
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
    def initUI(self):
   
        self.setWindowTitle('Game Title')
        self.setGeometry(100, 100, 1800, 1600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.Room = QTextEdit()
        self.Room.setReadOnly(True)
        layout.addWidget(self.Room)
       
        self.Main = QTextEdit()
        self.Main.setReadOnly(True)
        layout.addWidget(self.Main)

        self.textEdit = CustomTextEdit()
        layout.addWidget(self.textEdit)

def main():
    app = QApplication(sys.argv)
    mainWin = GameWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
