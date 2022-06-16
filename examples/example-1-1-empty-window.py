import sys
from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """ Set up the application """
        # Set x, y, width, height as *__args
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        # Display the window on the screen
        self.show()


# Run the program
if __name__ == '__main__':
    # A single instance of the QApplication class is responsible for many windows
    # or dialog boxes existing in an application.
    # sys.argv is needed for taking command-line arguments, otherwise use [] instead.
    app = QApplication(sys.argv)
    window = EmptyWindow()
    # The method exec() starts the application's event loop.
    # The function sys.exit() ensures a clean exit.
    sys.exit(app.exec())
