import datetime


# Getting date of birth (DOB) from user
year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
DOB_user = datetime.date(year, month, day)

# Getting date of death (DOD) of user based on life expectancy
life_expectancy_in_years = 79 # Taken for United States life expectancy stats from https://www.worldometers.info/demographics/life-expectancy/
life_expectancy_in_weeks = life_expectancy_in_years * 52 # 52 weeks in a year
DOD_user= datetime.date(year + life_expectancy_in_years, month, day) 
today = datetime.date.today()

# Getting the number of weeks lived:
delta_life = (today - DOB_user)
# To obtain the number of weeks lived I apply the .days function to Delta and I divide the result by 7. (7 days in a week)
delta_life_weeks = delta_life.days // 7 

# To obtain the numbers of weeks left to live. We compare the number of weeks lived to life expectancy in weeks.
time_left_in_weeks = life_expectancy_in_weeks - delta_life_weeks
print (DOB_user)
print (life_expectancy_in_years)
print (life_expectancy_in_weeks)
print (today)
print (delta_life_weeks)

counter = 0
while counter <= life_expectancy_in_weeks:
    while counter < delta_life_weeks:
        print("X", end = ' ')
        counter += 1
    while counter <= life_expectancy_in_weeks:
        print("0", end = ' ')
        counter += 1

percent_lived = round((delta_life_weeks / life_expectancy_in_weeks), ndigits = 3) * 100
print("\n")
print(f'You have lived {delta_life_weeks} weeks out of {life_expectancy_in_weeks} weeks.\nThat is {percent_lived} % of your life!\nTime to go and get things done!\nGod bless!\n')
