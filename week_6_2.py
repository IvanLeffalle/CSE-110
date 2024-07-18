people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]



youngest_age = 9999
youngest_name = ""
for person_line in people:
    new_list = person_line.split()

    name = new_list[0]
    age = int(new_list[1])

    if age < youngest_age:
        youngest_age = age

        youngest_name = name

print(f"The youngest age is: {youngest_age}")
print(f"The youngest name is: {youngest_name}")