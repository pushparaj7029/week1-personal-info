# Week 1 Personal Information Manager
# Author: Pushpendra Kumar
# Description: This program stores and displays personal information and logs user inputs to a file.

# Step 6: Welcome message
print("=" * 40)
print("     PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Step 2: Static information
name = "Pushpendra Kumar"      # User's name (string)
age = 22                   # User's age (integer)
city = "Jamshedpur JH , IN"     # User's current city (string)
hobby = "Listening Music"   # User's hobby (string)

# Step 3: User input
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Input cannot be empty! Please try again.")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Input cannot be empty! Please try again.")
    favorite_color = input("What's your favorite color? ").strip()

# Step 6: Enhancement – Age in months
age_in_months = age * 12

# Step 4: Display output
print()
print("=" * 40)
print("         YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# NEW FEATURE: Save to test_inputs.txt
with open("test_inputs.txt", "a") as file:
    file.write(f"Food: {favorite_food} | Color: {favorite_color}\n")

# Step 6: Goodbye message
print("=" * 40)
print("Thank you for using the program!")
print("=" * 40)
