import datetime
def get_valid_date():
    while True:
        user_input = input("Enter a date in the format YYYY-MM-DD: ")

        try:
            year, month, day = user_input.split('-')

            year = int(year)
            month = int(month)
            day = int(day)

            date = datetime.date(year, month, day)

            return date
        except ValueError as e:

            print(f"Error: {e}. Please ensure you enter a date in the format YYYY-MM-DD and that the date values are valid.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

valid_date = get_valid_date()
print(f"Valid date entered: {valid_date}")