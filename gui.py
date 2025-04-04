from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from memory_manager import MemoryManager
from visualization import visualize_paging, visualize_segmentation

class MemoryTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = MemoryManager()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Real-Time Memory Tracker")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()
        self.btn_allocate_paging = QPushButton("Allocate Paging", self)
        self.btn_allocate_paging.clicked.connect(self.allocate_paging)

        self.btn_allocate_segmentation = QPushButton("Allocate Segmentation", self)
        self.btn_allocate_segmentation.clicked.connect(self.allocate_segmentation)

        self.btn_visualize = QPushButton("Show Memory", self)
        self.btn_visualize.clicked.connect(self.show_visualization)

        self.label = QLabel("Memory Tracker Running...", self)
        layout.addWidget(self.btn_allocate_paging)
        layout.addWidget(self.btn_allocate_segmentation)
        layout.addWidget(self.btn_visualize)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def allocate_paging(self):
        self.manager.allocate_paging(1, 5)
        self.label.setText("Paging Allocated")

    def allocate_segmentation(self):
        self.manager.allocate_segmentation(2, 10)
        self.label.setText("Segmentation Allocated")

    def show_visualization(self):
        visualize_paging(self.manager)
        visualize_segmentation(self.manager)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryTrackerApp()
    window.show()
    sys.exit(app.exec_())
