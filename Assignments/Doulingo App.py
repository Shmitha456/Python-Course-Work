Lesson_ID =input("Enter Lesson_ID (int): ")
Language_Track = input("Enter Language_Track(str): ")
XP_Earned = float(input("Enter XP_Earned: "))
Skill_levels = input("Enter Skill_levels (comma-separated): ").split(',')

Lessons_Available = tuple(map(int, input("Enter Lessons_Available(tuple): ").strip('()').split(',')))
Lessons_Completed = tuple(map(int, input("Enter Lessons_Completed(tuple): ").strip('()').split(',')))

Streak_Bonus = float(input("Enter Streak_Bonus (%): "))
Power_Ups = set(input("Enter Power_Ups (comma-separated)(set): ").split(','))

Coach_Name = input("Enter Coach_Name: ")
Coach_Contact = input("Enter Coach_Contact: ")
Learning_Location = input("Enter Learning_Location: ")
Coach_info = {
    "Coach_Name": Coach_Name,
    "Coach_Contact": Coach_Contact,
    "Learning_Location": Learning_Location
}

# Using Comma Separation(sep=',')
print("\nLesson ID, Language Track, XP Earned :", Lesson_ID, Language_Track, XP_Earned, sep=', ')

# Using Percentage Formatting (% operator)
print("Streak Bonus: %.2f%%" % Streak_Bonus)

# Using f-strings(f"")
print(f"Lesson ID: {Lesson_ID}")
print(f"Language Track: {Language_Track}")
print(f"XP Earned: {XP_Earned}")
print(f"Skill Levels: {', '.join(Skill_levels)}")
print(f"Lessons Available: {Lessons_Available}")
print(f"Lessons Completed: {Lessons_Completed}")
print(f"Streak Bonus: {Streak_Bonus}%")
print(f"Power Ups: {', '.join(Power_Ups)}")

# Using .format() method
print(" Coach: Name - {}, Contact - {}, Location - {}".format(
    Coach_info["Coach_Name"], Coach_info["Coach_Contact"], Coach_info["Learning_Location"]
))