male_age = int(input("Enter male age: "))
female_age = int(input("Enter female age: "))

if male_age >= 21 and female_age >= 18:
    print("Eligible for Marriage ")
else:
    if male_age < 21:
        print("Sorry! Male not eligible ")
    if female_age < 1:
      print("Sorry! Female not eligible ")
