import requests as req
import json


class Departure:
    def __init__(self, departureTime,departureText,description,vehicleLongitude,routeDirection,route,blockNumber,terminal,actual,gate,vehicleLatitude,vehicleHeading):
        self.departureTime = departureTime
        self.departureText = departureText
        self.description = description
        self.vehicleLongitude = vehicleLongitude
        self.routeDirection = routeDirection
        self.route = route
        self.blockNumber = blockNumber
        self.terminal = terminal
        self.actual = actual
        self.gate = gate
        self.vehicleLatitude = vehicleLatitude
        self.vehicleHeading = vehicleHeading

    def __str__(self):
        return self.route + " " + self.description + " " + self.departureText

    def __repr__(self):
        return self.__str__()

class NexTrip:

    def __init__(self):
        self.base = "http://svc.metrotransit.org/NexTrip/"
        self.json = "?format=json"

    def departures(self, stop):
        r = req.get(self.base + str(stop) + self.json)
        if r.status_code != 200:
            r.close()
            raise RuntimeError, "Invalid status code: " + r.status_code
        if 'application/json;' not in r.headers['content-type']:
            r.close()
            raise RuntimeError, "Response is not json, but:" + r.headers['content-type']
        ret = []
        for depart in r.json():
            ret.append(Departure(depart['DepartureTime'],depart['DepartureText'],depart['Description'],depart['VehicleLongitude'],depart['RouteDirection'],depart['Route'],depart['BlockNumber'],depart['Terminal'],depart['Actual'],depart['Gate'],depart['VehicleLatitude'],depart['VehicleHeading']))
        r.close()
        return ret

if __name__ == "__main__":
    nt = NexTrip()
    print nt.departures(13207)