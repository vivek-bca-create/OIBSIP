def calculate_bmi(weight, height):
    """
    Formula for BMI calculation: weight (kg) / (height (m) ** 2)
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def get_bmi_category(bmi):
    """
    Determine the weight category based on the BMI value
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 45)
    print("      Oasis Infobyte - BMI Calculator        ")
    print("=" * 45)
    
    try:
        # Taking inputs from user
        weight = float(input("Enter your weight in Kilograms (kg): "))
        height_cm = float(input("Enter your height in Centimeters (cm): "))
        
        # Converting centimeters to meters
        height_m = height_cm / 100
        
        if weight <= 0 or height_cm <= 0:
            print("\n Error: Weight and height must be greater than 0!")
            return
            
        # Calculation and output result
        bmi = calculate_bmi(weight, height_m)
        
        if bmi:
            category = get_bmi_category(bmi)
            print("\n" + "-" * 30)
            print(f" Your BMI is: {bmi}")
            print(f" Category: {category}")
            print("-" * 30)
        else:
            print("\n Something went wrong. Please enter valid inputs.")
            
    except ValueError:
        print("\n Error: Please enter numbers only!")

if __name__ == "__main__":
    main()
