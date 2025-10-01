# BMI Calculator

# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI * 703

def gather_info():
    height = float(input("Your height? (inches or meters): "))
    weight = float(input("Your weight? (pounds or kilograms): "))
    system = input("Imperial or Metric system? (I/M): ").lower().strip()

    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the body Masss Index (BMI) for the
    given weight, height, and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system! Please use imperial or metric.")
