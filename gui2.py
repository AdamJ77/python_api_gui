from PySide2.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QWidget, QLineEdit, QPushButton
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PySide2.QtGui import QPixmap
import sys
from ui_airquality import Ui_MainWindow
from airquality import get_stations
from matplotlib import pyplot as plt
from io import BytesIO


def generate_plot(sensor, name):
    readings = sensor.readings()
    keys = [reading.date for reading in readings]
    value = [reading.value for reading in readings]
    plt.plot(keys, value, "o-", label=sensor.name(), markersize=3)
    plt.legend()
    plt.title(label=sensor.station().name())
    plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.clf()
    return buffer.getvalue()


class AirQualityWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupStationList()

    def _setupStationList(self):
        stations = get_stations()
        for station in stations:
            item = QListWidgetItem(str(station))
            item.station = station
            self.ui.stations.addItem(item)
        self.ui.stations.itemClicked.connect(self._selectStation)
        self.ui.sensors.itemClicked.connect(self._selectSensor)

    def _selectStation(self, item):
        self.ui.stack.setCurrentIndex(1)
        stationName = item.station.name()
        self.ui.stationName.setText(stationName)
        sensors = item.station.sensors()
        self.ui.sensors.clear()
        for sensor in sensors:
            sensor_item = QListWidgetItem(sensor.name())
            sensor_item.sensor = sensor
            self.ui.sensors.addItem(sensor_item)

    def _selectSensor(self, item):
        sensor = item.sensor
        image_data = generate_plot(sensor)
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.plot.setPixmap(pixmap)


def guiMain(args):
    app = QApplication(args)
    window = AirQualityWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
