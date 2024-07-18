year_user = int(input("Enter the year of interest: "))

max_year = ""

with open("life-expectancy.csv") as data_file:
    for line in data_file:
        columns = line.strip().split(",")  # Assuming CSV is comma-separated

        try:
            year = int(columns[2])  # Adjust this index based on actual data structure

            if year > max_year:
                max_year = year

        except ValueError:
            continue  # Skip lines where the year conversion fails

if max_year:
    print(f"The highest year after the input year is {max_year}")
else:
    print("No valid year found in the file")
