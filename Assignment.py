print("Please enter the following information:")
print("")

first_name = input("First name:")
last_name = input("Last name:")
email = input("Email address:")
phone_number = input("Phone number:")
job_title = input("Job title:")
id_number = input("ID number:")
print("")
print("The ID Card is:")
print("----------------------------------------")
output = f"{last_name.upper()}, {first_name}\n"
output += f"{job_title.capitalize()}\n"
output += f"ID: {id_number}\n"
print("")
output += f"{email.lower()}\n"
output += f"{phone_number}\n"
print(output.strip())
print("----------------------------------------")

