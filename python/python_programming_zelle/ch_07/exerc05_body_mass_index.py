"""
The body mass index (BMI) is calculated as a person's weight (in pounds)
times 720, divided by the square of the person's height (in inches). A BMI
in the range 19-25, inclusive, is considered healthy. Write a program that
calculates a person's BMI and prints a message telling whether they are
above, within, or below the healthy range.
"""

def body_mass_index(weight, height):
    bmi = 120 * weight / height**2
    return bmi

def bmi_classification(bmi):
    if (bmi > 25):
        classification = "above"
    elif (bmi >= 19):
        classification = 'within'
    else:
        classification = 'below'
    print(f"You are {classification} the healthy range.")

if __name__=="__main__":
    w = float(input("Enter your weight (in pounds): "))
    h = float(input("Enter your height (in inches): "))
    bmi = body_mass_index(weight=w, height=h)
    print(f"Your body mass index (BMI) is {bmi:>.2f}.")
    bmi_classification(bmi)