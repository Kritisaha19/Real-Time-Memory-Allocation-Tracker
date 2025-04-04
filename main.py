from PyQt5.QtWidgets import QApplication
import sys
from gui import MemoryTrackerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryTrackerApp()
    window.show()
    sys.exit(app.exec_())
