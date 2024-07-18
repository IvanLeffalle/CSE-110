with open("hr_system.txt") as employees:
    for line in employees: 
        parts = line.split(" ")

        name = parts[0]
        title = parts[2]

        print(f"Name: {name}, Title: {title}")
