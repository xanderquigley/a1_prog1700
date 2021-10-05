"""
Student Name: Alex Quigley - W0458866
Program Title: IT Data Analytics
Description:   Assignment 1 - Problem 3 - Imperial to Metric Conversion

This program will take an weight in imperial and convert it to the equivalent 
weight in metric.
"""


def main():
    # Start program with output message
    print("Imperial to Metric Conversion")

    # INPUT
    # Here we are going to prompt the user for the inputs of imperial measurements:
    tons = int(input("Enter the number of tons: "))
    stone = int(input("Enter the number of stone: "))
    pounds = int(input("Enter the number of pounds: "))
    ounces = int(input("Enter the number of ounces: "))

    # PROCESSING
    # We need to convert the imperial measurements into metric measurements:
    total_oz = 35840 * tons + 224 * stone + 16 * pounds + ounces    # given formula
    total_kilos = total_oz / 35.274
    metric_tons = int(total_kilos / 1000)

    # The total grams is the decimal of total kilos to the thousandth place
    # we use the mod function to get rid of the integer portion of kilos, then multiply by 1000 to get grams
    grams = (total_kilos % 1) * 1000

    # Format grams and kilos to be used in the output for user friendly viewing of totals
    formatted_grams = round(grams, 1)
    formatted_kilos = int(total_kilos - (metric_tons * 1000))

    # OUTPUT
    # Using concatenation to print the totals of the formatted metric conversions.
    print("The metric weight is " + str(metric_tons) + " metric tons, " + str(formatted_kilos) + " kilos, " + "and " + str(formatted_grams) +" grams.")

if __name__ == "__main__":
    main()