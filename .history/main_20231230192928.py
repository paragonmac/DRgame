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
        self.main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

        self.main = QTextEdit()
        self.main.setReadOnly(True)
        splitter.addWidget(self.main)
        self.main.setMinimumHeight(100)

        self.textEdit = CustomTextEdit()
        splitter.addWidget(self.textEdit)
        self.textEdit.setFixedHeight(50)

        layout.addWidget(splitter)
        
    def update_display(self, text):
        self.main.setText(text)
