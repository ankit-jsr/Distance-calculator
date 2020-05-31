"""
This program takes inputs of city names and calculates the distance between them
The user can select which dimension they need the result in

Steps:
1. Take in city names
2. Find latitude and longitude of the city
	a. Pull the relevant library to get coordinates of the city
	d. Check with user for the city, state and country names and confirm if they are talking about the same set of cities
3. Create a function to calculate the distance from the coordinates
4. Create a function to convert km to miles and vice-versa
5. Return the distance between the cities

Additional features for expansion:
1. Ability to enter multiple cities and get distances
2. UI to select city names and get results
3. UI showing Google map
4. Ability to check user's location and take it as input into one of 'source' or 'destination'

"""
import math
from geopy.geocoders import Nominatim as nm

global pi,rad_earth
pi = math.pi
rad_earth = 6371

class City():
	def __init__(self,latitude,longitude):
		self.latitude = latitude
		self.longitude = longitude

def dist_calc(city1,city2):
	latr1 = math.radians(city1.latitude)
	latr2 = math.radians(city2.latitude)
	longr1 = math.radians(city1.longitude)
	longr2 = math.radians(city2.longitude)

	dlat = latr1 - latr2
	dlong = longr1 - longr2
	a = math.sin(dlat/2)**2 + math.cos(latr1)*math.cos(latr2)*math.sin(dlong/2)**2

	c = 2*math.asin(math.sqrt(a))
	return "{:.1f}".format(c*rad_earth)


#Main function:
geolocator = nm(user_agent = "Ankit's Calc")

c1 = input("Enter the name of a city: ")
c2 = input("Enter the name of another city: ")
location1 = geolocator.geocode(c1)
location2 = geolocator.geocode(c2)

city_1 = City(location1.latitude,location1.longitude)
city_2 = City(location2.latitude,location2.longitude)

print("The aerial distance between {} and {} is {} km".format(c1,c2,dist_calc(city_1,city_2)))


