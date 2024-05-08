# Author: Matheus Tecchio, Jordan Buckley, Schumaicher Monteiro and Mohhammed Mohammed
# Data: 06/04/2024

# The main code that runs the interactive menu to execute all our functions.

import water_charges
import school_transport
import TFAandMonthlyPay
import property_tax

# Display the menu
def menu():
    while(True):
        print("\n--Welcome To The Multi-Bill Calculator Menu--")
        print("_" * 35)
        print("1. Tax")
        print("2. Monthly Pay for Sales Employees")
        print("3. Water Charges")
        print("4. Property Tax")
        print("5. School Transport")
        print("0. Exit")
        print("_" * 35)
        option = int(input("Choose an option (0-5): "))
        print("\n")

        if option == 1:
            TFAandMonthlyPay.calculate_tax()
        elif option == 2:
            TFAandMonthlyPay.monthly_pay()
        elif option == 3:
            water_charges.calculate_charges()
        elif option == 4:
            property_tax.calculate_property_tax()
        elif option == 5:
            school_transport.calculate_transport_cost()
        elif option == 0:
            pass
        else:
            print("Sorry, this option does not exist!")
if __name__ == "__main__":
    menu()