age = int(input("What's your age: "))

if age < 13:
    print("You're not a teenager yet!")
    print("Go back to school.")
elif 13 <= age:
    print("Wow, you're old")
    print("Are you enrolled in highschool?")
else:
    print("You are centuries off pal.")