# User inputs
city_flight = input("Please enter the city you are flying to: ").upper()
num_nights = int(input("Please enter the number of nights you are staying: "))
rental_days = int(input("Please enter the number of days you will be hiring a car: "))

def hotel_cost(num_nights, multiplier):
    # Calculate the total hotel cost based on the number of nights and the multiplier
    return num_nights * multiplier


def plane_cost(city_flight):
    # Calculate the flight cost based on the destination city
    # Assuming different flight costs for each city
    if city_flight == "TIRANE":
        return 400
    elif city_flight == "ANKARA":
        return 500
    elif city_flight == "DHAKA":
        return 150
    elif city_flight == "NEW DELHI":
        return 800
    elif city_flight == "LJUBLJANA":
        return 1500
    elif city_flight == "MADRID":
        return 1230
    else:
        print("This is not in my database")
        exit()


def car_rental_cost(rental_days, daily_cost):
    # Calculate the total car rental cost based on the number of rental days and daily cost
    return rental_days * daily_cost


def holiday_cost(city_flight, num_nights, rental_days):
    # Location-specific multipliers for hotel cost
    hotel_multiplier = {
        "TIRANE": 120,
        "ANKARA": 110,
        "DHAKA": 90,
        "NEW DELHI": 100,
        "LJUBLJANA": 130,
        "MADRID": 120
    }

    # Daily rental cost for car
    car_daily_cost = 50

    # Calculate individual costs
    flight_cost = plane_cost(city_flight)
    hotel_total_cost = hotel_cost(num_nights, hotel_multiplier.get(city_flight, 100))
    car_total_cost = car_rental_cost(rental_days, car_daily_cost)

    # Total holiday cost
    total_holiday_cost = flight_cost + hotel_total_cost + car_total_cost

    return flight_cost, hotel_total_cost, car_total_cost, total_holiday_cost



# Calculate and print holiday details
flight_cost, hotel_total_cost, car_total_cost, total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

# Display results
print("\nHoliday Details:")
print(f"Flight cost: £{flight_cost}")
print(f"Hotel cost: £{hotel_total_cost}")
print(f"Car rental cost: £{car_total_cost}")
print(f"Total holiday cost: £{total_holiday_cost}")
