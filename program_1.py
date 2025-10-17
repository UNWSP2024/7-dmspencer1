# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def calculate_total_rain():
    total = 0
    for rain in monthly_rain:
        total += rain

    return total

def calculate_average_rain():
    total = 0
    for rain in monthly_rain:
        total += rain

    average = total / 12

    return average

monthly_rain = []

for value in range(1, 13):
    rain_amount = float(input(f'How many inches of rain was there in Month {value}?: '))
    monthly_rain.append(rain_amount)

total_rain = calculate_total_rain()
average_rain = calculate_average_rain()

print(f'The total rain is {total_rain:,.2f} inches')
print(f'The average rain is {average_rain:,.2f} inches')
highest = max(monthly_rain)
highest = monthly_rain.index(highest) + 1
lowest = min(monthly_rain)
lowest = monthly_rain.index(lowest) + 1
print(f'The month with the highest rainfall is Month {highest}')
print(f'The month with the lowest rainfall is Month {lowest}')


