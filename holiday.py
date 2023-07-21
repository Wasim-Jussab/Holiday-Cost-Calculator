# Function to calculate the cost of the hotel stay
def hotel_cost(num_nights):
    return num_nights * 80 

# Function to calculate the cost of the flight
def plane_cost(city_flight):
    if city_flight.lower() == "new york":
        return 200  
    elif city_flight.lower() == "los angeles":
        return 300  
    elif city_flight.lower() == "chicago":
        return 250  
    else:
        return 0  # If the input is not valid, return 0 for the cost

# Function to calculate the cost of the car rental
def car_rental(rental_days):
    return rental_days * 40 

# Function to calculate the total holiday cost
def holiday_cost(num_nights, rental_days, city_flight):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    return hotel + plane + car

# Getting user inputs
city_flight = input("Enter the city you will be flying to (New York, Los Angeles, Chicago): ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Calling the holiday_cost function to calculate the total holiday cost
total_cost = holiday_cost(num_nights, rental_days, city_flight)

# Printing the details of the holiday
print("Your trip to " + city_flight + " for " + str(num_nights) + " nights:")
print("Flight cost: £" + str(plane_cost(city_flight)))
print("Hotel cost: £" + str(hotel_cost(num_nights)))
print("Car rental cost: £" + str(car_rental(rental_days)))
print("Total cost of holiday: £" + str(total_cost))
