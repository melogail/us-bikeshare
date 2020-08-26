import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # declaring some default variables
    month = None
    day = None

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, Washington?\n>>> ")
        # validate user input
        if city in CITY_DATA:
            break

    # prompting the user for time filter
    while True:
        time_filter = input("Would you like to filter the data by month, day, both or not at all? type 'none' "
                            "for not time filter.\n>>> ")

        # get user input for month (all, january, february, ... , june)
        if time_filter == 'month':
            month = month_prompt()
            break

        # get user input for day of week (all, monday, tuesday, ... sunday)
        elif time_filter == 'day':
            day = day_prompt()
            break

        # get user input for both day and time
        elif time_filter == 'both':
            month = month_prompt()
            day = day_prompt()
            break

        elif time_filter == 'none':
            break

    print('-' * 40)
    return city, month, day


def month_prompt():
    """Ask the user for month filter.

    Returns
    (str) name of the month
    """

    # generate month list
    month_list = ['all']
    for n in range(1, 7):
        month_list.append(calendar.month_name[n].lower())

    while True:
        month = input('Which month? January, February, March, April, May, June\n>>>').lower()

        if month in month_list:
            break
        else:
            print("Please choose one of specified months and make sure you type month name correctly!")

    return month


def day_prompt():
    """Ask user for choosing day of the week using integers as response to day number.

    Return:
    (int) day
    """
    day_list = ['all']
    for i in range(1, 8):
        day_list.append(i)

    while True:
        try:
            day = int(input("Which day? Please type your response as an integer (e.g., 1=Sunday)\n>>>"))
            if day in day_list:
                break
            else:
                print("Please choose your day as specified!")
        except ValueError:
            print("Please specify a number for day!")

    return day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        #df = load_data(city, month, day)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
