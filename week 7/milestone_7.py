"""
Author: Ivan Leffalle
Project: W07 - Windchill
"""
winds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

temp = float(input("What is the temperature? "))
grade = input("Fahrenheit or Celsius (F/C)? ")

def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

if grade.lower() == 'c':
    temp = celsius_to_fahrenheit(temp)
    grade = 'F'

def  wind_child(v):
   return 35.74 + 0.6215 * temp - 35.75 * v ** 0.16 + 0.4275 * temp * v ** 0.16
    
for v in winds:
    wc = wind_child(v)
    print(f"At temperature {temp: .1f}{grade.upper()}, and wind speed {v} mph, the windchill is: {wc: .2f}{grade.upper()}")


