if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create QApplication instance
    mainWin = GameWindow()
    mainWin.show()
    sys.exit(app.exec_())
