# Project: Currency Converter (Indian Rupee to Bangladeshi Taka)
# Created by: Mila Talukder

def convert_currency():
    print("--- Welcome to the INR to BDT Converter ---")
    
    # Static exchange rate (Example: 1 INR = 1.40 BDT)
    # In a real-world app, this could be fetched from an API
    exchange_rate = 1.40 
    
    try:
        # Taking input from the user
        rupee_amount = float(input("Enter amount in Indian Rupee (INR): "))
        
        # Calculation logic
        taka_amount = rupee_amount * exchange_rate
        
        # Displaying the result formatted to 2 decimal places
        print(f"\n[Result] {rupee_amount} INR is equal to {taka_amount:.2f} BDT")
        print("-------------------------------------------")
        
    except ValueError:
        # Error handling if the user enters something other than a number
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    convert_currency()