import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Create the text edit widget
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)  # Makes it read-only
        self.layout.addWidget(self.textEdit)

        # Add some initial text
        self.textEdit.append("Initial text at the bottom.")

    def addText(self, text):
        self.textEdit.append(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    # Example of adding new text
    widget.addText("New text, will appear below and push older text up.")

    sys.exit(app.exec_())
