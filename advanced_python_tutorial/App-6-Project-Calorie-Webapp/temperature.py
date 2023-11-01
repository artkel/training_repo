class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather_webpage
    """

    def __init__(self, country, city):
        self.city = city
        self.country = country

    def get(self):
        pass
