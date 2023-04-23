
if __name__ == "__main__":
    import sys
    from keyboard_gui import MainWindow
    from PyQt5 import QtWidgets
    import other_func as of
    import time

    of.change_layout('en')
    time.sleep(1)

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
