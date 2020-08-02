from src.window import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
