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
    city = input('Select a city: Chicago, New York City, Washington: \n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('Please enter a valid city') 
        city = input ('Choose one: Chicago, New York City, Washington: \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('select a month: January, February, March, April, May, June, or type all to display all: \n').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print('Please enter a valid month') 
        month = input('Choose one: January, February, March, April, May, June, or all: \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Select a day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type all if to display all: \n').lower()
    while day not in ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        print('Please enter a valid day') 
        day = input('Choose one: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, all: \n').lower()


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
    df['day'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    #filtering by month 
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    #filtering by day    
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #print(df['month'])   
    print('The most common month is: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is: {}'.format(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is: {}'.format(df['start hour'].mode()[0]))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip']=df['Start Station']+ ',' + df['End Station']
    print('The most frequent combination of start station and end station trip is: {}'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('The mean travel time: ',(df['Trip Duration'].mean()).round())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nThe counts of user types:\n',user_type)

    # TO DO: Display counts of gender
    # washington has no data about gender
    if city != 'washington': 
        gender = df['Gender'].value_counts()
        print('\nThe genders are:\n',gender)
    else:
        print('\nWashington has no data about gender')
 
    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('\nWashington has no data about Birth year')
    else:
        print('\nThe earliest year of birth is: ', int(df['Birth Year'].min())) 
        print('The most recent year of birth is: ', int(df['Birth Year'].max())) 
        print('The most common year of birth is: ', int(df['Birth Year'].mode()[0])) 
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    valid_choices = ['yes', 'no']
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    while view_data not in valid_choices:
        print('Invalid choice. Please enter either "yes" or "no".')
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        
    start_loc = 0
    while view_data == 'yes':
        print(df[start_loc:start_loc+5])
        start_loc += 5
        
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        while view_data not in valid_choices:
            print('Invalid choice. Please enter either "yes" or "no".')
            view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
