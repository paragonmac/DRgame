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

        self.Body = QTextEdit()  # Add the Body attribute
        self.Body.setReadOnly(True)
        splitter.addWidget(self.Body)
        self.Body.setMinimumHeight(100)

        self.textEdit = CustomTextEdit()
        splitter.addWidget(self.textEdit)
        self.textEdit.setFixedHeight(50)

        layout.addWidget(splitter)
        
    def update_display(self, text):
        self.Body.setText(text)
