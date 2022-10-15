from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QSpinBox, QSlider
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
import sys

# mozna wpisac adres https strony i po kliknieciu w przycisk przekierowuje do strony
def guiMain(args):
    app = QApplication(args)
    window = QWidget()
    verticallayout = QVBoxLayout(window)
    address = QLineEdit()
    button = QPushButton("Go")
    layout = QHBoxLayout()
    layout.addWidget(address)
    layout.addWidget(button)
    verticallayout.addLayout(layout)
    view = QWebEngineView()
    verticallayout.addWidget(view)

    def loadPage():
        address_as_string = address.text()
        view.load(QUrl(address_as_string))
    button.clicked.connect(loadPage)
    window.show()
    return app.exec_()

# pionowy suwak i widżet do wpisywania liczb (które można zwiekszac strzałkami)
# suwak i widzet sa połaczone przez connect i przy zmianie wartosci jednego zmienia sie wartosc drugiego
def guiMain2(args):
    app = QApplication(args)
    window = QWidget()
    verticallayout = QVBoxLayout(window)
    slider = QSlider()
    spinbox = QSpinBox()
    verticallayout.addWidget(slider)
    verticallayout.addWidget(spinbox)
    verticallayout.addLayout(verticallayout)

    def updateSpinbox(val):
        spinbox.setValue(val)

    def updateSlider(val):
        slider.setValue(val)
    slider.valueChanged.connect(updateSpinbox)
    spinbox.valueChanged.connect(updateSlider)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
