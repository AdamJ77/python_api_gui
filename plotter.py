import airquality
import sys
from random import choice
from matplotlib import pyplot as plt
import argparse


# matplotlib.use("Qt5Agg")
def list_stations(args):
    pattern = args.list_stations
    all_stations = airquality.get_stations()
    for station in all_stations:
        if pattern in station.name():
            print(f"{station.id()}\t{station}")


def main(arguments):
    parser = argparse.ArgumentParser
    parser.add_argument("--list-stations")
    args = parser.parse_args(arguments[1:])

    if args.list_stations:
        list_stations(args)
        return
    all_stations = [
        station
        for station in airquality.get_stations()
        if station.city_name() == "Warszawa"]
    station = choice(all_stations)
    all_sensors = station.sensors()
    for sensor in all_sensors:
        if sensor.code() == "CO":
            continue
        readings = sensor.readings()
        keys = [reading.date.strftime('%d.%m. %H:%M') for reading in readings]
        value = [reading.value for reading in readings]
        plt.plot(keys, value, "o-", label=sensor.name(), markersize=3)
    plt.legend()
    plt.title(label=station.name())
    plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
    figure = plt.gcf()
    plt.show()
    if args.save:
        figure.savefig(args.save, format="pdf")


if __name__ == "__main__":
    main(sys.argv)
