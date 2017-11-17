# Jamshed Ashurov
# 11/17/2017
# trip.py
# This file creates a class that will import the information from Google API and determine the distance and the
# duration of the trip.


class Trip:

    def __init__(self, origins, destinations, mode, sensor):
        """
        This function locates all the parameters: the starting and final position, the mode of the
        trip(driving, walking, and bicycle), and sensor. Moreover, it includes the the url line that will get the
        information from the Google API, the distance and the duration of the trip. As a whole, this function serves as
        a main function.
        :param origins:
        :param destinations:
        :param mode:
        :param sensor:
        """
        self.origins = origins
        self.destinations = destinations
        self.sensor = sensor
        self.mode = mode
        self.url = ""
        self.thecities()
        self.results = self.result()
        self.distance = "The distance is " + self.getdistance()
        self.duration = "The duration is " + self.getduration()

    def thecities(self):
        """
        This function replaces the spaces in the starting and the final position to the +, to make the url line work.
        Then, it adds the parameters to form a url line that will import the information from the Google API.
        :return:
        """
        self.origins = self.origins.replace(" ", "+")
        self.destinations = self.destinations.replace(" ", "+")
        self.url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + self.origins + \
                   "&destinations=" + self.destinations + "&mode=" + self.mode + "&sensor=" + self.sensor

    def result(self):
        """
        This function takes the url line and sends the information to the API and then returns the results.
        :return:
        """
        import urllib.request
        web_obj = urllib.request.urlopen(self.url)
        results_str = str(web_obj.read())
        web_obj.close()
        return results_str

    def getdistance(self):
        """
        This function takes the results from the Google API and finds the value of the distance. As the distance of the
        trip will always have the same distance from the word "text" in the results, our starting position will be
        start+9 which is the distance between the "text" and the distance value. Furthermore, the ending of the
        distance value will always be "km", so our ending position wil be end+2, so that it would include "km" too.
        :return:
        """
        start = self.results.find("text")
        end = self.results.find("km")
        return self.results[start+9:end+2]

    def getduration(self):
        """
        This function takes the results from the Google API and finds the value of the duration of the trip.
        As the duration of the trip will always be located in the same distance from the word "duration" in the results,
         our starting position will be start+43 which is the distance between the "duration" and the duration value.
         Furthermore, the ending of the duration value will always be "," after the "duration" text in the results, so
         our ending position wil be end-1, so that it would find the duration.
        :return:
        """
        start = self.results.find("duration")
        end = self.results.find(",", start+40)
        return self.results[start+43:end-1]

    def __str__(self):
        """
        This function replaces the + of the starting and the final destination of the trip to spaces again and allows
         to print it out.
        :return:
        """
        self.origins = self.origins.replace("+", " ")
        self.destinations = self.destinations.replace("+", " ")
        return "Origin: " + self.origins + ". Destination: " + self.destinations + ". Mode: " + self.mode







