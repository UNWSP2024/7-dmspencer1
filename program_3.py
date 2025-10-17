# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    repeat = 'y'

    while repeat == 'y':
        year = int(input('What year?: '))
        state = input('What state?: ')
        population = int(input('What was the population?: '))
        all_entered_values.append([year, state, population])
        repeat = input('Do you wish to enter another? (y/n): ')
    # Now have the user enter a year. 
    population_year = int(input('What year would you like the total population for?: '))
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

    sum_population_for_year(all_entered_values, population_year)

def sum_population_for_year(all_entered_values, year_to_sum):
    population_total = 0
    # Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    for year in all_entered_values:
        if year[0] == year_to_sum:
            population_total += year[2]

    # print the totalled population
    print(f'The total population for {year_to_sum} is {population_total:,}')

# Call the main function.
if __name__ == '__main__':
    main()