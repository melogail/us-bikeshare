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
    # declaring variables
    month = 'all'
    day = 'all'

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
    return city, month, day, time_filter


def month_prompt():
    """Ask the user for month filter.

    Returns
    (str) name of the month
    """

    # generate month list
    month_list = []
    for n in range(1, 7):
        month_list.append(calendar.month_name[n].lower())

    while True:
        month = input('Which month? January, February, March, April, May, June\n>>> ').lower()

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
    day_list = []
    for i in range(7):
        day_list.append(i)

    while True:
        try:
            day = int(input("Which day? Please type your response as an integer (e.g., 0=Monday)\n>>> "))
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

    # loading requested file data based on city name
    filename = city.replace(' ', '_') + '.csv'
    df = pd.read_csv(filename)

    # change 'Start Time' and 'End Time' to date object for further processing
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # add month filter
    if month != 'all':
        df = df[df['Start Time'].dt.month_name() == month.title()]

    # add day filter
    if day != 'all':
        df = df[df['Start Time'].dt.dayofweek == day]

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


def trip_duration_stats(df, time_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Duration: {}    Count: {}     ".format(df['Trip Duration'].sum(), df['Trip Duration'].count()), end='')

    # display mean travel time
    print('Avg Duration:{}     Filter: {}'.format(df['Trip Duration'].mean(), time_filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, time_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        print('User Type Statistics...')
        print("Subscribers: {}     Customers:{}     Filter: {}\n".format(len(df[df['User Type'] == 'Subscriber']),
                                                                         len(df[df['User Type'] == 'Customer']),
                                                                         time_filter))

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Gender Statistics...')
        print("Male: {}     Female: {}     Filter: {}\n".format(len(df[df['Gender'] == 'Male']),
                                                                len(df[df['Gender'] == 'Female']),
                                                                time_filter))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('User Age Statistics...')
        print("Earliest: {}    Most Recent:{}     Most Common:{}\n".format(str(int(df['Birth Year'].max())),
                                                                           str(int(df['Birth Year'].min())),
                                                                           str(int(df['Birth Year'].mode()[0]))
                                                                           ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day, time_filter = get_filters()
        df = load_data(city, month, day)

        # time_stats(df)
        # station_stats(df)
        trip_duration_stats(df, time_filter)
        user_stats(df, time_filter)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
