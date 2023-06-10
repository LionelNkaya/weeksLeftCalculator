import datetime

# Getting date of birth (DOB) from user
year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
DOB_user = datetime.date(year, month, day)

# Getting life expectancy in weeks
life_expectancy_in_years = 79 # Taken for United States life expectancy stats from https://www.worldometers.info/demographics/life-expectancy/
life_expectancy_in_weeks = life_expectancy_in_years * 52 # 52 weeks in a year
today = datetime.date.today()

# Getting the number of weeks lived:
delta_life = (today - DOB_user)
# To obtain the number of weeks lived I apply the .days function to Delta and I divide the result by 7. (7 days in a week)
delta_life_weeks = delta_life.days // 7 

# To obtain the numbers of weeks left to live. We compare the number of weeks lived to life expectancy in weeks.
time_left_in_weeks = life_expectancy_in_weeks - delta_life_weeks

# Printing in terminal: X for weeks lived and 0 for weeks left to live
counter = 0
while counter <= life_expectancy_in_weeks:
    while counter < delta_life_weeks:
        print("X", end = ' ')
        counter += 1
    while counter <= life_expectancy_in_weeks:
        print("0", end = ' ')
        counter += 1

# Calculating the percentage of life lived
percent_lived = (delta_life_weeks / life_expectancy_in_weeks) * 100

# Providing stats to the user:
print("\n")
print(f'You have lived {delta_life} days in your life. \nThat is {delta_life_weeks} weeks out of {life_expectancy_in_weeks} weeks.\nYou have lived {round(percent_lived)} % of your life!\nTime to go and get things done!\nGod bless!\n')