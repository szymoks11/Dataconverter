import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Converter')

        self.layout = QVBoxLayout()

        self.input_label = QLabel('No input file selected')
        self.output_label = QLabel('No output file selected')

        self.input_button = QPushButton('Select Input File')
        self.input_button.clicked.connect(self.select_input_file)

        self.output_button = QPushButton('Select Output File')
        self.output_button.clicked.connect(self.select_output_file)

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_files)

        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_button)
        self.layout.addWidget(self.convert_button)

        self.setLayout(self.layout)

    def select_input_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yaml *.yml)", options=options)
        if file:
            self.input_label.setText(file)

    def select_output_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yaml *.yml)", options=options)
        if file:
            self.output_label.setText(file)

    def convert_files(self):
        input_file = self.input_label.text()
        output_file = self.output_label.text()
        convert(input_file, output_file)
        print(f"Converted {input_file} to {output_file}")

def main():
    app = QApplication(sys.argv)
    ex = ConverterUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
