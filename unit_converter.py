def convert_length():
    try:
        input_value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (Meters, Feet, Inches): ").lower()
        to_unit = input("Enter the unit to convert to (Meters, Feet, Inches): ").lower()

        # Conversion factors
        conversion_factors = {
            "meters": 1.0,
            "feet": 3.28084,
            "inches": 39.3701,
        }

        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            print("Invalid unit entered.")
        else:
            conversion_factor = conversion_factors[from_unit]
            result = input_value / conversion_factor * conversion_factors[to_unit]
            print(f"Result: {result} {to_unit}")
    except ValueError:
        print("Invalid input.")

print("Length Unit Converter")
while True:
    convert_length()
    another_conversion = input("Do you want to convert another value? (yes/no): ").lower()
    if another_conversion != "yes":
        print("Exiting the unit converter.")
        break
