import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import random

class KoordinatMouse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Task Week 3 - (F1D022110 - Ameylia Intan Zurtika Ayu)')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")
        
        self.label_koordinat = QLabel(self)
        self.label_koordinat.setAlignment(Qt.AlignCenter)
        self.label_koordinat.resize(150, 30)
        
        self.label_koordinat.setMouseTracking(True)
        self.label_koordinat.installEventFilter(self)
        self.setMouseTracking(True)
        
        self.show()
    
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        
        self.label_koordinat.setText(f"x: {x}, y: {y}")
        
        offset_x = 20  
        offset_y = 20
        
        posisi_x_baru = x + offset_x
        posisi_y_baru = y + offset_y
        
        if posisi_x_baru + self.label_koordinat.width() > self.width():
            posisi_x_baru = self.width() - self.label_koordinat.width()
        
        if posisi_y_baru + self.label_koordinat.height() > self.height():
            posisi_y_baru = self.height() - self.label_koordinat.height()
        
        self.label_koordinat.move(posisi_x_baru, posisi_y_baru)
    
    def eventFilter(self, obj, event):
        if obj == self.label_koordinat and event.type() == event.Enter:
            lebar_jendela = self.width() - self.label_koordinat.width()
            tinggi_jendela = self.height() - self.label_koordinat.height()
            posisi_x_baru = random.randint(0, lebar_jendela)
            posisi_y_baru = random.randint(0, tinggi_jendela)
            self.label_koordinat.move(posisi_x_baru, posisi_y_baru)
            
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = KoordinatMouse()
    sys.exit(app.exec_())
