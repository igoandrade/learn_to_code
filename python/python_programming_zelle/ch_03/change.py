# change.py
#   A program to calculate the value of some change in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input(f"{'Quarters':<8s}: "))
    dimes = eval(input(f"{'Dimes':<8s}: "))
    nickels = eval(input(f"{'Nickels':<8s}: "))
    pennies = eval(input(f"{'Pennies':<8s}: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your chance is", total)

if __name__=='__main__':
    main()