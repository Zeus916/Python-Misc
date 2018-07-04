import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import QRect
import cv2
from PIL.ImageQt import ImageQt



class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        FileName =  'dog2.jpg'
        # Create widget
        label = QLabel(self)
        #  pixmap = QPixmap('dog.jpg')
        Image = cv2.imread('dog2.jpg')
        width , height, channel = Image.shape
        bytesPerLine = 3 *width
        #qImg = QImage(Image, width, height, QImage.Format_RGB888)

        qim = ImageQt(Image)
        pix = QPixmap.fromImage(qim)

        #qpix = QPixmap.fromImage(qImg)
        # label.setGeometry(QRect(10,10, width, height))
        label.setPixmap(QPixmap(pix))
        
        # self.resize(pixmap.width(),pixmap.height())
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())