def convert_to_float(strings):
    converted_floats = []
    errors = []

    for s in strings:
        try:
            value = float(s)
            converted_floats.append(value)
        except ValueError as e:
            errors.append((s, f"ValueError: {e}"))
        except Exception as e:
            errors.append((s, f"Unexpected error: {e}"))

    return converted_floats, errors
strings = ["12.34","56.78","not_a_number","98.76","","3.14abc",]

converted_floats, errors = convert_to_float(strings)
print("Converted floats:", converted_floats)
print("Errors:")
for error in errors:
    print(f"String: '{error[0]}', Error: {error[1]}")