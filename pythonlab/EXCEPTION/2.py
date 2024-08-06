class NotInRangeError(Exception):
    pass

def get_integer_input():
    try:
        user_input = input("Enter an integer between 1 and 1000: ")
        value = int(user_input)
        if value < 1 or value > 1000:
            raise NotInRangeError(f"Error: The value {value} is not between 1 and 1000.")
        print(f"You entered a valid integer: {value}")
    except NotInRangeError as e:
        print(e)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

get_integer_input()