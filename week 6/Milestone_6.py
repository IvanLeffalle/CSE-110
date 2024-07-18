"""
Author: Ivan Leffalle
Project: Project 06: Data Analysis
"""
#for creativity I added on line 64 an option to allow the user to type a country, 
#then display the minimum and maximum life expectancy for that country.  
with open("life-expectancy.csv") as data_file:
    max_expectancy = -1
    max_expectancy_name = ""
    max_expectancy_year = ""

    min_expectancy = 999999999999
    min_Expectancy_name = ""
    min_Expectancy_year= 99999

    total_expectancy = 0
    count = 0

    max_expectancy_user = -1
    max_expectancy_name_user = ""

    min_expectancy_user = 999999999999999
    min_Expectancy_name_user = ""

    max_expectancy_user_country = 0
    min_expectancy_user_country = 9999999999999999999999999999
#I used this option to skip the header
    next(data_file)

    user_year = int(input("Enter the year of interest: "))
#new question for creativity
    user_country = input("Please enter a country: ")

    for line in data_file:
        parts = line.split(",")

        country = parts[0]
        year = int(parts[2])
        expectancy = float(parts[3])

        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_Expectancy_name = country
            min_Expectancy_year = year
        
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_Expectancy_name = country
            max_Expectancy_year = year
            
        if user_year == year:
            total_expectancy += expectancy
            count += 1
            if expectancy > max_expectancy_user:
                max_expectancy_user = expectancy
                max_expectancy_name_user = country
            
            if expectancy < min_expectancy_user:
               min_expectancy_user = expectancy
               min_Expectancy_name_user = country

        if user_country.lower() == country.lower():
            if expectancy > max_expectancy_user_country:
                max_expectancy_user_country = expectancy
            if expectancy < min_expectancy_user_country:
                min_expectancy_user_country = expectancy
            

if count > 0:
    average_expectancy = total_expectancy / count
        



print(f"\nThe overall min life expectancy is: {max_expectancy} from {max_Expectancy_name} in {max_Expectancy_year}")
print(f"The overall min life expectancy is: {min_expectancy} from {min_Expectancy_name} in {min_Expectancy_year}")
print(f"\nFor the year {user_year}:")
print(f"The average life expectancy across all countries was {average_expectancy: .2f}")
print(f"The max life expectancy was in {max_expectancy_name_user} with {max_expectancy_user}")
print(f"The min life expectancy was in {min_Expectancy_name_user} with {min_expectancy_user}")
print("")
print(f"For {user_country}: ")
print(f"The max life expectancy is: { max_expectancy_user_country: .2f} ")
print(f"The min life expectancy is: { min_expectancy_user_country: .2f} ")




