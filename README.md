# Holiday Cost Calculator

This is a simple Python program that helps calculate the cost of a holiday trip based on the number of hotel nights, flight destination, and car rental days.

## How It Works

The program consists of four functions:

1. `hotel_cost(num_nights)`: Calculates the cost of the hotel stay based on the number of nights. The default rate is £80 per night.

2. `plane_cost(city_flight)`: Calculates the cost of the flight based on the destination city. The rates are as follows:
   - New York: £200
   - Los Angeles: £300
   - Chicago: £250
   - Other cities: £0 (if the input is not valid)

3. `car_rental(rental_days)`: Calculates the cost of the car rental based on the number of rental days. The default rate is £40 per day.

4. `holiday_cost(num_nights, rental_days, city_flight)`: Combines the individual costs of the hotel, flight, and car rental to calculate the total cost of the holiday.

## How to Use

1. Ensure you have Python installed on your machine.

2. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/wasim-jussab/holiday-cost-calculator.git
```

3. Change to the project directory:

```bash
cd holiday-cost-calculator
```

4. Run the program:

```bash
python holiday.py
```

5. Follow the on-screen prompts to enter the details of your holiday trip:
   - Enter the destination city you will be flying to (New York, Los Angeles, Chicago).
   - Enter the number of nights you will be staying at the hotel.
   - Enter the number of days you will be hiring a car for.

6. The program will calculate and display the details of the holiday, including the flight cost, hotel cost, car rental cost, and the total cost of the holiday.

## Contributing

If you'd like to contribute to this project or report any issues, please feel free to open a pull request or submit an issue on the GitHub repository.

---
Created by [Wasim Jussab](https://github.com/wasim-jussab
