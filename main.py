import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Import de la classe générée depuis le .ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Applique l'interface à cette fenêtre

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()