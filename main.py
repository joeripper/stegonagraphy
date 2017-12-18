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
        self.imagelayout = QGridLayout()

        self.imageLabel1 = QLabel()
        self.imageLabel1.setAlignment(Qt.AlignCenter)
        self.imageLabel1.resize(300, 300)
        self.imageLabel2 = QLabel()
        self.imageLabel2.setAlignment(Qt.AlignCenter)
        self.imageLabel2.resize(300, 300)
        self.imagelayout.addWidget(self.imageLabel1, 0, 0)
        self.imagelayout.addWidget(self.imageLabel2, 0, 1)

        self.createButtonsLayout()

        mainLayout = QVBoxLayout()
#        mainLayout.addWidget(self.imageLabel1)
#        mainLayout.addWidget(self.imageLabel2)
        mainLayout.addLayout(self.imagelayout)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)

#        self.shootScreen()
#        self.delaySpinBox.setValue(5)

        self.setWindowTitle("stego image")
        self.resize(640, 400)

    def createButtonsLayout(self):
        self.loadButton1 = self.createButton("firstImage", self.show_dialog)

        self.loadButton2 = self.createButton("secondImage", self.show_dialog)

        self.processButton = self.createButton("run", self.show_dialog)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.loadButton1)
        self.buttonsLayout.addWidget(self.loadButton2)
        self.buttonsLayout.addWidget(self.processButton)

    def createButton(self, text, member):
        button = QPushButton(text)
        button.clicked.connect(member)
        return button

    def show_dialog(self):
        sender = self.sender()
        fname = QFileDialog.getOpenFileName(self, 'Open Image', os.getcwd())[0]
        pixmap = QPixmap(fname)
        if sender.text() == "firstImage":
            self.imageLabel1.setPixmap(pixmap)
            self.adressFirstImage = fname
        elif sender.text() == "secondImage":
            self.imageLabel2.setPixmap(pixmap)
            self.adressSecondImage = fname
        else:
            stego.process_image(self.adressFirstImage, self.adressSecondImage, fname)




    def temp_func(self):
        print('dick')



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    stegoApp = StegoImage()
    stegoApp.show()
    sys.exit(app.exec_())