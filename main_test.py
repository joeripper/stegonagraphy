from PyQt5.QtCore import QDir, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QCheckBox, QFileDialog, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpinBox,
        QVBoxLayout, QWidget)

import os
import stego

class StegoImage(QWidget):
    def __init__(self):
        super(StegoImage, self).__init__()

        self.adressFirstImage = ''
        self.adressSecondImage = ''
        self.mainLayout = QGridLayout()

        self.imageLabel1 = QLabel()
        self.imageLabel1.resize(300, 300)
        self.imageLabel2 = QLabel()
        self.imageLabel2.resize(300, 300)

        self.createButtonsLayout()


        self.setLayout(self.mainLayout)

        self.setWindowTitle("stego image")
        self.resize(200, 50)

    def createButtonsLayout(self):
        self.loadButton1 = self.createButton("firstImage", self.show_dialog)
        self.loadButton2 = self.createButton("secondImage", self.show_dialog)
        self.processButton = self.createButton("run", self.show_dialog)
        self.unprocessButton = self.createButton("giveGolo", self.show_new_window)

        self.mainLayout.addWidget(self.loadButton1, 1, 0)
        self.mainLayout.addWidget(self.loadButton2, 1, 1)
        self.mainLayout.addWidget(self.processButton, 1, 2)
        self.mainLayout.addWidget(self.unprocessButton, 1, 3)

    def createButton(self, text, member):
        button = QPushButton(text)
        button.clicked.connect(member)
        return(button)

    def show_dialog(self):
        self.mainLayout.addWidget(self.imageLabel1, 0, 0, 1, 2)
        self.mainLayout.addWidget(self.imageLabel2, 0, 2, 1, 2)

        sender = self.sender()
        fname = QFileDialog.getOpenFileName(self, 'Open Image', os.getcwd())[0]
        pixmap = QPixmap(fname).scaled(300, 300)
        if sender.text() == "firstImage":
            self.imageLabel1.setPixmap(pixmap)
            self.adressFirstImage = fname
        elif sender.text() == "secondImage":
            self.imageLabel2.setPixmap(pixmap)
            self.adressSecondImage = fname
#        elif sender.text() == "run":
#            stego.process_image(self.adressFirstImage, self.adressSecondImage, fname)
        else:
            pass

    def show_new_window(self):
        self.processWindow = QWidget()
        self.processLayout = QGridLayout()
        self.processLabel = QLabel()
        tmp = stego.process_image(self.adressFirstImage, self.adressSecondImage)
        self.processPixmap = QPixmap()

        self.processLabel.setPixmap(self.processPixmap)
        self.processLayout.addWidget(self.processLabel)
        self.processWindow.setWindowTitle("new window")
        self.processWindow.setLayout(self.processLayout)
        self.processWindow.show()



    def temp_func(self):
        print('dick')



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    stegoApp = StegoImage()
    stegoApp.show()
    sys.exit(app.exec_())