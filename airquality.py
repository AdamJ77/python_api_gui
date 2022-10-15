import requests
from datetime import datetime

urls = {
    "findAll": "https://api.gios.gov.pl/pjp-api/rest/station/findAll",
    "sensors": "https://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationId}",
    "getData": "https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensorId}",
    "getIndex": "https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{stationId}"
}


def get_stations():
    stations = requests.get(urls["findAll"]).json()
    all_stations = [Station(station_data) for station_data in stations]
    return all_stations


class AirApiObject:
    def __init__(self, data) -> None:
        self._data = data

    def id(self):
        return self._data["id"]

    def _get(self, key):
        return self._data.get(key)


class Station(AirApiObject):
    def name(self):
        return self._get("stationName")

    def pos(self):
        lat = self._get("gegrLat")
        lon = self._get("gegrLon")
        return (float(lat), float(lon))

    def city_name(self):
        return self._get("city")["name"]

    def city_data(self):
        return self._get("city")

    def sensors(self):
        all_sensors = requests.get(urls["sensors"].format(stationId=self.id()))
        sensors = [Sensor(self, sensor) for sensor in all_sensors.json()]
        return sensors

    def __str__(self):
        return self.name()

    def __repr__(self):
        pass


class Sensor(AirApiObject):
    def __init__(self, station, data) -> None:
        super().__init__(data)
        self._station = station

    def name(self):
        return self._get("param").get("paramName")

    def code(self):
        return self._get("param").get("paramCode")

    def station(self):
        return self._station

    def param_data(self):
        return self._get("param")

    def readings(self):
        result = requests.get(urls["getData"].format(sensorId=self.id())).json()
        key = result["key"]
        values = result["values"]
        return [
            Reading(self,
                    key,
                    datetime.fromisoformat(value["date"]),
                    value["value"])
            for value in values
        ]


class Reading:
    def __init__(self, sensor, key, date, value):
        self._sensor = sensor
        self.key = key
        self.date = date
        self.value = value

    def __str__(self):
        return f'{self.key}: {self.value} on {self.date}'

    def sensor(self):
        return self._sensor
