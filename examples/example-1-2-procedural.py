# 1. Import necessary modules
# Use sys to accept command-line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget
# 2. Create QApplication object
app = QApplication(sys.argv)
# 3. Create window from QWidget object
window = QWidget()
# 4. Call the show method to display GUI window
window.show()
# 5. Start the event loop. Use sys.exit to close the program
sys.exit(app.exec())
