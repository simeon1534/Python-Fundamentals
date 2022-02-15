class Town:

    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude_input):
        self.latitude_input=latitude_input

    def set_longitude(self, longitude_input):
        self.longitude_input = longitude_input

    def __repr__(self):
        result = f"Town: {self.name} | Latitude: {self.latitude_input} | Longitude: {self.longitude_input }"

        return result


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
