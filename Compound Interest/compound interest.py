# compound interest calculator 

print(" \n              ====== Welcome to the compound interest app! ====== ")
print(" ====== See how much you invest with a simple app without the hidden bank fees ====== ")
print("\n                  ===== Input starting amount ===== ")
print("                  ===== Input interest rate ===== ")
print("     ====== Input total amount of years inveseted or plan to invest ====== ")


def compound_interest(): 
    while True: 
        try:
            principle = float(input("\nplease enter your starting amount: "))
    
            rate = float(input("please enter your rate: "))
            if rate > 1:
                rate = rate / 100.0
              
            n = float(input("Please enter monthly cycle for interest per year: "))
    
            time = float(input("please enter how many years you have invested or plan to invest: "))
    
            total = principle * (1 + rate / n) ** (n * time) 

            print(f"\nYour total compound interest is: ${total:.2f} ")

        except ValueError:
            print("Please use a number, cannot use symbols 😊") 

compound_interest()



