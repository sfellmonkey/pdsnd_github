import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
   Asks user to specify a city, month, and day to analyze.

   Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
   """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Choose a city between Chicago, New York City, Washington: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('Please enter a valid city')
        city = input("Choose a city between Chicago, New York City, Washington: ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Choose a month between January and June. If you would like to look at all months please enter all: ").lower()

    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('Please enter a valid month')
        month = input("Choose a month between January and June. If you would like to look at all months please enter all: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day you would like to explore. If you want to look at all days please enter all: ").lower()

    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('Please enter a valid day')
        day = input("Choose a day you would like to explore. If you want to look at all days please enter all: ").lower()

    print('-'*40)
    return city, month, day



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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month was: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day was: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour was: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common starting station was: ', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station was: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df['trip'].mode()[0]
    print('The most common combination of start station and end station trip was: ', most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {}.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of gender:', gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode())
        print('The earliest year of birth is {}.\n'
        'The most recent year of birth is {}.\n'
        'The most common year of birth is {}.'.format(earliest_yob, most_recent_yob, most_common_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        first_five_rows = input('Would you like to see 5 rows of data?\nPlease enter yes or no.').lower()
        if first_five_rows in ('yes', 'y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                next_five_rows = input('Would you like to see another 5 rows of data?\nPlease enter yes or no\n').lower()
                if next_five_rows in ('yes', 'y'):
                    i = 0
                    while True:
                        print(df.iloc[i:i+5])
                        i += 5
                        more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
                        if more_data not in ('yes', 'y'):
                            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
