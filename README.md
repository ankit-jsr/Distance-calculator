# Distance-calculator
Calculate distance between two entered cities

This program takes inputs of city names and calculates the distance between them
The user can select which dimension they need the result in

Steps:
1. Take in city names
2. Find latitude and longitude of the city
	a. Check edge cases for cities having same names - take country name as well
	b. Spellings of names entered could be incorrect - give a drop down suggestion as soon as the user types in the name
	c. Pull the relevant library to get coordinates of the city
	d. Check with user for the city, state and country names and confirm if they are talking about the same set of cities
3. Create a function to calculate the distance from the coordinates
4. Create a function to convert km to miles and vice-versa
5. Return the distance between the cities

Additional features for expansion:
1. Ability to enter multiple cities and get distances
2. UI to select city names and get results
3. UI showing Google map
4. Ability to check user's location and take it as input into one of 'source' or 'destination'
