
# FitBuddy - AI Fitness Plan Generator

print("===== Welcome to FitBuddy =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
goal = input("Enter your fitness goal (Weight Loss / Fitness / Muscle Gain): ")
level = input("Enter your fitness level (Beginner / Intermediate): ")

print("\n===== Your Personal Fitness Plan =====")
print("Name:", name)
print("Age:", age)
print("Goal:", goal)
print("Fitness Level:", level)

if goal.lower() == "weight loss":
    print("\nYour Workout Plan:")
    print("1. Walking - 20 minutes")
    print("2. Light Cardio - 10 minutes")
    print("3. Stretching - 5 minutes")

elif goal.lower() == "fitness":
    print("\nYour Workout Plan:")
    print("1. Walking - 15 minutes")
    print("2. Bodyweight Exercises - 10 minutes")
    print("3. Stretching - 5 minutes")

elif goal.lower() == "muscle gain":
    print("\nYour Workout Plan:")
    print("1. Squats - 10 repetitions")
    print("2. Wall Push-ups - 10 repetitions")
    print("3. Light Exercises - 10 minutes")

else:
    print("Please enter a valid fitness goal.")

print("\nThank you for using FitBuddy!")
