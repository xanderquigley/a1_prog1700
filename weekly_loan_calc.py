"""
Student Name: Alex Quigley - W0458866
Program Title: IT Data Analytics
Description: Assignment 2 - Problem 2 - Weekly Loan Calulator

This program will calculate weekly payments when given the loan principle, interest rate, and
course of the loan.
"""

def main():
    # Start program with output message
    print("Weekly Loan Calculator\n")

    # INPUT
    principle = float(input("Enter the amount of loan: "))
    interest_rate = float(input("Enter the interest rate (%): "))
    term_in_years = int(input("Enter the number of years: "))

    # PROCESSING
    # Use given formula to calculate i, and then continue with the given formula to calculate weekly payment using i.
    weekly_payment_i = interest_rate / 5200
    weekly_payment = (weekly_payment_i / (1 - (1 + weekly_payment_i) ** (-52 * term_in_years))) * principle
    formatted_payment = "{:.2f}".format(weekly_payment)

    # OUTPUT
    print("\nYour weekly payment will be: $" + str(formatted_payment))

if __name__ == "__main__":
    main()