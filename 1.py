import sys
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon(
            [QPoint(50,100), QPoint(50,200), 
             QPoint(100,200), QPoint(100,100),])
        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.drawPolygon([QPoint(100,200), QPoint(200,200), QPoint(200,100), QPoint(100,100)])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
        
class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        polygon_points = [
            QPoint(random.randint(50, 150), random.randint(50, 150)),
            QPoint(random.randint(100, 200), random.randint(100, 200)),
            QPoint(random.randint(150, 250), random.randint(50, 150)),
            QPoint(random.randint(100, 200), random.randint(200, 300)),
        ]
        p.drawPolygon(polygon_points)
        p.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        p.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pie_position = QPoint(random.randint(50, 200), random.randint(200, 400))
        pie_size = random.randint(50, 150)
        p.drawPie(pie_position.x(), pie_position.y(), pie_size, pie_size, 0, 180 * 16)
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
        
class Simple_drawing_window4(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Preme Drawing")
        self.monkey = QPixmap("images/monkey.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
    
        p.setPen(QColor(255, 255, 0)) 
        p.setBrush(QColor(255, 255, 0))
        p.drawEllipse(100, 100, 50, 200)  
        
        p.setPen(QColor(139, 69, 19))  
        p.setBrush(QColor(139, 69, 19))
        p.drawRect(115, 50, 20, 50)  
        p.drawPixmap(QRect(250,100,300,300), self.monkey)
        p.end()
        
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window4()
    w.show()
    
    w2 = Simple_drawing_window2()
    w2.show()
    
    w3 = Simple_drawing_window3()
    w3.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
