import sys
import os
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog, QLabel, QTextEdit


# you can copy and run this code

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        self.warning = False
        self.file_path = None
        self.TP_1_Flair = ''
        self.TP_1_T1 = ''

        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("DICOM to NIFTI Converter")
        self.setFixedSize(500, 300)

        file_btn = QPushButton("Choose the DICOM Folder")
        self.myTextBox = QTextEdit()
        self.myTextBox.setFixedHeight(40)
        verify_1 = QLabel("Please verify the file path")
        verify_1.setAlignment(Qt.AlignRight)
        self.errorcheck = QLabel('-')
        self.errorcheck.setAlignment(Qt.AlignRight)


        self.file_btn_2 = QPushButton("Choose path for NIFTI Image")
        self.myTextBox_2 = QTextEdit()
        self.myTextBox_2.setFixedHeight(40)
        verify_2 = QLabel("Please verify the file path")
        verify_2.setAlignment(Qt.AlignRight)

        self.convert = QPushButton("Convert DICOM to NIFTI")

        layout = QVBoxLayout()
        layout.addWidget(file_btn)
        layout.addWidget(self.myTextBox)
        layout.addWidget(verify_1)
        layout.addWidget(self.errorcheck)


        layout.addWidget(self.file_btn_2)
        layout.addWidget(self.myTextBox_2)
        layout.addWidget(verify_2)

        layout.addWidget(self.convert)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        file_btn.clicked.connect(self.open_1)  # connect clicked to self.open()
        self.file_btn_2.clicked.connect(self.open_2)  # connect clicked to self.open()
        self.convert.clicked.connect(self.dicom_to_nifti)

        self.file_btn_2.setEnabled(False)
        self.convert.setEnabled(False)

        self.show()

    def open_1(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if path != ('', ''):
            print("File path : " + path)
            self.myTextBox.setText(path)
            self.DICOM_folder = path
    #         IMPLEMENT TO ONLY CHOOSE FOLDER!!
            self.file_btn_2.setEnabled(True)

        files = os.listdir(path)
        for i in files:
            if '.dcm' in i:
                print("x")
            else:
                self.warning = True
        print("warning " + str(self.warning))
        if self.warning == True:
            self.errorcheck.setText("DICOM Images not in Folder, please recheck!")
        else:
            self.errorcheck.setText("Looks Good!")

    def open_2(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if path != ('', ''):
            print("File path : " + path)
            self.myTextBox_2.setText(path)
            self.nifti_path = path
            self.convert.setEnabled(True)
    #         IMPLEMENT TO ONLY CHOOSE FILE!!

    def dicom_to_nifti(self):
        x = os.system(f"dcm2niix -z y -f %p_%t_%s -o {self.nifti_path} {self.DICOM_folder}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
