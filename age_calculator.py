
from datetime import date

print("===== AGE CALCULATOR =====")

# Get date of birth from user
day = int(input("Enter your birth day: "))
month = int(input("Enter your birth month: "))
year = int(input("Enter your birth year: "))

# Store date of birth
dob = date(year, month, day)

# Get today's date
today = date.today()

# Check valid date
if dob > today:
    print("Invalid date of birth!")
else:
    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    if age_days < 0:
        age_months -= 1
        previous_month = today.month - 1

        if previous_month == 0:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_year = today.year

        days_in_month = (
            date(today.year, today.month, 1) -
            date(previous_year, previous_month, 1)
        ).days

        age_days += days_in_month

    if age_months < 0:
        age_years -= 1
        age_months += 12

    print("\nYour Age Is:")
    print("Years:", age_years)
    print("Months:", age_months)
    print("Days:", age_days)
