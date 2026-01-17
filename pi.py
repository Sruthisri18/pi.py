# personal_info.py
# Author: KOlipaka Sruthi Sri
# Project: Personal Information Display Program
# Description: Collects and displays personal information with user input

# Step2: Store static information
name = "Kolipaka Sruthi Sri"                           # Personal name as string
age = 21                                               # Current age as integer
city = "Chennai"                                       # Current city as string
hobby="dance"                                          # Favourite hobby as string

#Step 06: Welcome message
print("=" * 50)
print(" Welcome to Personal Information Display!")
print("=" *50)

#Step 3:
while True:
    favourite_food = input("What is your favourite food? ").strip()
    if favourite_food: #Check if input is not empty
        break
    print(" Pani puri")

while True:
    favourite_color = input("What is your favourite color? ").strip()
    if favourite_color: # Check if input is not empty
        break
    print("Blue")

#Step 6: Calculate age in months
    age_months = age * 12

#Step 4: Display information using f-strings
print("\n" + "=" *50)
print("PERSONAL INFORMATION SUMMARY")
print("=" *50),

print(f"Name: {name}")
print(f"Age: {age} years ({age_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print("-" * 50)
print(f"Your favorite food: {favourite_food}")
print(f"Your favorite color: {favourite_color}")
print("=" * 50)

# Step 6: Goodbye message
print("\nThank you for using Personal Information Display!")
print("Goodbye! 👋")


    
