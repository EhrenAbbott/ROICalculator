# # We will continue practicing Object Oriented Programming in this assignment to become more fluent in Python. 
# # Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# # Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video 
# # of what Brandon usually does to calculate his Rental Property ROI.
# # Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program 
# # that will calculate the Return on Investment(ROI) for a rental property.
# # This project will be completed individually, though you can feel free to share ideas with your fellow students.
# # Once completed, commit the project to github and submit the link to this assignment.


import time

class ROI(): 
    
    def income(self): 
        while True:
            rental_income_answer = input("What is the monthly rental income of your property?")
            if rental_income_answer: 
                try:  
                    rental_income_answer = float(rental_income_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid number.")
        while True: 
            laundry_income_answer = input("If you have monthly laundry income, please enter the amount. Otherwise, enter '0'.")
            if laundry_income_answer.lower() == "0": 
                break 
            else: 
                try:  
                    laundry_income_answer = float(laundry_income_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.") 
        while True: 
            storage_income_answer = input("If you have monthly storage income, please enter the amount. Otherwise, enter '0'.")
            if storage_income_answer.lower() == "0": 
                break 
            else: 
                try:  
                    storage_income_answer = float(storage_income_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.") 
        while True: 
            misc_income_answer = input("If you have any other monthly, miscellaneous income, please enter the amount. Otherwise, enter '0'.")
            if misc_income_answer.lower() == "0": 
                break 
            else: 
                try:  
                    misc_income_answer = float(misc_income_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.")  
        income_answer = int(rental_income_answer) + int(laundry_income_answer) + int(storage_income_answer) + int(misc_income_answer)
        time.sleep(1)
        print(f"Your total monthly income for this property is: ${income_answer}.") 
        time.sleep(1)
        print("Time to calculate your expenses.")
        time.sleep(1)
        while True: 
            yearly_tax_answer = input("What are your yearly taxes?")
            try:  
                yearly_tax_answer = float(yearly_tax_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.") 
        while True: 
            yearly_insurance_answer = input("How much for you pay for insurance a year?")
            try:  
                yearly_insurance_answer = float(yearly_insurance_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.")
        while True: 
            electric_answer = input("What is your monthly electric bill?")
            try:  
                electric_answer = float(electric_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.")
        while True: 
            gas_answer = input("What is your monthly gas bill?")
            try:  
                gas_answer = float(gas_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.")
        while True: 
            water_answer = input("What is your monthly sewerage and water bill?")
            try:  
                water_answer = float(water_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.")
        while True: 
            trash_answer = input("What is your monthly cost of trash collection?")
            try:  
                trash_answer = float(trash_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.")
        while True: 
            HOA_answer = input("If you have monthly HOA fees, please enter the amount. Otherwise, enter '0'.")
            if HOA_answer.lower() == "0": 
                break 
            else: 
                try:  
                    HOA_answer = float(HOA_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.") 
        while True: 
            lawnsnow_answer = input("If you have monthly landscaping/lawn care costs, please enter the amount. Otherwise, enter '0'.")
            if lawnsnow_answer.lower() == "0": 
                break 
            else: 
                try:  
                    lawnsnow_answer = float(lawnsnow_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.") 
        while True: 
            units_answer = input("How many units does your property have?")
            try:  
                units_answer = float(units_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.") 
        time.sleep(1)  
        print(f"This means you should set aside ${100*int(units_answer)} per month for repairs and capital expenditures (each).")
        repairs_expense = int(units_answer)*100 
        capex_expense = int(units_answer)*100
        vacancy = (int(rental_income_answer)*.05)*units_answer
        time.sleep(2)
        print(f"Based on your monthly rental income, you should also set aside ${vacancy} a month for anticipated vacancy.")
        time.sleep(2) 
        while True: 
            manager_answer = input("If you pay someone to manage this property, please enter their monthly salary (for this property only). Otherwise, enter '0'.")
            if manager_answer.lower() == "0": 
                break 
            else: 
                try:  
                    manager_answer = float(manager_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.") 
        time.sleep(1)
        print("Almost done with expenses!")
        time.sleep(1)
        while True: 
            mortgage_answer = input("What is your monthly mortgage payment?")
            try:  
                mortgage_answer = float(mortgage_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.") 
        time.sleep(2)
        expenses_answer = int(mortgage_answer) + int(manager_answer) + int(capex_expense) + int(repairs_expense) + int(lawnsnow_answer) + int(HOA_answer) + int(trash_answer) +int(water_answer) + int(gas_answer) + int(electric_answer) + (int(yearly_tax_answer)/12) + (int(yearly_insurance_answer)/12) + int(vacancy)
        print(f"Your total monthly expenses come to: ${expenses_answer}.")
        time.sleep(2)
        cash_flow = income_answer - expenses_answer 
        print(f"And your monthly cash flow is: ${cash_flow}")
        time.sleep(2)
        print("Now to calcualte your intial investment.")
        while True: 
            down_payment_answer = input("How much did you pay for the down payment on this property?")
            try:  
                down_payment_answer = float(down_payment_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.") 
        while True: 
            closing_answer = input("What were the associated closing costs?")
            try:  
                closing_answer = float(closing_answer.replace(",","").strip('$'))
                break
            except: 
                print("Please enter a valid response.") 
        while True: 
            reno_answer = input("If you invested any money upfront on renovations to the property, please enter that amount here. Otherwise, enter '0'.")
            if reno_answer.lower() == "0": 
                break 
            else: 
                try:  
                    reno_answer = float(reno_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.")
        while True: 
            misc_inv_answer = input("If you had any other miscellaneous investment expenses, please enter that amount here. Otherwise, enter '0'.")
            if misc_inv_answer.lower() == "0": 
                break 
            else: 
                try:  
                    misc_inv_answer = float(misc_inv_answer.replace(",","").strip('$'))
                    break
                except: 
                    print("Please enter a valid response.")
        investment_answer = int(misc_inv_answer) + int(reno_answer) + int(closing_answer) + int(down_payment_answer)
        time.sleep(2)
        print(f"Your total initial investment for this property was: ${investment_answer}")
        CoCROI = ((cash_flow * 12)/investment_answer)*100
        print(f"This means your Cash on Cash ROI is: {CoCROI}%")
    
my_property = ROI()

def runROI():
    my_property.income() 
    while True: 
        continue_q = input("Would you like to continue using the ROI calculator?")
        if continue_q.lower().strip('.') == "no": 
            print("Thank you for using the ROI Calculator!")
            break 
        elif continue_q.lower().strip('.') == "yes":
            my_property.income()
        else: 
            print("Please enter 'yes' or 'no'")
        
runROI()
