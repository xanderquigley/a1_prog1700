"""
Student Name: Alex Quigley - W0458866
Program Title: IT Data Analytics
Description:   Assignment 1 - Problem 1 - Hipster's Local Vinyl Records

This program will take in customer information and calculate the total for the customer to pay for the records 
purchased along with the price of delivery.
"""

def main():
    # Print output message to start the program
    print("Hipster's Local Vinyl Records - Customer Order Details")

    # INPUT
    # Create variables to store needed information
    delivery_rate = 15      # $15/km
    tax = 0.14
    cust_name = input("Enter the customer's name: ")
    distance_km = float(input("Enter the distance in kilometers for delivery: "))
    records_cost = float(input("Enter the cost of records purchased: "))

    # PROCESSING
    delivery_cost = float(delivery_rate * distance_km)  # delivery cost is a product of distance and delivery rate
    purchase_cost = float(records_cost * (1 + tax))    # purchase cost is a product of the tax rate and records cost
    total_cost = float(purchase_cost + delivery_cost)  # total cost is the sum of purchase cost and delivery cost

    # Format the variables into a two decimal format to be used later
    formatted_delivery = "{:.2f}".format(delivery_cost)
    formatted_purchase = "{:.2f}".format(purchase_cost)
    formatted_total = "{:.2f}".format(total_cost)

    # OUTPUT
    # We need to print the totals for the user using concatenation of the formatted variables.
    # Make sure to cast as string when printing.
    print("Summary for " + cust_name)
    print("Delivery Cost: $" + str(formatted_delivery))
    print("Purchase Cost: $" + str(formatted_purchase))
    print("Total Cost   : $" + str(formatted_total))

if __name__ == "__main__":
    main()