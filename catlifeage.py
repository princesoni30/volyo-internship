def cat_to_human_age(age):
    if age <= 2:
        return age * 12.5
    else:
        return 25 + (age - 2) * 4

# Input
age = int(input("Enter cat age: "))
print("Human age:", cat_to_human_age(age))