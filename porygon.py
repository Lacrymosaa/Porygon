import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image

class Porygon(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Porygon')
        self.setWindowIcon(QIcon("porygon.ico"))
        self.setFixedSize(300, 100)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.load_button = QPushButton('Carregar Arquivo PNG', self)
        self.load_button.clicked.connect(self.loadPNG)

        self.convert_button = QPushButton('Converter para ICO', self)
        self.convert_button.clicked.connect(self.convert)
        self.convert_button.setEnabled(False)

        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.convert_button)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.central_widget.setLayout(self.layout)

    def loadPNG(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, 'Carregar Arquivo PNG', '', 'Images (*.png)', options=options)

        if fileName:
            self.png_file = fileName
            self.convert_button.setEnabled(True)
            self.showImage(fileName)

    def showImage(self, fileName):
        pixmap = QPixmap(fileName)
        self.image_label.setPixmap(pixmap)
        self.image_label.show()

    def convert(self):
        try:
            png_image = Image.open(self.png_file)

            ico_file = os.path.splitext(self.png_file)[0] + '.ico'
            png_image.save(ico_file)

            QMessageBox.information(self, 'Sucesso', f'Arquivo ICO gerado: {ico_file}')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao converter imagem: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Porygon()
    window.show()
    sys.exit(app.exec_())
