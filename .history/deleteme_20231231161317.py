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
        # Append text at the end
        self.textEdit.append(text)
        
        # Move the scrollbar to the bottom
        cursor = QTextCursor(self.textEdit.document())
        cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(cursor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    widget.addTextAtBottom("First line (will appear at bottom)")
    widget.addTextAtBottom("Second line (will appear after first line)")

    sys.exit(app.exec_())
