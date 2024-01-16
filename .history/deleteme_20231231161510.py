import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QTextCursor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.layout.addWidget(self.textEdit)

    def addTextAtBottom(self, text):
        # Move cursor to the beginning
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.textEdit.setTextCursor(cursor)

        # Insert new text at the cursor position
        self.textEdit.insertPlainText(text + '\n')

        # Scroll to the bottom
        cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(cursor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    widget.addTextAtBottom("New text at the bottom, pushing older text up.")
    widget.addTextAtBottom("Another line at the bottom.")

    sys.exit(app.exec_())
