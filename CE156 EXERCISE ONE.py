#OBTAIN TODAY'S DATE
from datetime import date
#DEFINE A FUNCTION THAT CHECKS A VALID DATE
def valid_date(date_string):
    try:
        day, month, year = map(int, date_string.split('/'))
        #CHECK IF THE DATE IS VALID
        if_date_valid = date(year, month, day)
        return if_date_valid
    except ValueError:
        return None
#DEFINE A FUNCTION THAT CALCULATE'S AGE
def calculate_age(birth_date):
    #OBTAIN A DATE OBJECT CONTAINING TODAY'S DATE
    today = date.today()
    # CHECK IF THE BIRTHDAY HAS OCCURRED THIS YEAR OR PASSED
    if_birthday_passed = (today.month, today.day) >= (birth_date.month, birth_date.day)
    age = today.year - birth_date.year - (not if_birthday_passed)
    return age
#WRITE THE PROGRAM THAT ASK THE USER TO INPUT HIS/HER DATE OF BIRTH IN THE FORMAT dd/mm/yyyy
def main():
    while True:
        user_input = input("Enter your date of birth (dd/mm/yyyy): ")
        birth_date = valid_date(user_input)
        if birth_date:
            age = calculate_age(birth_date)
            print(f"You are {age} years old.")

            today = date.today()
            if (today.month, today.day) == (birth_date.month, birth_date.day):
                print("Happy birthday!")
            break
        else:
            print("Invalid date format or date. Please enter a valid date.")

if __name__ == "__main__":
    main()
