import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.text_lines = []  # Store lines of text in reverse order
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.layout.addWidget(self.textEdit)

    def addTextAtBottom(self, text):
        # Insert new text at the beginning of the list
        self.text_lines.insert(0, text)
        # Update the textEdit with reversed text
        self.textEdit.setPlainText('\n'.join(self.text_lines))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    # Example of adding new text
    widget.addTextAtBottom("First line (will appear at bottom)")
    widget.addTextAtBottom("Second line (will push first line up)")

    sys.exit(app.exec_())
